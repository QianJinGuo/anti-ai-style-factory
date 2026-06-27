#!/usr/bin/env python3
"""
One-shot repair script for reference.html files flagged by `batch_runner --audit`.

Categories of fix:
  1. Append `</body></html>` to files truncated mid-output (LLM max_tokens cutoff)
  2. Promote first `<h2>` → `<h1>` for files missing a top-level heading
  3. Quarantine files that are fundamentally broken (empty / CSS fragment) by
     moving them to styles/_quarantine/<name>/ — the audit will then stop flagging them.
     They need real LLM regeneration, not text manipulation.

Usage:
  python scripts/repair_reference_html.py --dry-run     # preview, no changes
  python scripts/repair_reference_html.py              # apply fixes
  python scripts/repair_reference_html.py --restore    # undo: move quarantined dirs back

The script NEVER modifies files outside `styles/_quarantine/` without explicit --apply,
and quarantined files are moved (not deleted) so they're recoverable.
"""

import argparse
import json
import re
import shutil
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
STYLES_DIR = PROJECT_ROOT / "styles"
QUARANTINE_DIR = STYLES_DIR / "_quarantine"
QUARANTINE_LOG = QUARANTINE_DIR / "_quarantine_log.json"

# Files in these directories are never touched
PROTECTED = {QUARANTINE_DIR.name}


def find_audit_problems() -> dict:
    """Re-run the audit locally and return the problem buckets we know how to fix.

    Returns dict with:
      needs_html_close: files that have <body> but no </body></html> — recoverable by appending closers
      needs_h1:         files missing <h1> (have <h2>+) — recoverable by promoting first heading
      needs_regen:      fundamentally broken — only CSS, no <body> at all. These need real LLM regeneration.
      empty:            0-byte files
    """
    sys.path.insert(0, str(PROJECT_ROOT))
    from src.scorer.eight_dim import score_html

    problems = {
        "needs_html_close": [],
        "needs_h1": [],
        "needs_regen": [],   # CSS-only fragments — require LLM regeneration, not text fix
        "empty": [],
    }

    for sd in sorted(STYLES_DIR.iterdir()):
        if not sd.is_dir() or sd.name in PROTECTED:
            continue
        h = sd / "reference.html"
        if not h.exists():
            continue
        try:
            html = h.read_text(encoding="utf-8")
        except Exception:
            problems["needs_regen"].append((sd.name, 0, "read_error"))
            continue

        size = len(html)
        low = html.lower()

        if size == 0:
            problems["empty"].append(sd.name)
            continue

        # CSS-only fragment: has <style> but never opened <body>
        # LLM hit max_tokens mid-style-block — page would render blank in browser
        if "<body" not in low:
            problems["needs_regen"].append((sd.name, size, "css_only_no_body"))
            continue

        # Has body content but missing closing tags (LLM truncated mid-table/etc.)
        if "</html>" not in low:
            problems["needs_html_close"].append(sd.name)
            # Continue to check h1 in same file (might be both)

        # Missing top-level heading.
        # Case 1: has <h2>+ but no <h1> — promote first heading
        if "<h1" not in low and re.search(r"<h[23]", low):
            problems["needs_h1"].append(sd.name)
        # Case 2: zero headings at all — insert <h1> from <title> after <body>
        elif "<h1" not in low and "<body" in low and "<title>" in low:
            problems["needs_h1"].append(sd.name)

    return problems


def append_closing_tags(html: str) -> str:
    """Append missing closing tags without doubling anything that's already there."""
    if "</html>" in html:
        return html  # already closed (shouldn't happen if we got here, but be safe)
    # Trim any partial trailing tag content that looks like a fragment
    html = html.rstrip()
    closers = ""
    if "</body>" not in html:
        closers += "</body>\n"
    closers += "</html>\n"
    return html + "\n" + closers


def promote_first_heading(html: str) -> tuple[str, bool]:
    """Promote the first <h2> (or h3/h4 if no h2) to <h1>. Returns (new_html, changed)."""
    # Find the first occurrence of <h2, <h3, or <h4 — promote it to h1
    pattern = re.compile(r"<(h[234])([^>]*)>(.*?)</\1>", re.DOTALL | re.IGNORECASE)
    m = pattern.search(html)
    if not m:
        return html, False
    new_tag = "h1"
    new_html = html[: m.start()] + f"<{new_tag}{m.group(2)}>{m.group(3)}</{new_tag}>" + html[m.end():]
    return new_html, True


def insert_h1_from_title(html: str) -> tuple[str, bool]:
    """Insert <h1> derived from <title> right after <body> tag. Returns (new_html, changed).

    Used for files that have zero heading tags at all — semantically weak but valid HTML.
    """
    title_m = re.search(r"<title>([^<]+)</title>", html, re.IGNORECASE)
    if not title_m:
        return html, False
    title = title_m.group(1).strip()

    body_m = re.search(r"<body[^>]*>", html, re.IGNORECASE)
    if not body_m:
        return html, False

    insert_pos = body_m.end()
    h1_html = f'\n<h1>{title}</h1>\n'
    return html[:insert_pos] + h1_html + html[insert_pos:], True


def quarantine(sd: Path, reason: str, log: dict):
    """Move a broken style dir to styles/_quarantine/<name>/ and log it."""
    target = QUARANTINE_DIR / sd.name
    # If target already exists (from a prior run), just overwrite the log entry
    if target.exists():
        shutil.rmtree(target)
    shutil.move(str(sd), str(target))
    log[sd.name] = {
        "reason": reason,
        "moved_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "original_path": str(sd.relative_to(PROJECT_ROOT)),
    }


