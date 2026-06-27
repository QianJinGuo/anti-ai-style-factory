"""
Tests for the 8-dimension anti-AI taste scorer.

Covers every dimension with positive (should trigger) and negative (should not) cases,
plus edge cases, the pass/fail gate, and the CLI entry point.
"""

import json
import sys
from pathlib import Path

import pytest

# Ensure project root is on path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.scorer.eight_dim import score_html, score_file, main, DIMENSIONS


# ── Helpers ──────────────────────────────────────────────────

def clean_html(**overrides):
    """Return a minimal anti-AI-clean HTML page. Override any dimension."""
    base = """<!DOCTYPE html>
<html>
<head>
<style>
  body { font-family: 'EB Garamond', serif; margin: 0; }
  h1 { font-size: 32px; }
  .card { border: 1px solid #333; padding: 16px; }
</style>
</head>
<body>
  <nav>Nav</nav>
  <h1>Workshop Production Report</h1>
  <p>Q3 output: 1,247 units assembled, 98.2% pass rate.</p>
  <div class="card">Metric A: 42</div>
  <div class="card">Metric B: 87</div>
</body>
</html>"""
    # Apply overrides by string replacement
    html = base
    for key, val in overrides.items():
        if key == "font":
            html = html.replace("font-family: 'EB Garamond', serif", f"font-family: {val}")
        elif key == "add_style":
            html = html.replace("</style>", f"  {val}\n</style>")
        elif key == "add_body":
            html = html.replace("</body>", f"  {val}\n</body>")
    return html


# ── Dimension 1: font_cliche ─────────────────────────────────

class TestFontCliche:
    """Detects AI-default fonts as PRIMARY font."""

    @pytest.mark.parametrize("font", [
        "Inter, sans-serif",
        "Roboto, sans-serif",
        "Lato, sans-serif",
        "Open Sans, sans-serif",
        "Helvetica Neue, sans-serif",
        "Poppins, sans-serif",
    ])
    def test_ai_font_as_primary_scores_2(self, font):
        html = clean_html(font=font)
        scores = score_html(html)
        assert scores["font_cliche"] == 2

    def test_ai_font_as_secondary_ignored(self):
        """Only the PRIMARY (first) font triggers the score."""
        html = clean_html(font="'EB Garamond', Inter, sans-serif")
        scores = score_html(html)
        assert scores["font_cliche"] == 0

    def test_custom_font_scores_0(self):
        html = clean_html(font="'Georgia', serif")
        scores = score_html(html)
        assert scores["font_cliche"] == 0

    def test_no_font_declaration_scores_0(self):
        html = "<html><body><p>Hello</p></body></html>"
        scores = score_html(html)
        assert scores["font_cliche"] == 0

    def test_case_insensitive_match(self):
        html = clean_html(font="inter, sans-serif")
        scores = score_html(html)
        assert scores["font_cliche"] == 2


# ── Dimension 2: purple_gradient ─────────────────────────────

class TestPurpleGradient:
    """Detects AI-signature purple-blue gradient colors."""

    @pytest.mark.parametrize("color", [
        "#667eea",
        "#764ba2",
        "#8b5cf6",
        "#a78bfa",
    ])
    def test_purple_hex_color_scores_2(self, color):
        html = clean_html(add_style=f"a {{ color: {color}; }}")
        scores = score_html(html)
        assert scores["purple_gradient"] == 2

    def test_rgba_purple_scores_2(self):
        html = clean_html(add_style="a { color: rgba(102, 126, 234, 0.5); }")
        scores = score_html(html)
        assert scores["purple_gradient"] == 2

    def test_no_purple_scores_0(self):
        html = clean_html(add_style="a { color: #3366cc; }")
        scores = score_html(html)
        assert scores["purple_gradient"] == 0

    def test_random_hex_not_flagged(self):
        html = clean_html(add_style="a { color: #667890; }")
        scores = score_html(html)
        assert scores["purple_gradient"] == 0


# ── Dimension 3: glassmorphism ───────────────────────────────

