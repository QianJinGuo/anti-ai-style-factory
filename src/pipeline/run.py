#!/usr/bin/env python3
"""
Anti-AI Style Factory — Pipeline Runner
========================================
Main entry point. Reads seeds from catalog, generates styles via LLM,
scores with 8-dim rubric, iterates until passing, saves output.

Supports concurrent generation with --workers (XFYUN: 100路/300 QPS).

Usage:
  python3 -m src.pipeline.run                    # Generate all pending seeds
  python3 -m src.pipeline.run --seed bauhaus-1919  # Generate one seed
  python3 -m src.pipeline.run --tier 1            # Generate all Tier 1 seeds
  python3 -m src.pipeline.run --batch 5           # Generate next 5 pending seeds
  python3 -m src.pipeline.run --workers 5         # 5 concurrent workers
  python3 -m src.pipeline.run --dry-run           # Show what would be generated
  python3 -m src.pipeline.run --status            # Show generation status
"""

import argparse
import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

import yaml

# Ensure project root is on path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.generator.llm_generator import generate_style, save_result, get_client


def parse_seeds(catalog_path: Path) -> list:
    """Parse seed definitions from catalog/SEEDS.md.
    Tier is inferred from the markdown heading above each table.
    """
    if not catalog_path.exists():
        return []
    text = catalog_path.read_text()
    seeds = []
    current_tier = 1

    for line in text.splitlines():
        m = re.match(r"^##\s+Tier\s+(\d+)", line)
        if m:
            current_tier = int(m.group(1))
            continue
        m = re.match(
            r"\|\s*`(\S+)`\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|",
            line,
        )
        if m:
            seed_id = m.group(1).strip()
            if seed_id.startswith("--") or seed_id.upper().startswith("ID"):
                continue
            seeds.append(
                {
                    "id": seed_id,
                    "name": m.group(2).strip(),
                    "era": m.group(3).strip(),
                    "region": m.group(4).strip(),
                    "principle": m.group(5).strip(),
                    "anti_ai_signal": m.group(6).strip(),
                    "tier": current_tier,
                }
            )
    return seeds


def get_style_status(styles_dir: Path, seed_id: str) -> str:
    """Check if a style has already been generated and validated."""
    meta_path = styles_dir / seed_id / "metadata.json"
    if not meta_path.exists():
        return "pending"
    meta = json.loads(meta_path.read_text())
    return meta.get("status", "pending")


def cmd_status(config: dict, seeds: list):
    """Show generation status."""
    styles_dir = PROJECT_ROOT / config["pipeline"]["output_dir"]
    validated = scaffolded = pending = 0
    for s in seeds:
        status = get_style_status(styles_dir, s["id"])
        tier = s.get("tier", "?")
        icon = {
            "validated": "✅",
            "scaffold": "🔧",
            "failed": "❌",
            "pending": "⬜",
        }.get(status, "❓")
        print(f"  {icon} T{tier} {s['id']:25s} {s['name']:20s} [{status}]")
        if status == "validated":
            validated += 1
        elif status in ("scaffold", "failed"):
            scaffolded += 1
        else:
            pending += 1
    print(f"\n  Total: {len(seeds)} | ✅ {validated} validated | 🔧 {scaffolded} attempted | ⬜ {pending} pending")


def _generate_one(client, config, seed, styles_dir, index, total):
    """Generate a single style, for use in thread pool."""
    print(f"\n{'=' * 60}")
    print(f"[{index}/{total}] {seed['id']} — {seed['name']} (worker starting)")
    print(f"{'=' * 60}")

    start = time.time()
    result = generate_style(client, config, seed)
    elapsed = time.time() - start
    result["elapsed_seconds"] = round(elapsed, 1)

    if result["status"] == "validated":
        style_dir = save_result(result, styles_dir)
        print(f"  ✅ [{seed['id']}] PASSED {result['scores']['total']}/16 — saved to {style_dir}")
    else:
        save_result(result, styles_dir)
        print(f"  ❌ [{seed['id']}] FAILED after {result['iterations']} attempts")

    print(f"  ⏱  {elapsed:.1f}s")
    return result


