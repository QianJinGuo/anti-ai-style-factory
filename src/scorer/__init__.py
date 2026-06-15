"""
Anti-AI Style Factory — 8-Dimension Scorer
===========================================
Scores HTML against the AI-taste rubric. Pure Python, no deps.
Reuses the proven rubric from design-md skill.
"""

import re
from dataclasses import dataclass, field

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

MARKETING_WORDS = [
    "future", "next-gen", "next generation", "empower", "seamless",
    "cutting-edge", "revolutionary", "innovation", "innovative", "transform",
]


@dataclass
class ScoreResult:
    font_cliche: int = 0
    purple_gradient: int = 0
    glassmorphism: int = 0
    uniform_radius: int = 0
    emoji_icons: int = 0
    placeholder_copy: int = 0
    heavy_shadow: int = 0
    element_density: int = 0
    notes: list = field(default_factory=list)

    @property
    def total(self) -> int:
        return (
            self.font_cliche + self.purple_gradient + self.glassmorphism +
            self.uniform_radius + self.emoji_icons + self.placeholder_copy +
            self.heavy_shadow + self.element_density
        )

    def passed(self, threshold: int = 4) -> bool:
        return self.total <= threshold

    def failing_dims(self) -> list:
        return [k for k in [
            "font_cliche", "purple_gradient", "glassmorphism",
            "uniform_radius", "emoji_icons", "placeholder_copy",
            "heavy_shadow", "element_density",
        ] if getattr(self, k) > 0]

    def to_dict(self) -> dict:
        d = {k: getattr(self, k) for k in [
            "font_cliche", "purple_gradient", "glassmorphism",
            "uniform_radius", "emoji_icons", "placeholder_copy",
            "heavy_shadow", "element_density",
        ]}
        d["total"] = self.total
        d["verdict"] = "PASS" if self.passed() else "FAIL"
        d["failing"] = self.failing_dims()
        d["notes"] = self.notes
        return d


def score_html(html: str) -> ScoreResult:
    """Score HTML against the 8-dimension AI-taste rubric."""
    r = ScoreResult()
    h = html.lower()

    # 1. font_cliche — parse font-family declarations
    font_decl_match = re.search(r"font-family\s*[:=]\s*['\"]?([^;\"'>]+)", html, re.I)
    declared = [x.strip() for x in (font_decl_match.group(1).split(",") if font_decl_match else [])]
    declared_names = [d.split()[0].strip("'\"") for d in declared if d]
    font_hits = [f for f in CLICHE_FONTS if any(f.lower() == d.lower() for d in declared_names)]
    if font_hits:
        r.font_cliche = 2 if declared_names and declared_names[0] in CLICHE_FONTS else 1
        r.notes.append(f"Cliche fonts found: {font_hits}")

    # 2. purple_gradient
    has_purple_grad = any(re.search(p, h) for p in PURPLE_GRAD_COLORS)
    if has_purple_grad:
        r.purple_gradient = 2
        r.notes.append("AI-signature purple gradient detected")
    elif "linear-gradient" in h:
        r.purple_gradient = 1
        r.notes.append("Gradient present (not AI-purple, but flagged)")

    # 3. glassmorphism
    has_blur = bool(re.search(
        r"(?:filter|backdrop-filter)\s*:\s*blur\s*\(\s*([5-9]|[1-9][0-9])", h
    ))
    has_rgba_white = any(
        f"rgba(255,255,255,0.{i}" in h.replace(" ", "") for i in [1, 2, 3]
    )
    if has_blur and has_rgba_white:
        r.glassmorphism = 2
        r.notes.append("Glassmorphism: backdrop-filter blur + rgba white")
    elif has_blur:
        r.glassmorphism = 1

    # 4. uniform_radius
    radii = [int(x) for x in re.findall(r"border-radius\s*:\s*(\d+)px", h) if x.isdigit()]
    radii = [x for x in radii if x > 0]
    if radii:
        unique = set(radii)
        if len(unique) == 1 and list(unique)[0] in (12, 16):
            r.uniform_radius = 2
            r.notes.append(f"Uniform AI-default radius: {list(unique)[0]}px")
        elif len(unique) <= 2:
            r.uniform_radius = 1

    # 5. emoji_icons
    emoji_count = len(EMOJI_RE.findall(html))
    if emoji_count >= 5:
        r.emoji_icons = 2
        r.notes.append(f"{emoji_count} emoji found")
    elif emoji_count >= 1:
        r.emoji_icons = 1
        r.notes.append(f"{emoji_count} emoji found")

    # 6. placeholder_copy — word-stem matching, skip CSS properties
    # Strip CSS to avoid false positives on "text-transform" etc.
    html_no_css = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.DOTALL | re.I)
    h_no_css = html_no_css.lower()
    marketing_hits = [w for w in MARKETING_WORDS if w in h_no_css]
    if len(marketing_hits) >= 3:
        r.placeholder_copy = 2
        r.notes.append(f"Marketing copy detected: {marketing_hits}")
    elif len(marketing_hits) >= 1:
        r.placeholder_copy = 1
        # Check if it's just a CSS property
        if marketing_hits == ["transform"] and "text-transform" in h:
            r.placeholder_copy = 0  # false positive, CSS property
            r.notes = [n for n in r.notes if "Marketing" not in n]

    # 7. heavy_shadow
    heavy_shadow = bool(re.search(
        r"box-shadow[^;}]*rgba?[^;}]*\b([2-9][0-9]|1[0-9]{2})", h
    ))
    if heavy_shadow:
        r.heavy_shadow = 2
        r.notes.append("Heavy blurred shadow detected")
    elif "box-shadow" in h:
        # Check if it's a hard shadow (0 blur)
        hard_shadow = bool(re.search(r"box-shadow[^;]*\d+px\s+\d+px\s+0px", h))
        if not hard_shadow:
            r.heavy_shadow = 1

    # 8. element_density
    elem_count = len(re.findall(r"<[a-z]+", h))
    if elem_count >= 25:
        r.element_density = 2
        r.notes.append(f"High density: {elem_count} elements")
    elif elem_count >= 12:
        r.element_density = 1

    return r
