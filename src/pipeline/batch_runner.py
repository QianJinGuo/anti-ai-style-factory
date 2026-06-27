#!/usr/bin/env python3
"""
Batch Runner — XFYUN Batch API pipeline for anti-AI-style-factory.
================================================================
Two-phase batch generation:
  Phase A: All seeds → DESIGN.md (one batch)
  Phase B: All DESIGNs → reference.html (one batch)
  Phase C: Score all HTMLs locally, save passing ones

Usage:
  python -m src.pipeline.batch_runner --submit-design --limit 100   # submit phase A
  python -m src.pipeline.batch_runner --poll                        # poll all open batches
  python -m src.pipeline.batch_runner --consume                     # process completed phase A → submit phase B
  python -m src.pipeline.batch_runner --finalize                    # process completed phase B → score & save
  python -m src.pipeline.batch_runner --status                      # show batch state

State file: state/batches.json — tracks all submitted batches.
"""

import argparse
import json
import re
import subprocess
import sys
import time
import uuid
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.scorer.eight_dim import score_html
from src.generator.llm_generator import (
    SYSTEM_PROMPT,
    build_design_md_prompt,
    build_reference_html_prompt,
    extract_code_block,
    resolve_api_key,
)
from src.pipeline.run import parse_seeds, get_style_status

BATCH_HOST = "https://spark-api-open.xf-yun.com"
STATE_DIR = PROJECT_ROOT / "state"
STATE_FILE = STATE_DIR / "batches.json"
JSONL_DIR = PROJECT_ROOT / "state" / "jsonl"


# ── API key resolution ──
def get_api_key(config: dict) -> str:
    """Resolve the active provider's API key (delegates to the shared resolver)."""
    return resolve_api_key(config)


def load_config() -> dict:
    return yaml.safe_load((PROJECT_ROOT / "config" / "pipeline.yaml").read_text())


# ── State management ──
def load_state() -> dict:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"batches": []}


def save_state(state: dict):
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False))


# ── XFYUN Batch API ──
def http_request(method: str, url: str, key: str, body=None, content_type=None, raw=False):
    headers = {"Authorization": f"Bearer {key}"}
    if content_type:
        headers["Content-Type"] = content_type
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = r.read()
            return data if raw else json.loads(data)
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {e.code} on {method} {url}: {err_body}")


def upload_jsonl(key: str, jsonl_path: Path) -> str:
    """Upload jsonl, return file_id."""
    boundary = uuid.uuid4().hex
    file_bytes = jsonl_path.read_bytes()
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="purpose"\r\n\r\nbatch\r\n'
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{jsonl_path.name}"\r\n'
        f"Content-Type: application/octet-stream\r\n\r\n"
    ).encode() + file_bytes + f"\r\n--{boundary}--\r\n".encode()

    resp = http_request(
        "POST", f"{BATCH_HOST}/v1/files",
        key=key, body=body,
        content_type=f"multipart/form-data; boundary={boundary}"
    )
    return resp["id"]


def create_batch(key: str, file_id: str, description: str) -> dict:
    payload = json.dumps({
        "input_file_id": file_id,
        "endpoint": "/v1/chat/completions",
        "completion_window": "24h",
        "metadata": {"description": description}
    }).encode()
    return http_request(
        "POST", f"{BATCH_HOST}/v1/batches",
        key=key, body=payload, content_type="application/json"
    )


def get_batch(key: str, batch_id: str) -> dict:
    return http_request("GET", f"{BATCH_HOST}/v1/batches/{batch_id}", key=key)


def download_file(key: str, file_id: str) -> str:
    raw = http_request("GET", f"{BATCH_HOST}/v1/files/{file_id}/content", key=key, raw=True)
    return raw.decode("utf-8")