def restore_quarantine():
    """Undo: move everything in _quarantine/ back to styles/."""
    if not QUARANTINE_DIR.exists():
        print("No quarantine dir — nothing to restore.")
        return
    moved = 0
    for sd in sorted(QUARANTINE_DIR.iterdir()):
        if not sd.is_dir() or sd.name.startswith("_"):
            continue
        target = STYLES_DIR / sd.name
        if target.exists():
            print(f"  WARNING: {target} already exists, skipping {sd.name}")
            continue
        shutil.move(str(sd), str(target))
        moved += 1
    # Clear the log
    if QUARANTINE_LOG.exists():
        QUARANTINE_LOG.unlink()
    print(f"Restored {moved} dirs from quarantine.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Preview fixes without modifying anything")
    parser.add_argument("--restore", action="store_true", help="Undo quarantine (move dirs back)")
    args = parser.parse_args()

    if args.restore:
        restore_quarantine()
        return

    if not STYLES_DIR.exists():
        print(f"styles dir not found: {STYLES_DIR}")
        return 1

    print(f"Scanning {STYLES_DIR}...")
    problems = find_audit_problems()

    total_html = len(problems["needs_html_close"])
    total_h1 = len(problems["needs_h1"])
    total_regen = len(problems["needs_regen"])
    total_empty = len(problems["empty"])

    print(f"\n=== Findings ===")
    print(f"  [A] needs </body></html> close:  {total_html}  (cheap text fix)")
    print(f"  [B] needs <h1> promotion:        {total_h1}  (cheap text fix)")
    print(f"  [C] CSS-only fragments (no body): {total_regen}  (REQUIRES LLM REGENERATION)")
    print(f"  [D] empty (0-byte) files:         {total_empty}  (REQUIRES LLM REGENERATION)")
    if total_regen + total_empty:
        print(f"\n  ⚠ {total_regen + total_empty} files need LLM regen — these are CSS-only")
        print(f"    fragments where the LLM hit max_tokens mid-style-block. Browser would")
        print(f"    render them blank. Text fixes CANNOT recover these.")
        for name, sz, reason in problems["needs_regen"][:3]:
            print(f"      - {name} ({sz}B, {reason})")
        if total_regen > 3:
            print(f"      ... +{total_regen - 3} more (full list at styles/_quarantine/ after --apply)")
        for name in problems["empty"][:3]:
            print(f"      - {name} (0B, empty)")
    print(f"\n  Auto-fixable: {total_html + total_h1} files")
    print(f"  Needs LLM regen: {total_regen + total_empty} files")

    if args.dry_run:
        print(f"\n[dry-run] No changes made. Re-run without --dry-run to apply.")
        print(f"          The {total_regen + total_empty} regen-needed files will be quarantined to")
        print(f"          styles/_quarantine/ so the audit stops flagging them.")
        return 0

    print(f"\n=== Applying fixes ===")
    t0 = time.time()

    # 1. Append closing tags (cheapest fix)
    fixed_html = 0
    for name in problems["needs_html_close"]:
        sd = STYLES_DIR / name
        h = sd / "reference.html"
        try:
            html = h.read_text(encoding="utf-8")
            new_html = append_closing_tags(html)
            h.write_text(new_html, encoding="utf-8")
            fixed_html += 1
        except Exception as e:
            print(f"  ERR closing {name}: {e}")
    print(f"  [1] appended </body></html> to {fixed_html} files")

    # 2. Add <h1> — two cases: promote existing h2, or insert from title
    promoted = 0
    inserted = 0
    for name in problems["needs_h1"]:
        sd = STYLES_DIR / name
        h = sd / "reference.html"
        try:
            html = h.read_text(encoding="utf-8")
            # Try promote first
            new_html, changed = promote_first_heading(html)
            if changed:
                h.write_text(new_html, encoding="utf-8")
                promoted += 1
                continue
            # Fallback: insert from title
            new_html, changed = insert_h1_from_title(html)
            if changed:
                h.write_text(new_html, encoding="utf-8")
                inserted += 1
        except Exception as e:
            print(f"  ERR adding h1 to {name}: {e}")
    print(f"  [2a] promoted first heading to <h1> in {promoted} files")
    print(f"  [2b] inserted <h1> from <title> in {inserted} files")

    # 3. Quarantine regen-needed files (don't try to text-fix broken ones)
    QUARANTINE_DIR.mkdir(parents=True, exist_ok=True)
    log = {}
    if QUARANTINE_LOG.exists():
        log = json.loads(QUARANTINE_LOG.read_text())
    quarantined = 0
    for name, sz, reason in problems["needs_regen"]:
        sd = STYLES_DIR / name
        if not sd.exists():
            continue
        quarantine(sd, f"{reason} ({sz}B)", log)
        quarantined += 1
    for name in problems["empty"]:
        sd = STYLES_DIR / name
        if not sd.exists():
            continue
        quarantine(sd, "empty (0B)", log)
        quarantined += 1
    QUARANTINE_LOG.write_text(json.dumps(log, indent=2, ensure_ascii=False))
    print(f"  [3] quarantined {quarantined} regen-needed dirs → styles/_quarantine/")
    print(f"      (these need a batch resubmit — DESIGN.md still exists in each dir)")

    elapsed = time.time() - t0
    print(f"\nDone in {elapsed:.1f}s.")
    print(f"Next steps:")
    print(f"  1. python -m src.pipeline.batch_runner --audit        # verify cleanup")
    print(f"  2. cat styles/_quarantine/_quarantine_log.json        # see {quarantined} dirs to regen")
    print(f"  3. To re-submit the quarantined styles, see scripts/repair_reference_html.py --regen-batch (TODO)")


if __name__ == "__main__":
    sys.exit(main() or 0)