class TestGlassmorphism:
    """Detects backdrop-filter: blur + rgba white overlay."""

    def test_blur_plus_rgba_white_scores_2(self):
        html = clean_html(add_style=".card { backdrop-filter: blur(10px); background: rgba(255,255,255,0.2); }")
        scores = score_html(html)
        assert scores["glassmorphism"] == 2

    def test_blur_only_no_score(self):
        html = clean_html(add_style=".card { backdrop-filter: blur(10px); }")
        scores = score_html(html)
        assert scores["glassmorphism"] == 0

    def test_rgba_white_only_no_score(self):
        html = clean_html(add_style=".card { background: rgba(255,255,255,0.2); }")
        scores = score_html(html)
        assert scores["glassmorphism"] == 0

    def test_small_blur_no_score(self):
        """Blur < 5px should not trigger."""
        html = clean_html(add_style=".card { backdrop-filter: blur(3px); background: rgba(255,255,255,0.2); }")
        scores = score_html(html)
        assert scores["glassmorphism"] == 0


# ── Dimension 4: uniform_radius ──────────────────────────────

class TestUniformRadius:
    """Detects uniform AI-typical border-radius (all identical 12px or 16px)."""

    def test_all_12px_scores_2(self):
        html = clean_html(add_style="""
            .a { border-radius: 12px; }
            .b { border-radius: 12px; }
            .c { border-radius: 12px; }
        """)
        scores = score_html(html)
        assert scores["uniform_radius"] == 2

    def test_all_16px_scores_2(self):
        html = clean_html(add_style="""
            .a { border-radius: 16px; }
            .b { border-radius: 16px; }
        """)
        scores = score_html(html)
        assert scores["uniform_radius"] == 2

    def test_mixed_radii_no_score(self):
        html = clean_html(add_style="""
            .a { border-radius: 12px; }
            .b { border-radius: 8px; }
        """)
        scores = score_html(html)
        assert scores["uniform_radius"] == 0

    def test_uniform_but_not_ai_typical(self):
        """All 4px is uniform but not the AI-typical 12/16."""
        html = clean_html(add_style="""
            .a { border-radius: 4px; }
            .b { border-radius: 4px; }
        """)
        scores = score_html(html)
        assert scores["uniform_radius"] == 0

    def test_no_radius_no_score(self):
        scores = score_html(clean_html())
        assert scores["uniform_radius"] == 0


# ── Dimension 5: emoji_icons ─────────────────────────────────

class TestEmojiIcons:
    """Detects emoji characters used as icons."""

    def test_5_or_more_emoji_scores_2(self):
        html = clean_html(add_body="""
            <span>🚀</span><span>📊</span><span>💡</span><span>🎯</span><span>✨</span>
        """)
        scores = score_html(html)
        assert scores["emoji_icons"] == 2

    def test_1_to_4_emoji_scores_1(self):
        html = clean_html(add_body="<span>🔥</span><span>📊</span>")
        scores = score_html(html)
        assert scores["emoji_icons"] == 1

    def test_no_emoji_scores_0(self):
        scores = score_html(clean_html())
        assert scores["emoji_icons"] == 0


# ── Dimension 6: placeholder_copy ────────────────────────────

class TestPlaceholderCopy:
    """Detects marketing language in visible text (not CSS)."""

    def test_3_plus_stems_scores_2(self):
        html = clean_html(add_body="""
            <p>Our revolutionary platform empowers seamless innovation.</p>
        """)
        scores = score_html(html)
        assert scores["placeholder_copy"] == 2

    def test_1_stem_scores_1(self):
        html = clean_html(add_body="<p>Next generation workflow.</p>")
        scores = score_html(html)
        assert scores["placeholder_copy"] == 1

    def test_no_marketing_scores_0(self):
        scores = score_html(clean_html())
        assert scores["placeholder_copy"] == 0

    def test_stems_in_css_only_no_score(self):
        """Marketing words inside <style> tags should NOT trigger."""
        html = clean_html(add_style="/* seamless revolutionary innovative */")
        scores = score_html(html)
        assert scores["placeholder_copy"] == 0

    def test_stems_in_script_only_no_score(self):
        """Marketing words inside <script> tags should NOT trigger."""
        html = clean_html(add_body='<script>var seamless = "revolutionary";</script>')
        scores = score_html(html)
        assert scores["placeholder_copy"] == 0