# ── JSONL builders ──
def build_design_jsonl(seeds: list, model: str, max_tokens: int, temperature: float) -> list:
    """Each line = one DESIGN.md generation request."""
    lines = []
    for seed in seeds:
        prompt = build_design_md_prompt(seed)
        lines.append({
            "custom_id": f"design::{seed['id']}",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": model,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                "max_tokens": max_tokens,
                "temperature": temperature,
            }
        })
    return lines


def build_html_jsonl(seed_design_pairs: list, model: str, max_tokens: int, temperature: float) -> list:
    """Each line = one reference.html generation request, given a seed and its DESIGN.md."""
    lines = []
    for seed, design_md in seed_design_pairs:
        prompt = build_reference_html_prompt(seed, design_md)
        lines.append({
            "custom_id": f"html::{seed['id']}",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": model,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                "max_tokens": max_tokens,
                "temperature": temperature,
            }
        })
    return lines


def write_jsonl(lines: list, path: Path):
    JSONL_DIR.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for line in lines:
            f.write(json.dumps(line, ensure_ascii=False) + "\n")


# ── Output parser ──
def parse_batch_output(content: str) -> dict:
    """Parse batch output jsonl, return {custom_id: response_text}."""
    results = {}
    for line in content.strip().splitlines():
        if not line.strip():
            continue
        try:
            row = json.loads(line)
            cid = row["custom_id"]
            body = row.get("response", {}).get("body", {})
            choices = body.get("choices", [])
            if choices:
                results[cid] = choices[0]["message"]["content"]
            else:
                results[cid] = None
        except Exception as e:
            print(f"  parse error: {e}")
    return results


# ── Commands ──
def cmd_submit_design(args, config, state):
    """Submit phase A: DESIGN.md generation batch."""
    key = get_api_key(config)
    catalog = PROJECT_ROOT / "catalog" / "SEEDS.md"
    seeds = parse_seeds(catalog)
    styles_dir = PROJECT_ROOT / config["pipeline"]["output_dir"]

    # Filter pending seeds
    pending = [s for s in seeds if get_style_status(styles_dir, s["id"]) != "validated"]
    # Skip seeds already in an open batch
    in_flight = set()
    for b in state["batches"]:
        if b.get("phase") == "design" and b.get("status") not in ("completed", "failed", "expired", "consumed"):
            in_flight.update(b.get("seed_ids", []))
    pending = [s for s in pending if s["id"] not in in_flight]

    if args.limit and args.limit > 0:
        pending = pending[:args.limit]

    if not pending:
        print("No pending seeds to submit.")
        return

    print(f"Submitting {len(pending)} seeds for phase A (DESIGN.md)...")

    lines = build_design_jsonl(
        pending,
        config["llm"]["model"],
        config["llm"]["max_tokens"],
        config["llm"]["temperature"],
    )
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    jsonl_path = JSONL_DIR / f"design_{ts}.jsonl"
    write_jsonl(lines, jsonl_path)
    print(f"  wrote {len(lines)} lines to {jsonl_path}")

    file_id = upload_jsonl(key, jsonl_path)
    print(f"  uploaded → file_id={file_id}")

    batch = create_batch(key, file_id, f"design-{ts}")
    print(f"  created batch={batch['id']} status={batch['status']}")

    state["batches"].append({
        "phase": "design",
        "batch_id": batch["id"],
        "input_file_id": file_id,
        "jsonl_path": str(jsonl_path),
        "seed_ids": [s["id"] for s in pending],
        "status": batch["status"],
        "created_at": batch.get("created_at"),
        "submitted_at": datetime.now().isoformat(),
    })
    save_state(state)


