"""
Anti-AI Style Factory — 8-Dimension Scorer
===========================================
Scores HTML against the 8-dim AI-taste rubric.
Total score 0-16. Target: ≤4 for anti-AI-taste output.
"""

import argparse
import json
import re
import sys
from pathlib import Path


CLICHE_FONTS = {"Inter", "Roboto", "Lato", "Open Sans", "Helvetica Neue", "Poppins"}

PURPLE_GRAD_COLORS = [
    r"#667eea", r"#764ba2", r"#8b5cf6", r"#a78bfa",
    r"rgba?\(\s*102\s*,\s*126\s*,\s*234",
    r"rgba?\(\s*118\s*,\s*75\s*,\s*162",
]

EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F9FF"
    "\U0001F600-\U0001F64F"
    "\U0001F680-\U0001F6FF"
    "\U0001FA00-\U0001FAFF"
    "\U00002600-\U000027BF"
    "\U0001F300-\U0001F5FF"
    "\u2700-\u27bf"
    "]"
)

MARKETING_STEMS = [
    "futur", "next-gen", "next generation", "empower", "seamless",
    "cutting-edge", "revolutionar", "innovati",
]

# Dimension descriptions for feedback in LLM retry prompts
DIMENSIONS = {
    "font_cliche": "Uses AI-default fonts as PRIMARY font (Inter, Roboto, Lato, Open Sans, Helvetica Neue, Poppins)",
    "purple_gradient": "Contains AI-signature purple-blue gradient colors (#667eea, #764ba2, #8b5cf6, #a78bfa)",
    "glassmorphism": "Uses backdrop-filter: blur + rgba white background",
    "uniform_radius": "All elements have the same border-radius (especially 12px or 16px)",
    "emoji_icons": "Contains emoji characters used as icons",
    "placeholder_copy": "Contains marketing language (future, next-gen, empower, seamless, revolutionary, innovative) in VISIBLE TEXT, not CSS",
    "heavy_shadow": "Uses fluffy colored box-shadows with blur >= 20px AND rgba color",
    "element_density": "Extremely widget-heavy page (>= 40 HTML tags in one page)",
}