# ── Dimension 7: heavy_shadow ────────────────────────────────

class TestHeavyShadow:
    """Detects fluffy colored box-shadows (blur >= 20px + rgba)."""

    def test_3_plus_fluffy_shadows_scores_2(self):
        html = clean_html(add_style="""
            .a { box-shadow: 0 4px 20px rgba(0,0,0,0.1); }
            .b { box-shadow: 0 4px 25px rgba(100,100,255,0.2); }
            .c { box-shadow: 0 4px 30px rgba(255,0,0,0.15); }
        """)
        scores = score_html(html)
        assert scores["heavy_shadow"] == 2

    def test_1_fluffy_shadow_scores_1(self):
        html = clean_html(add_style=".a { box-shadow: 0 4px 20px rgba(0,0,0,0.1); }")
        scores = score_html(html)
        assert scores["heavy_shadow"] == 1

    def test_hard_shadow_no_score(self):
        """Hard offset shadows (no blur) are fine."""
        html = clean_html(add_style=".a { box-shadow: 2px 2px 0 #000; }")
        scores = score_html(html)
        assert scores["heavy_shadow"] == 0

    def test_small_blur_no_score(self):
        html = clean_html(add_style=".a { box-shadow: 0 2px 8px rgba(0,0,0,0.1); }")
        scores = score_html(html)
        assert scores["heavy_shadow"] == 0


# ── Dimension 8: element_density ─────────────────────────────

class TestElementDensity:
    """Detects extremely widget-heavy pages (>= 40 HTML tags)."""

    def test_40_plus_tags_scores_2(self):
        tags = "".join(f"<div class='w{i}'>Widget {i}</div>" for i in range(45))
        html = clean_html(add_body=tags)
        scores = score_html(html)
        assert scores["element_density"] == 2

    def test_under_40_tags_scores_0(self):
        scores = score_html(clean_html())
        assert scores["element_density"] == 0


# ── Total score & pass/fail ──────────────────────────────────

class TestTotalScore:
    """Integration tests for total score and pass/fail logic."""

    def test_clean_page_scores_low(self):
        """A clean page with no AI markers should score 0."""
        scores = score_html(clean_html())
        assert scores["total"] == 0
        assert scores["total"] <= 4  # pass

    def test_max_ai_page_scores_high(self):
        """A page with every AI marker should score near 16."""
        html = """<!DOCTYPE html>
<html>
<head>
<style>
  body { font-family: 'Inter', sans-serif; }
  .card {
    border-radius: 12px;
    backdrop-filter: blur(10px);
    background: rgba(255,255,255,0.2);
    box-shadow: 0 4px 20px rgba(102,126,234,0.2);
    color: #667eea;
  }
  .a { border-radius: 12px; }
  .b { border-radius: 12px; }
  .c { border-radius: 12px; }
  .d { box-shadow: 0 4px 25px rgba(0,0,0,0.15); }
  .e { box-shadow: 0 4px 30px rgba(100,100,255,0.2); }
</style>
</head>
<body>
  <nav>Nav</nav>
  <h1>Revolutionary seamless platform</h1>
  <p>Next-gen innovative empower future cutting-edge.</p>
  <div class="card">🚀</div>
  <div class="card">📊</div>
  <div class="card">💡</div>
  <div class="card">🎯</div>
  <div class="card">✨</div>
  """ + "".join(f"<div class='w{i}'>W{i}</div>" for i in range(45)) + """
</body>
</html>"""
        scores = score_html(html)
        assert scores["font_cliche"] == 2
        assert scores["purple_gradient"] == 2
        assert scores["glassmorphism"] == 2
        assert scores["uniform_radius"] == 2
        assert scores["emoji_icons"] == 2
        assert scores["placeholder_copy"] == 2
        assert scores["heavy_shadow"] == 2
        assert scores["element_density"] == 2
        assert scores["total"] == 16

    def test_pass_threshold_default(self):
        scores = score_html(clean_html())
        assert scores["total"] <= 4

    def test_score_keys(self):
        """Output dict should contain all 8 dimension keys + total."""
        scores = score_html(clean_html())
        expected_keys = set(DIMENSIONS.keys()) | {"total"}
        assert expected_keys == set(scores.keys())


