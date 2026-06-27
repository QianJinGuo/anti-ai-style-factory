#!/usr/bin/env python3
"""
Gallery Index Builder
=====================
Scans styles/*/metadata.json + styles/*/DESIGN.md to produce gallery/data/styles.json.

Usage:
    python scripts/build_gallery.py [--output gallery/data/styles.json] [--force]

The output JSON contains:
  - styles[]: per-style index records (id, name, movement, medium, palette, scores, colors)
  - filterOptions: deduplicated movements, mediums, palettes
  - stats: summary counts

Zero dependencies beyond stdlib (json, re, pathlib).
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

# Must match seed_generator.py
PALETTES = {"warm", "cool", "earth", "neon", "monochrome", "pastel", "jewel", "muted"}
TEXTURES = {
    "grain",
    "paper",
    "canvas",
    "stone",
    "metal",
    "wood",
    "fabric",
    "concrete",
    "wax",
    "glass",
}
MEDIUMS = {
    "poster",
    "book-cover",
    "dashboard",
    "landing",
    "editorial-spread",
    "packaging",
    "signage",
    "exhibition",
    "infographic",
    "card-ui",
    "typography-specimen",
    "wayfinding",
    "album-art",
    "stamp",
    "banknote",
    "map",
    "recipe",
    "ticket",
    "catalog",
    "annual-report",
}

# Movement roots — the first segment of any valid style id.
# Computed from catalog at build time; fallback to known list.
KNOWN_MOVEMENTS = {
    "african-wax",
    "arabic-geo",
    "art-brut",
    "art-deco",
    "art-nouveau",
    "bauhaus",
    "biomorphic",
    "blackletter",
    "baroque",
    "brutalist-arch",
    "brutalist-web",
    "chinese-stone",
    "comic-book",
    "constructivist",
    "cyberpunk",
    "dada",
    "data-ink",
    "de-stijl",
    "dutch-golden",
    "editorial",
    "film-noir",
    "gothic-cath",
    "graffiti",
    "grunge",
    "ink-wash",
    "japanese-minimal",
    "letterpress",
    "memphis",
    "mexican-mural",
    "mid-century",
    "neon-sign",
    "newspaper",
    "op-art",
    "persian-mini",
    "pixel-art",
    "polaroid",
    "pop-art",
    "retrowave",
    "russian-avant",
    "scandinavian",
    "skeuomorphic",
    "space-age",
    "streamline",
    "swiss-intl",
    "technicolor",
    "terminal",
    "terrazzo",
    "ukiyo-e",
    "ukiyoe",
    "vaporwave",
    "vernacular",
    "wabi-sabi",
    "wiener-wk",
    "y2k",
    "zine-punk",
}

# Multi-segment movements (hyphenated but still a single movement)
MULTI_SEG_MOVEMENTS = {
    "brutalist-web",
    "brutalist-arch",
    "swiss-intl",
    "african-wax",
    "art-deco",
    "art-nouveau",
    "art-brut",
    "chinese-stone",
    "comic-book",
    "ink-wash",
    "mid-century",
    "op-art",
    "neon-sign",
    "pop-art",
    "pixel-art",
    "space-age",
    "de-stijl",
    "dutch-golden",
    "russian-avant",
    "wiener-wk",
    "wabi-sabi",
    "data-ink",
    "film-noir",
    "cyberpunk",
}


def parse_style_id(sid: str) -> dict:
    """Parse a style id into movement, medium, palette, texture components.

    Examples:
        bauhaus → {movement: bauhaus}
        bauhaus-poster-cool → {movement: bauhaus, medium: poster, palette: cool}
        brutalist-web → {movement: brutalist-web}
        african-wax-cool → {movement: african-wax, palette: cool}
    """
    parts = sid.split("-")
    result = {"movement": "", "medium": "", "palette": "", "texture": ""}

    if not parts:
        return result

    # Try multi-segment movement first (longest match)
    for length in range(min(len(parts), 3), 0, -1):
        candidate = "-".join(parts[:length])
        if candidate in KNOWN_MOVEMENTS:
            result["movement"] = candidate
            remaining = parts[length:]
            break
    else:
        result["movement"] = parts[0]
        remaining = parts[1:]

    # Parse remaining segments
    for seg in remaining:
        if seg in MEDIUMS:
            result["medium"] = seg
        elif seg in PALETTES:
            result["palette"] = seg
        elif seg in TEXTURES:
            result["texture"] = seg

    return result


def extract_colors_from_design(design_md: str) -> dict:
    """Extract color tokens from DESIGN.md YAML frontmatter."""
    colors = {}
    in_frontmatter = False
    frontmatter_lines = []

    for line in design_md.split("\n"):
        if line.strip() == "---":
            if in_frontmatter:
                break
            in_frontmatter = True
            continue
        if in_frontmatter:
            frontmatter_lines.append(line)

    if not frontmatter_lines:
        return colors

    in_colors = False
    for line in frontmatter_lines:
        stripped = line.strip()
        if stripped.startswith("colors"):
            in_colors = True
            continue
        if in_colors and stripped and not stripped.startswith(" "):
            in_colors = False
            continue
        if in_colors:
            match = re.match(r'(\w+)\s*:\s*"?([^"]+)"?', stripped)
            if match:
                key, val = match.group(1), match.group(2).strip()
                # Clean up inline comments
                val = re.sub(r"\s+#.*$", "", val).strip()
                if val.startswith("#") or val.startswith("rgb"):
                    colors[key] = val

    return colors


def build_index(styles_dir: Path) -> dict:
    """Scan all style directories and build the index."""
    styles = []
    movements = Counter()
    mediums = Counter()
    palettes = Counter()
    score_totals = Counter()

    style_dirs = sorted(d for d in styles_dir.iterdir() if d.is_dir())
    total = len(style_dirs)
    errors = []

    for i, style_dir in enumerate(style_dirs, 1):
        meta_path = style_dir / "metadata.json"
        design_path = style_dir / "DESIGN.md"

        if not meta_path.exists():
            continue

        # Progress indicator
        if i % 1000 == 0:
            print(f"  [{i}/{total}] ...", file=sys.stderr)

        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            errors.append(f"{style_dir.name}: {e}")
            continue

        sid = meta.get("id", style_dir.name)
        parsed = parse_style_id(sid)

        # Extract colors from DESIGN.md if available
        colors = {}
        if design_path.exists():
            try:
                design_md = design_path.read_text(encoding="utf-8")
                colors = extract_colors_from_design(design_md)
            except OSError:
                pass

        record = {
            "id": sid,
            "name": meta.get("name", sid),
            "movement": parsed["movement"],
            "medium": parsed["medium"],
            "palette": parsed["palette"],
            "texture": parsed["texture"],
            "status": meta.get("status", ""),
            "total": meta.get("scores", {}).get("total", -1),
            "scores": meta.get("scores", {}),
            "colors": colors,
        }

        styles.append(record)
        movements[parsed["movement"]] += 1
        if parsed["medium"]:
            mediums[parsed["medium"]] += 1
        if parsed["palette"]:
            palettes[parsed["palette"]] += 1
        total_score = record["total"]
        if total_score >= 0:
            score_totals[total_score] += 1

    return {
        "styles": styles,
        "filterOptions": {
            "movements": sorted(movements.keys()),
            "mediums": sorted(mediums.keys()),
            "palettes": sorted(palettes.keys()),
            "movementCounts": dict(sorted(movements.items())),
            "mediumCounts": dict(sorted(mediums.items())),
            "paletteCounts": dict(sorted(palettes.items())),
        },
        "stats": {
            "total": len(styles),
            "movements": len(movements),
            "mediums": len(mediums),
            "palettes": len(palettes),
            "validated": sum(1 for s in styles if s["status"] == "validated"),
            "scoreDistribution": dict(sorted(score_totals.items())),
        },
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build gallery index from styles directory.")
    parser.add_argument(
        "--output",
        "-o",
        default=str(Path(__file__).parent.parent / "gallery" / "data" / "styles.json"),
        help="Output JSON path (default: gallery/data/styles.json)",
    )
    parser.add_argument(
        "--styles-dir",
        default=str(Path(__file__).parent.parent / "styles"),
        help="Root styles directory (default: styles/)",
    )
    parser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="Rebuild even if output exists",
    )
    args = parser.parse_args(argv)

    output_path = Path(args.output)
    styles_dir = Path(args.styles_dir)

    if output_path.exists() and not args.force:
        print(f"Output exists: {output_path}")
        print("Use --force to rebuild.")
        return 0

    if not styles_dir.is_dir():
        print(f"Error: styles directory not found: {styles_dir}", file=sys.stderr)
        return 1

    print(f"Scanning {styles_dir} ...", file=sys.stderr)
    data = build_index(styles_dir)
    print(
        f"Found {data['stats']['total']} styles "
        f"({data['stats']['movements']} movements, "
        f"{data['stats']['mediums']} mediums, "
        f"{data['stats']['palettes']} palettes)",
        file=sys.stderr,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    # Print size
    size_kb = output_path.stat().st_size / 1024
    print(f"Wrote {output_path} ({size_kb:.0f} KB)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