def score_html(html: str) -> dict:
    """Return dict of 8 dimension scores (0-2 each) plus total (0-16)."""
    h = html.lower()

    # 1. font_cliche — only flag if AI font is the PRIMARY (first) declared font
    font_decl_match = re.search(r"font-family\s*[:=]\s*['\"]?([^;\"'>]+)", html, re.I)
    declared = [x.strip().strip("'\"") for x in (font_decl_match.group(1).split(",") if font_decl_match else []) if x.strip()]
    primary_font = declared[0] if declared else ""
    # Match full font name (handles multi-word fonts like "Open Sans", "Helvetica Neue")
    font_hits = [f for f in CLICHE_FONTS if f.lower() == primary_font.lower()]
    font_score = 2 if font_hits else 0

    # 2. purple_gradient — only flag actual purple-blue gradient colors
    has_purple = any(re.search(p, h) for p in PURPLE_GRAD_COLORS)
    grad_score = 2 if has_purple else 0

    # 3. glassmorphism — needs BOTH blur AND rgba white overlay
    has_blur = bool(re.search(r"(?:filter|backdrop-filter)\s*:\s*blur\s*\(\s*([5-9]|[1-9][0-9])", h))
    has_rgba = any(f"rgba(255,255,255,0.{i}" in h.replace(" ", "") for i in [1, 2, 3])
    glass_score = 2 if (has_blur and has_rgba) else 0

    # 4. uniform_radius — flag only when ALL radii are identical AND it's the AI-typical 12/16px
    radii = [int(r) for r in re.findall(r"border-radius\s*:\s*(\d+)px", h) if r.isdigit()]
    radii = [r for r in radii if r > 0]
    if not radii:
        radius_score = 0
    else:
        unique = set(radii)
        radius_score = 2 if (len(unique) == 1 and list(unique)[0] in (12, 16)) else 0

    # 5. emoji_icons
    emoji_count = len(EMOJI_RE.findall(html))
    emoji_score = 2 if emoji_count >= 5 else (1 if emoji_count >= 1 else 0)

    # 6. placeholder_copy — check only in visible text, not CSS/JS properties
    # Strip style and script tags first
    visible = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.S | re.I)
    visible = re.sub(r"<script[^>]*>.*?</script>", "", visible, flags=re.S | re.I)
    visible_lower = visible.lower()
    copy_hits = sum(1 for stem in MARKETING_STEMS if stem in visible_lower)
    copy_score = 2 if copy_hits >= 3 else (1 if copy_hits >= 1 else 0)

    # 7. heavy_shadow — only flag fluffy shadows (blur >= 20 AND rgba color)
    # Hard offset shadows (no blur or blur < 10) are fine for many styles
    shadow_matches = re.findall(r"box-shadow\s*:\s*([^;}{]+)", h)
    fluffy_count = 0
    for shadow_val in shadow_matches:
        has_big_blur = bool(re.search(r"\b([2-9][0-9]|1[0-9]{2,})px\b", shadow_val))
        has_rgba_color = "rgba(" in shadow_val
        if has_big_blur and has_rgba_color:
            fluffy_count += 1
    shadow_score = 2 if fluffy_count >= 3 else (1 if fluffy_count >= 1 else 0)

    # 8. element_density — only flag extremely widget-heavy pages
    elem_count = len(re.findall(r"<[a-z]+", h))
    density_score = 2 if elem_count >= 40 else 0

    scores = {
        "font_cliche": font_score,
        "purple_gradient": grad_score,
        "glassmorphism": glass_score,
        "uniform_radius": radius_score,
        "emoji_icons": emoji_score,
        "placeholder_copy": copy_score,
        "heavy_shadow": shadow_score,
        "element_density": density_score,
    }
    scores["total"] = sum(scores.values())
    return scores


def score_file(path: Path) -> dict:
    """Score an HTML file. Returns scores + pass/fail."""
    html = path.read_text(encoding="utf-8")
    scores = score_html(html)
    scores["file"] = str(path)
    scores["pass"] = scores["total"] <= 4
    return scores


__all__ = [
    "score_html",
    "score_file",
    "main",
    "DIMENSIONS",
    "CLICHE_FONTS",
    "PURPLE_GRAD_COLORS",
    "MARKETING_STEMS",
    "EMOJI_RE",
]


def main(argv: list = None) -> int:
    """CLI entry point. Score one or more HTML files (or `-` for stdin).

    Examples:
      anti-ai-score styles/bauhaus/reference.html
      anti-ai-score a.html b.html --threshold 6
      cat page.html | anti-ai-score -
    """
    parser = argparse.ArgumentParser(
        prog="anti-ai-score",
        description="Score HTML against the 8-dimension anti-AI rubric (0-16; lower is better).",
    )
    parser.add_argument("files", nargs="+", help="HTML file path(s), or '-' for stdin")
    parser.add_argument(
        "-t", "--threshold", type=int, default=4,
        help="pass threshold for total score (default: 4)",
    )
    parser.add_argument("--pretty", action="store_true", help="pretty-print JSON")
    args = parser.parse_args(argv)

    results = []
    for f in args.files:
        if f == "-":
            html = sys.stdin.read()
            scores = score_html(html)
            scores["file"] = "<stdin>"
        else:
            path = Path(f)
            if not path.exists():
                print(f"anti-ai-score: {f}: file not found", file=sys.stderr)
                return 1
            scores = score_file(path)
        scores["pass"] = scores["total"] <= args.threshold
        results.append(scores)

    indent = 2 if args.pretty else None
    print(json.dumps(results, indent=indent, ensure_ascii=False))

    # Exit non-zero if any file failed the threshold (handy in CI / scripts)
    return 1 if any(not r["pass"] for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