# ── score_file ───────────────────────────────────────────────

class TestScoreFile:
    """Test file-based scoring."""

    def test_score_sample_style(self, tmp_path):
        html = clean_html()
        f = tmp_path / "test.html"
        f.write_text(html)
        scores = score_file(f)
        assert scores["file"] == str(f)
        assert scores["pass"] is True
        assert scores["total"] == 0

    def test_score_file_with_ai_content(self, tmp_path):
        html = clean_html(
            font="Inter, sans-serif",
            add_style="a { color: #667eea; } .a { border-radius: 12px; } .b { border-radius: 12px; } .c { border-radius: 12px; }",
        )
        f = tmp_path / "ai.html"
        f.write_text(html)
        scores = score_file(f)
        assert scores["pass"] is False
        assert scores["total"] >= 6


# ── CLI entry point ──────────────────────────────────────────

class TestCLI:
    """Test the anti-ai-score CLI."""

    def test_score_single_file(self, tmp_path, capsys):
        f = tmp_path / "clean.html"
        f.write_text(clean_html())
        ret = main([str(f)])
        assert ret == 0
        out = json.loads(capsys.readouterr().out)
        assert len(out) == 1
        assert out[0]["total"] == 0
        assert out[0]["pass"] is True

    def test_score_stdin(self, tmp_path, capsys, monkeypatch):
        import io
        monkeypatch.setattr(sys, "stdin", io.StringIO(clean_html()))
        ret = main(["-"])
        assert ret == 0
        out = json.loads(capsys.readouterr().out)
        assert out[0]["file"] == "<stdin>"

    def test_fail_returns_nonzero(self, tmp_path, capsys):
        f = tmp_path / "ai.html"
        f.write_text(clean_html(
            font="Inter, sans-serif",
            add_style="a { color: #667eea; } .a { border-radius: 12px; } .b { border-radius: 12px; } .c { border-radius: 12px; }",
        ))
        ret = main([str(f)])
        assert ret == 1

    def test_custom_threshold(self, tmp_path, capsys):
        """With threshold=10, even a slightly-AI page should pass."""
        f = tmp_path / "marginal.html"
        f.write_text(clean_html(font="Inter, sans-serif"))  # scores 2
        ret = main([str(f), "-t", "10"])
        assert ret == 0

    def test_pretty_print(self, tmp_path, capsys):
        f = tmp_path / "clean.html"
        f.write_text(clean_html())
        main([str(f), "--pretty"])
        out = capsys.readouterr().out
        assert "\n" in out  # pretty-printed JSON has newlines

    def test_file_not_found(self, capsys):
        ret = main(["nonexistent.html"])
        assert ret == 1


# ── Sample styles validation ─────────────────────────────────

class TestSampleStyles:
    """Verify that the bundled sample styles all pass the rubric."""

    SAMPLE_DIR = Path(__file__).resolve().parent.parent / "sample_styles"

    @pytest.mark.skipif(
        not (Path(__file__).resolve().parent.parent / "sample_styles").exists(),
        reason="sample_styles/ not found"
    )
    @pytest.mark.parametrize("style", [
        "bauhaus", "swiss-intl", "brutalist-web", "art-deco",
        "cyberpunk", "ukiyo-e", "memphis", "terminal", "wabi-sabi", "pop-art",
    ])
    def test_sample_style_passes(self, style):
        html_path = self.SAMPLE_DIR / style / "reference.html"
        if not html_path.exists():
            pytest.skip(f"Sample {style} not found")
        scores = score_file(html_path)
        assert scores["total"] <= 4, (
            f"Sample style '{style}' scores {scores['total']}/16 — "
            f"failing: {', '.join(k for k, v in scores.items() if k not in ('total', 'file', 'pass') and v > 0)}"
        )
