#!/usr/bin/env python3
"""
Anti-AI Style Factory — Pipeline Runner
========================================
Main entry point. Reads seeds from catalog, generates styles via LLM,
scores with 8-dim rubric, iterates until passing, saves output.

Usage:
  python3 -m src.pipeline.run                    # Generate all pending seeds
  python3 -m src.pipeline.run --seed bauhaus-1919  # Generate one seed
  python3 -m src.pipeline.run --tier 1            # Generate all Tier 1 seeds
  python3 -m src.pipeline.run --dry-run           # Show what would be generated
  python3 -m src.pipeline.run --status            # Show generation status
"""

import argparse
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import yaml

# Ensure project root is on path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.scorer.eight_dim import score_html, DIMENSIONS
from src.generator.llm_generator import generate_style, save_result, get_client


def parse_seeds(catalog_path: Path) -> list:
    """Parse seed definitions from catalog/SEEDS.md."""
    if not catalog_path.exists():
        return []
    text = catalog_path.read_text()
    seeds = []
    for match in re.finditer(
        r"\|\s*`(\S+)`\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|",
        text,
    ):
        seed_id = match.group(1).strip()
        if seed_id.startswith("--") or seed_id.upper().startswith("ID"):
            continue
        seeds.append({
            "id": seed_id,
            "name": match.group(2).strip(),
            "era": match.group(3).strip(),
            "region": match.group(4).strip(),
            "principle": match.group(5).strip(),
            "anti_ai_signal": match.group(6).strip(),
        })
    return seeds


def seed_tier(seed_id: str) -> int:
    """Determine tier from catalog ordering."""
    tier_map = {
        "bauhaus-1919": 1, "swiss-1950": 1, "brutalist-web": 1,
        "art-deco-1925": 1, "de-stijl-1917": 1,
        "ukiyo-e-1831": 2, "memphis-1981": 2, "constructivist": 2,
        "terminal-green": 2, "editorial-1960": 2,
        "japanese-minimal": 3, "cyberpunk-neon": 3, "vernacular-sign": 3,
        "data-ink-tufte": 3, "dutch-golden": 3,
        "letterpress": 4, "zine-punk": 4, "chinese-stone": 4,
        "arabic-geometric": 4, "african-wax": 4,
    }
    return tier_map.get(seed_id, 4)


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
        tier = seed_tier(s["id"])
        icon = {"validated": "✅", "scaffold": "🔧", "failed": "❌", "pending": "⬜"}.get(status, "❓")
        print(f"  {icon} T{tier} {s['id']:25s} {s['name']:20s} [{status}]")
        if status == "validated":
            validated += 1
        elif status in ("scaffold", "failed"):
            scaffolded += 1
        else:
            pending += 1
    print(f"\n  Total: {len(seeds)} | ✅ {validated} validated | 🔧 {scaffolded} attempted | ⬜ {pending} pending")


def cmd_run(config: dict, seeds: list, args):
    """Run the generation pipeline."""
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
        target_seeds = [s for s in seeds if seed_tier(s["id"]) == args.tier]

    # Skip already validated
    if not args.force:
        pending = [s for s in target_seeds if get_style_status(styles_dir, s["id"]) != "validated"]
    else:
        pending = target_seeds

    if not pending:
        print("All target seeds already validated. Use --force to regenerate.")
        return

    print(f"Pipeline: {len(pending)} seeds to generate ({len(target_seeds) - len(pending)} already done)")
    if args.dry_run:
        for s in pending:
            print(f"  Would generate: {s['id']} ({s['name']})")
        return

    # Create LLM client
    client = get_client(config)

    # Run pipeline
    run_log = {
        "started": datetime.now().isoformat(),
        "config": config,
        "results": [],
    }

    passed = failed = 0
    for i, seed in enumerate(pending, 1):
        print(f"\n{'='*60}")
        print(f"[{i}/{len(pending)}] {seed['id']} — {seed['name']}")
        print(f"{'='*60}")

        start = time.time()
        result = generate_style(client, config, seed)
        elapsed = time.time() - start

        result["elapsed_seconds"] = round(elapsed, 1)
        run_log["results"].append(result)

        if result["status"] == "validated":
            style_dir = save_result(result, styles_dir)
            # Also copy catalog SEEDS.md to styles dir
            print(f"  Saved to: {style_dir}")
            passed += 1
        else:
            # Save failed result too (for debugging)
            save_result(result, styles_dir)
            failed += 1

        print(f"  Time: {elapsed:.1f}s | Status: {result['status']}")

    # Save run log
    run_log["completed"] = datetime.now().isoformat()
    run_log["summary"] = {"passed": passed, "failed": failed, "total": len(pending)}
    log_path = log_dir / f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    log_path.write_text(json.dumps(run_log, indent=2, ensure_ascii=False))

    print(f"\n{'='*60}")
    print(f"Pipeline complete: ✅ {passed} passed | ❌ {failed} failed | Log: {log_path}")


def load_config() -> dict:
    """Load pipeline config."""
    config_path = PROJECT_ROOT / "config" / "pipeline.yaml"
    if config_path.exists():
        return yaml.safe_load(config_path.read_text())
    return {
        "llm": {
            "base_url": "https://api.tinyfish.cn/v1",
            "model": "gpt-4o",
            "api_key_env": "TINYFISH_API_KEY",
            "max_tokens": 4096,
            "temperature": 0.7,
        },
        "scoring": {"eight_dim_max": 4, "max_iterations": 3},
        "pipeline": {"output_dir": "./styles", "log_dir": "./logs"},
    }


def main():
    parser = argparse.ArgumentParser(description="Anti-AI Style Factory Pipeline")
    parser.add_argument("--seed", help="Generate a specific seed")
    parser.add_argument("--tier", type=int, help="Generate all seeds in a tier (1-4)")
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