def cmd_poll(args, config, state):
    """Poll all open batches."""
    key = get_api_key(config)
    open_batches = [b for b in state["batches"]
                    if b.get("status") not in ("completed", "failed", "expired", "consumed")]
    if not open_batches:
        print("No open batches.")
        return

    print(f"Polling {len(open_batches)} open batches...")
    for b in open_batches:
        try:
            info = get_batch(key, b["batch_id"])
            old_status = b["status"]
            b["status"] = info["status"]
            b["request_counts"] = info.get("request_counts", {})
            if info.get("output_file_id"):
                b["output_file_id"] = info["output_file_id"]
            if info.get("error_file_id"):
                b["error_file_id"] = info["error_file_id"]
            print(f"  [{b['phase']}] {b['batch_id'][:30]} {old_status}→{b['status']} {info.get('request_counts', {})}")
        except Exception as e:
            print(f"  ERR {b['batch_id']}: {e}")
    save_state(state)


def cmd_consume(args, config, state):
    """Process completed phase A batches → kick off phase B."""
    key = get_api_key(config)
    catalog = PROJECT_ROOT / "catalog" / "SEEDS.md"
    seeds = {s["id"]: s for s in parse_seeds(catalog)}
    styles_dir = PROJECT_ROOT / config["pipeline"]["output_dir"]

    consumed = 0
    for b in state["batches"]:
        if b.get("phase") != "design" or b.get("status") != "completed":
            continue
        if not b.get("output_file_id"):
            continue
        print(f"Consuming design batch {b['batch_id']}...")
        content = download_file(key, b["output_file_id"])
        results = parse_batch_output(content)
        print(f"  parsed {len(results)} responses")

        # Save raw DESIGN.md per seed and build phase B input
        seed_design_pairs = []
        for cid, text in results.items():
            if not text or not cid.startswith("design::"):
                continue
            seed_id = cid[len("design::"):]
            seed = seeds.get(seed_id)
            if not seed:
                continue
            design_md = extract_code_block(text)
            # Save to styles dir as scaffold
            sd = styles_dir / seed_id
            sd.mkdir(parents=True, exist_ok=True)
            (sd / "DESIGN.md").write_text(design_md)
            seed_design_pairs.append((seed, design_md))

        if not seed_design_pairs:
            print("  no usable designs; marking consumed")
            b["status"] = "consumed"
            consumed += 1
            continue

        # Submit phase B for these
        lines = build_html_jsonl(
            seed_design_pairs,
            config["llm"]["model"],
            config["llm"]["max_tokens"],
            config["llm"]["temperature"],
        )
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        jsonl_path = JSONL_DIR / f"html_{ts}.jsonl"
        write_jsonl(lines, jsonl_path)
        print(f"  wrote {len(lines)} html prompts to {jsonl_path}")
        file_id = upload_jsonl(key, jsonl_path)
        print(f"  uploaded → file_id={file_id}")
        new_batch = create_batch(key, file_id, f"html-{ts}")
        print(f"  created phase-B batch={new_batch['id']}")
        state["batches"].append({
            "phase": "html",
            "batch_id": new_batch["id"],
            "input_file_id": file_id,
            "jsonl_path": str(jsonl_path),
            "seed_ids": [s["id"] for s, _ in seed_design_pairs],
            "status": new_batch["status"],
            "parent_batch": b["batch_id"],
            "submitted_at": datetime.now().isoformat(),
        })
        b["status"] = "consumed"
        consumed += 1

    print(f"Consumed {consumed} design batches.")
    save_state(state)