def cmd_run(config: dict, seeds: list, args):
    """Run the generation pipeline (concurrent)."""
    styles_dir = PROJECT_ROOT / config["pipeline"]["output_dir"]
    log_dir = PROJECT_ROOT / config["pipeline"]["log_dir"]
    styles_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)

    # Filter seeds
    target_seeds = seeds
    if args.seed:
        target_seeds = [s for s in seeds if s["id"] == args.seed]
        if not target_seeds:
            print(f"ERROR: seed '{args.seed}' not found. Available: {', '.join(s['id'] for s in seeds)}")
            return
    elif args.tier:
        target_seeds = [s for s in seeds if s.get("tier") == args.tier]

    # Skip already validated
    if not args.force:
        pending = [s for s in target_seeds if get_style_status(styles_dir, s["id"]) != "validated"]
    else:
        pending = target_seeds

    if not pending:
        print("All target seeds already validated. Use --force to regenerate.")
        return

    # Batch limit
    if args.batch and args.batch > 0:
        pending = pending[: args.batch]

    workers = args.workers or 1
    total = len(pending)

    print(f"Pipeline: {total} seeds to generate | {workers} worker(s)")
    if args.dry_run:
        for s in pending:
            print(f"  Would generate: {s['id']} ({s['name']})")
        return

    # Create LLM client (thread-safe: OpenAI client uses connection pool)
    client = get_client(config)

    # Run pipeline
    run_log = {
        "started": datetime.now().isoformat(),
        "config": {k: v for k, v in config.items() if k != "llm"},
        "results": [],
    }

    passed = failed = 0

    if workers <= 1:
        # Sequential mode
        for i, seed in enumerate(pending, 1):
            result = _generate_one(client, config, seed, styles_dir, i, total)
            run_log["results"].append(result)
            if result["status"] == "validated":
                passed += 1
            else:
                failed += 1
    else:
        # Concurrent mode — each worker gets its own OpenAI client
        # (connection pooling works better per-thread)
        print(f"Launching {workers} concurrent workers...")

        def _thread_job(seed_info):
            idx, seed = seed_info
            thread_client = get_client(config)
            result = _generate_one(thread_client, config, seed, styles_dir, idx, total)
            return result

        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(_thread_job, (i, s)): s for i, s in enumerate(pending, 1)}
            for future in as_completed(futures):
                seed = futures[future]
                try:
                    result = future.result()
                    run_log["results"].append(result)
                    if result["status"] == "validated":
                        passed += 1
                    else:
                        failed += 1
                except Exception as e:
                    print(f"  💥 [{seed['id']}] Worker crashed: {e}")
                    run_log["results"].append(
                        {
                            "seed_id": seed["id"],
                            "status": "crashed",
                            "error": str(e),
                        }
                    )
                    failed += 1

    # Save run log
    run_log["completed"] = datetime.now().isoformat()
    run_log["summary"] = {
        "passed": passed,
        "failed": failed,
        "total": total,
        "workers": workers,
    }
    log_path = log_dir / f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    log_path.write_text(json.dumps(run_log, indent=2, ensure_ascii=False))

    print(f"\n{'=' * 60}")
    print(f"Pipeline complete: ✅ {passed} passed | ❌ {failed} failed | Workers: {workers} | Log: {log_path}")


def load_config() -> dict:
    """Load pipeline config."""
    config_path = PROJECT_ROOT / "config" / "pipeline.yaml"
    if config_path.exists():
        return yaml.safe_load(config_path.read_text())
    return {
        "llm": {
            "provider": "openai",
            "model": "gpt-4o",
            "max_tokens": 4096,
            "temperature": 0.7,
            "providers": {
                "openai": {
                    "base_url": "https://api.openai.com/v1",
                    "api_key_env": "OPENAI_API_KEY",
                }
            },
        },
        "scoring": {"eight_dim_max": 4, "max_iterations": 3},
        "pipeline": {"output_dir": "./styles", "log_dir": "./logs"},
    }


def main():
    parser = argparse.ArgumentParser(description="Anti-AI Style Factory Pipeline")
    parser.add_argument("--seed", help="Generate a specific seed")
    parser.add_argument("--tier", type=int, help="Generate all seeds in a tier (1-6)")
    parser.add_argument("--batch", type=int, default=0, help="Generate next N pending seeds")
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Concurrent workers (XFYUN: up to 10 recommended)",
    )
    parser.add_argument("--force", action="store_true", help="Regenerate even if already validated")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be generated")
    parser.add_argument("--status", action="store_true", help="Show generation status")
    args = parser.parse_args()

    config = load_config()
    catalog_path = PROJECT_ROOT / "catalog" / "SEEDS.md"
    seeds = parse_seeds(catalog_path)

    if not seeds:
        print("No seeds found. Check catalog/SEEDS.md")
        sys.exit(1)

    if args.status:
        cmd_status(config, seeds)
    else:
        cmd_run(config, seeds, args)


if __name__ == "__main__":
    main()
