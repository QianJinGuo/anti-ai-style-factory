# Anti-AI Style Factory

> Score any HTML for "AI taste." Generate anti-AI design systems from 55+ historical design movements.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/QianJinGuo/anti-ai-style-factory/actions/workflows/ci.yml/badge.svg)](https://github.com/QianJinGuo/anti-ai-style-factory/actions)

**Anti-AI Style Factory** is a harness pipeline that generates design style specifications inspired by real historical design movements — Bauhaus, Swiss International, Ukiyo-e, Memphis, Cyberpunk, and 50+ more. Every generated style passes an 8-dimension "anti-AI taste" rubric: no Inter font, no purple gradients, no glassmorphism, no emoji icons.

The **scorer** is pure Python with zero dependencies — use it standalone in CI to catch AI-taste HTML before it ships.

---

## Quick Start

### Install

```bash
pip install -e .

# Or just the dependencies:
pip install -r requirements.txt
```

### Score HTML (zero dependencies)

The scorer works standalone — no LLM needed:

```bash
# Score a file
anti-ai-score styles/bauhaus/reference.html

# Score from stdin
cat page.html | anti-ai-score -

# Score multiple files with custom threshold
anti-ai-score a.html b.html --threshold 6

# Pretty-print JSON
anti-ai-score page.html --pretty
```

Use it as a Python library:

```python
from src.scorer import score_html

scores = score_html(html_string)
print(scores["total"])        # 0-16, lower = more anti-AI
print(scores["font_cliche"])  # 0 or 2
print(scores["pass"])         # True if total <= 4
```

### Generate Styles

Configure your LLM provider in `config/pipeline.yaml`, then:

```bash
anti-ai-factory --seed bauhaus       # Generate one seed
anti-ai-factory --tier 1             # Generate an entire tier
anti-ai-factory --batch 5            # Process next 5 pending seeds
anti-ai-factory --workers 5          # 5 concurrent workers
anti-ai-factory --status             # Show generation status
anti-ai-factory --dry-run            # Preview without generating
```

---

## The 8-Dimension Rubric

Every generated HTML is scored on 8 dimensions (0-2 each, 0-16 total). Target: **≤ 4** to pass.

| Dimension | What it detects | Score |
|-----------|----------------|-------|
| `font_cliche` | AI-default fonts as primary (Inter, Roboto, Lato, Open Sans, Poppins) | 0/2 |
| `purple_gradient` | AI-signature purple-blue gradients (#667eea, #764ba2) | 0/2 |
| `glassmorphism` | backdrop-filter: blur + rgba white overlay | 0/2 |
| `uniform_radius` | All elements have identical border-radius (12px or 16px) | 0/2 |
| `emoji_icons` | Emoji characters used as UI icons | 0/1/2 |
| `placeholder_copy` | Marketing language ("seamless", "revolutionary", "empower") | 0/1/2 |
| `heavy_shadow` | Fluffy colored box-shadows (blur ≥ 20px + rgba) | 0/1/2 |
| `element_density` | Extremely widget-heavy pages (≥ 40 HTML tags) | 0/2 |

### Gate Rules

All generated `reference.html` must also:
- ❌ Not use Inter/Roboto/Lato/Open Sans/Poppins as primary font
- ❌ Not contain purple-blue gradients (#667eea, #764ba2)
- ❌ Not use glassmorphism (backdrop-filter: blur)
- ❌ Not use emoji as icons

---

## Architecture

```
catalog/SEEDS.md         ← 15,000+ style seed definitions (55 movements × regions × media × palettes)
config/pipeline.yaml     ← LLM provider config + scoring thresholds
src/
  generator/             ← LLM call layer (generates DESIGN.md + HTML)
  scorer/                ← 8-dimension scorer (pure Python, zero deps)
  pipeline/              ← Main harness loop (generate → score → accept/reject → iterate)
sample_styles/           ← 10 curated example outputs
scripts/                 ← Gallery builder, seed generator, repair tools
gallery/                 ← Web-based preview gallery + scorer UI
demos/                   ← Standalone demo HTML files
```

---

## LLM Provider Configuration

`config/pipeline.yaml` supports multiple providers. Switch by changing `llm.provider`:

```yaml
llm:
  provider: openai        # openai | xfyun | any OpenAI-compatible API
  model: "gpt-4o"
  max_tokens: 4096
  temperature: 0.7
  providers:
    openai:
      base_url: "https://api.openai.com/v1"
      api_key_env: "OPENAI_API_KEY"
    xfyun:
      base_url: "https://maas-api.cn-huabei-1.xf-yun.com/v2"
      api_key_env: "XFYUN_API_KEY"
```

API key resolution: environment variable → `.env` file in project root.

---

## Design Movement Seeds

The `catalog/SEEDS.md` contains 15,000+ seed definitions organized in tiers:

| Tier | Description | Examples |
|------|-------------|----------|
| 1 | Core movements | Bauhaus, Swiss International, Brutalist Web, Art Deco, Memphis |
| 2 | Regional variants | Bauhaus·Berlin, Art Deco·Shanghai, Ukiyo-e·Edo |
| 3 | Medium adaptations | Poster, Book Cover, Dashboard, Landing Page |
| 4 | Palette variations | Warm, Cool, Earth, Neon, Monochrome, Pastel |
| 5 | Material textures | Grain, Paper, Canvas, Stone, Metal, Wood |
| 6+ | Full combinations | All dimensions composed |

Each seed captures: movement name, era, region, core principles, and anti-AI signals.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Adding new design movement seeds
- Improving the scorer rubric
- Submitting generated styles

---

## License

[MIT](LICENSE) — use the scorer in your CI, fork the generator, build on top.

---

## Related

- [DESIGN.md spec](https://github.com/nicedoc/designmd) — Google's design token format
- [Anti-AI Style Gallery](https://qianjinguo.github.io/anti-ai-style-factory/) — Browse generated styles online
