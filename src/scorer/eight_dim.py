"""
Anti-AI Style Factory — 8-Dimension Scorer
===========================================
Scores HTML against the 8-dim AI-taste rubric.
Total score 0-16. Target: ≤4 for anti-AI-taste output.
"""

import re
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
    "cutting-edge", "revolutionar", "innovati", "transform",
]


# Dimension descriptions for feedback in LLM retry prompts
DIMENSIONS = {
    "font_cliche": "Uses AI-default fonts (Inter, Roboto, Lato, Open Sans, Helvetica Neue, Poppins)",
    "purple_gradient": "Contains AI-signature purple-blue gradient colors (#667eea, #764ba2, #8b5cf6, #a78bfa)",
    "glassmorphism": "Uses backdrop-filter: blur + rgba white background",
    "uniform_radius": "All elements have the same border-radius (especially 12px or 16px)",
    "emoji_icons": "Contains emoji characters used as icons",
    "placeholder_copy": "Contains marketing language (future, next-gen, empower, seamless, revolutionary)",
    "heavy_shadow": "Uses fluffy colored box-shadows with blur >= 20px",
    "element_density": "Too many HTML elements on one page (>= 25 is AI-typical widget pile-up)",
}


def score_html(html: str) -> dict:
    """Return dict of 8 dimension scores (0-2 each) plus total (0-16)."""
    h = html.lower()

    # 1. font_cliche — parse font-family declarations
    font_decl_match = re.search(r"font-family\s*[:=]\s*['\"]?([^;\"'>]+)", html, re.I)
    declared = [x.strip() for x in (font_decl_match.group(1).split(",") if font_decl_match else [])]
    declared_names = [d.split()[0].strip("'\"") for d in declared if d]
    font_hits = [f for f in CLICHE_FONTS if any(f.lower() == d.lower() for d in declared_names)]
    font_score = 2 if (font_hits and declared_names and declared_names[0] in CLICHE_FONTS) else (1 if font_hits else 0)

    # 2. purple_gradient
    has_purple = any(re.search(p, h) for p in PURPLE_GRAD_COLORS)
    grad_score = 2 if has_purple else (1 if "linear-gradient" in h else 0)

    # 3. glassmorphism
    has_blur = bool(re.search(r"(?:filter|backdrop-filter)\s*:\s*blur\s*\(\s*([5-9]|[1-9][0-9])", h))
    has_rgba = any(f"rgba(255,255,255,0.{i}" in h.replace(" ", "") for i in [1, 2, 3])
    glass_score = 2 if (has_blur and has_rgba) else (1 if has_blur else 0)

    # 4. uniform_radius
    radii = [int(r) for r in re.findall(r"border-radius\s*:\s*(\d+)px", h) if r.isdigit()]
    radii = [r for r in radii if r > 0]
    if not radii:
        radius_score = 0
    else:
        unique = set(radii)
        radius_score = 2 if (len(unique) == 1 and list(unique)[0] in (12, 16)) else (1 if len(unique) <= 2 else 0)

    # 5. emoji_icons
    emoji_count = len(EMOJI_RE.findall(html))
    emoji_score = 2 if emoji_count >= 5 else (1 if emoji_count >= 1 else 0)

    # 6. placeholder_copy — stem matching (catches innovative/innovation/innovating)
    copy_hits = sum(1 for stem in MARKETING_STEMS if stem in h)
    copy_score = 2 if copy_hits >= 3 else (1 if copy_hits >= 1 else 0)

    # 7. heavy_shadow
    heavy = bool(re.search(r"box-shadow[^;}]*rgba?[^;}]*\b([2-9][0-9]|1[0-9]{2})", h))
    shadow_score = 2 if heavy else (1 if "box-shadow" in h else 0)

    # 8. element_density
    elem_count = len(re.findall(r"<[a-z]+", h))
    density_score = 2 if elem_count >= 25 else (1 if elem_count >= 12 else 0)

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