def cmd_finalize(args, config, state):
    """Process completed phase B batches → score and save validated styles."""
    key = get_api_key(config)
    catalog = PROJECT_ROOT / "catalog" / "SEEDS.md"
    seeds = {s["id"]: s for s in parse_seeds(catalog)}
    styles_dir = PROJECT_ROOT / config["pipeline"]["output_dir"]
    target = config["scoring"]["eight_dim_max"]

    finalized = 0
    for b in state["batches"]:
        if b.get("phase") != "html" or b.get("status") != "completed":
            continue
        if not b.get("output_file_id"):
            continue
        print(f"Finalizing html batch {b['batch_id']}...")
        content = download_file(key, b["output_file_id"])
        results = parse_batch_output(content)

        passed = failed = 0
        for cid, text in results.items():
            if not text or not cid.startswith("html::"):
                continue
            seed_id = cid[len("html::"):]
            seed = seeds.get(seed_id)
            if not seed:
                continue
            html = extract_code_block(text)
            scores = score_html(html)
            sd = styles_dir / seed_id
            sd.mkdir(parents=True, exist_ok=True)
            (sd / "reference.html").write_text(html)
            status = "validated" if scores["total"] <= target else "failed"
            metadata = {
                "id": seed_id,
                "name": seed["name"],
                "status": status,
                "scores": scores,
                "iterations": 1,
                "via": "batch",
                "batch_id": b["batch_id"],
            }
            (sd / "metadata.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False))
            if status == "validated":
                passed += 1
            else:
                failed += 1

        print(f"  ✅ {passed} passed | ❌ {failed} failed")
        b["status"] = "consumed"
        b["passed"] = passed
        b["failed"] = failed
        finalized += 1

    print(f"Finalized {finalized} html batches.")
    save_state(state)


def cmd_status(args, config, state):
    """Show batch status."""
    if not state["batches"]:
        print("No batches submitted.")
        return
    print(f"{'Phase':<8} {'Batch ID':<35} {'Status':<12} {'Counts':<25} {'Submitted':<20}")
    print("-" * 110)
    for b in state["batches"]:
        cnts = b.get("request_counts", {})
        cnts_str = f"t={cnts.get('total', '?')} ok={cnts.get('completed', '?')} fail={cnts.get('failed', '?')}"
        print(f"{b.get('phase', '?'):<8} {b['batch_id']:<35} {b.get('status', '?'):<12} {cnts_str:<25} {b.get('submitted_at', '')[:19]}")


def cmd_audit(args, config, state):
    """Audit every output/*/reference.html for structural integrity and AI-taste drift.

    Read-only — never modifies HTML or metadata. Designed to be cheap enough to run
    on every poll cycle (5-minute cadence) so regressions surface immediately.

    Categories reported:
      - structural: missing <h1>, <style>, viewport meta, or </html> close
      - drift:      metadata.score_history disagrees with current 8-dim rescore
      - ai-trace:   8-dim dimensions flagging AI patterns (font_cliche, purple_gradient,
                    glassmorphism, uniform_radius, emoji_icons, placeholder_copy,
                    heavy_shadow, element_density)
      - size:       files suspiciously small (<1KB) or zero
    """
    import time as _time

    styles_dir = PROJECT_ROOT / config["pipeline"]["output_dir"]
    target = config["scoring"]["eight_dim_max"]

    if not styles_dir.exists():
        print(f"audit: styles dir not found: {styles_dir}")
        return

    t0 = _time.time()
    structural = []   # (style_id, [issue_codes])
    drift = []        # (style_id, stored_total, cur_total, cur_pass)
    ai_trace = []     # (style_id, dim_name, dim_score)
    size_problems = []

    audited = 0
    total = 0
    ai_trace_total = 0

    for sd in sorted(styles_dir.iterdir()):
        if not sd.is_dir():
            # Skip stray files like .DS_Store at the root of styles_dir
            continue
        h = sd / "reference.html"
        m = sd / "metadata.json"
        if not h.exists():
            continue
        total += 1
        audited += 1

        try:
            html = h.read_text(encoding="utf-8")
        except Exception as e:
            structural.append((sd.name, [f"read_error:{type(e).__name__}"]))
            continue

        # ── size checks ──
        size = len(html)
        if size < 1024:
            size_problems.append((sd.name, size, "<1KB"))

        # ── structural checks ──
        issues = []
        low = html.lower()
        if "<style" not in low:
            issues.append("no_<style>")
        if "<h1" not in low:
            issues.append("no_<h1>")
        if "viewport" not in low:
            issues.append("no_viewport")
        if "</html>" not in low:
            issues.append("no_</html>")
        if issues:
            structural.append((sd.name, issues))

        # ── 8-dim rescore + drift + ai-trace ──
        scores = score_html(html)
        cur_pass = scores["total"] <= target

        # AI-trace detail (every non-zero dim that signals AI patterns)
        for dim, val in scores.items():
            if dim == "total":
                continue
            if val > 0:
                ai_trace.append((sd.name, dim, val))
                ai_trace_total += 1

        # Drift: stored metadata disagrees with current scorer verdict
        if m.exists():
            try:
                meta = json.loads(m.read_text())
                stored_total = meta.get("scores", {}).get("total", -1)
                stored_status = meta.get("status", "?")
                # Only meaningful drift when both sides are present
                if stored_total >= 0:
                    if stored_status == "validated" and not cur_pass:
                        drift.append((sd.name, stored_total, scores["total"], "STORED_OK_NOW_FAIL"))
                    elif stored_status == "failed" and cur_pass:
                        drift.append((sd.name, stored_total, scores["total"], "STORED_FAIL_NOW_OK"))
            except Exception:
                pass

    elapsed = _time.time() - t0

    # ── Report ──
    print(f"\n=== reference.html audit ({audited} files, {elapsed:.2f}s) ===\n")

    print(f"[1] STRUCTURAL: {len(structural)} files have structural issues")
    if structural:
        for sid, issues in structural[:20]:
            print(f"  - {sid}: {', '.join(issues)}")
        if len(structural) > 20:
            print(f"  ... +{len(structural) - 20} more")
    print()

    print(f"[2] 8-DIM DRIFT: {len(drift)} files disagree with stored metadata")
    if drift:
        for sid, st, ct, kind in drift[:20]:
            print(f"  - {sid}: stored={st} cur={ct} ({kind})")
        if len(drift) > 20:
            print(f"  ... +{len(drift) - 20} more")
    print()

    print(f"[3] AI TRACE: {ai_trace_total} dim flags across {len(set(x[0] for x in ai_trace))} files")
    # top 10 most-flagged dims
    from collections import Counter
    dim_counts = Counter(d for _, d, _ in ai_trace)
    for dim, cnt in dim_counts.most_common():
        print(f"  - {dim}: {cnt} hits")
    print()

    print(f"[4] SIZE: {len(size_problems)} files anomalously small")
    if size_problems:
        for sid, sz, label in size_problems[:10]:
            print(f"  - {sid}: {sz}B ({label})")
    print()

    # Final summary line — easy to grep from cron logs
    total_problems = len(structural) + len(drift) + len(size_problems)
    print(f"AUDIT_SUMMARY audited={audited} structural={len(structural)} drift={len(drift)} "
          f"ai_trace_files={len(set(x[0] for x in ai_trace))} size_anomalies={len(size_problems)} "
          f"total_problems={total_problems}")
    print(f"audit_elapsed_s={elapsed:.2f}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--submit-design", action="store_true", help="Submit phase A batch (DESIGN.md)")
    parser.add_argument("--poll", action="store_true", help="Poll all open batches")
    parser.add_argument("--consume", action="store_true", help="Consume completed design batches → submit html")
    parser.add_argument("--finalize", action="store_true", help="Finalize completed html batches → score+save")
    parser.add_argument("--status", action="store_true", help="Show batch state")
    parser.add_argument("--audit", action="store_true", help="Audit all output/*/reference.html (read-only)")
    parser.add_argument("--limit", type=int, default=0, help="Limit seeds when submitting")
    args = parser.parse_args()

    config = load_config()
    state = load_state()

    if args.submit_design:
        cmd_submit_design(args, config, state)
    elif args.poll:
        cmd_poll(args, config, state)
    elif args.consume:
        cmd_consume(args, config, state)
    elif args.finalize:
        cmd_finalize(args, config, state)
    elif args.status:
        cmd_status(args, config, state)
    elif args.audit:
        cmd_audit(args, config, state)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
