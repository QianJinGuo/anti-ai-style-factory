# Getting Started — Anti-AI Style Factory

A harness that generates **anti-AI-taste** design styles from real design-movement DNA.
It reads style "seeds" (historical design movements), calls an LLM to produce a
`DESIGN.md` spec + a `reference.html`, then scores the output with an 8-dimension
rubric — anything scoring above 4/16 is regenerated until it passes (or gives up).

The scorer is pure-Python and zero-dependency: you can use it standalone to grade
any HTML for "AI taste," independent of generation.

---

## 1. What's in the box

| Path | Purpose |
|------|---------|
| `catalog/SEEDS.md` | 15,000+ seed definitions across **7 tiers** (movement → region → medium → palette → material). |
| `config/pipeline.yaml` | LLM provider config + scoring thresholds. |
| `src/generator/` | LLM call layer: builds prompts, calls the model, iterates. |
| `src/scorer/eight_dim.py` | The 8-dimension rubric (0–16, target ≤ 4). |
| `src/pipeline/run.py` | Main loop: generate → score → accept/reject → retry. |
| `src/pipeline/batch_runner.py` | Two-phase XFYUN batch API runner (design → html → score). |
| `scripts/seed_generator.py` | Generates the seed catalog from movement×region×media combos. |
| `styles/{seed-id}/` | **Output**: each style has `DESIGN.md` + `reference.html` + `metadata.json`. ~15,070 validated. |
| `demos/` | 5 hand-picked demo HTMLs (brutalist, japanese-minimal, neon, terrazzo, vaporwave). |

### The 7 seed tiers
1. **基础运动** (base movements) — Bauhaus, Swiss, Brutalist, Art Deco…
2. **地域变体** (regional variants)
3. **运动×媒介** (movement × medium)
4. **运动×色盘** (movement × palette) — suffixes like `-cool`, `-warm`, `-jewel`, `-neon`…
5. **运动×材质** (movement × material)
6. **运动×媒介×色盘** (medium × palette)
7. **运动×媒介×材质** (medium × material)

Every seed is a *legitimate combination* of real design history — nothing is invented.

---

## 2. Install

**Requires Python ≥ 3.9.** (The project venv runs 3.11.)

```bash
git clone <your-repo-url> anti-ai-style-factory
cd anti-ai-style-factory

# Option A — install as an editable package (recommended; gives you the CLIs)
pip install -e .

# Option B — just the runtime deps, run via python -m
pip install -r requirements.txt
```

Verify:

```bash
anti-ai-score --help      # if installed
python -m src.scorer.eight_dim --help   # if not installed
```

---

## 3. Configure your LLM

`config/pipeline.yaml` supports multiple providers — switch by editing one field:

```yaml
llm:
  provider: xfyun          # xfyun | openai  ← change this one line
  model: "xopqwen36v35b"
  max_tokens: 4096
  temperature: 0.7
  providers:
    xfyun:
      base_url: "https://maas-api.cn-huabei-1.xf-yun.com/v2"
      api_key_env: "CHATXUNFEI"
    openai:
      base_url: "https://api.openai.com/v1"
      api_key_env: "OPENAI_API_KEY"
```

**API key resolution order** (the code tries each in turn):
1. Environment variable (e.g. `export OPENAI_API_KEY=sk-...`)
2. `~/.zshenv` — a line like `export CHATXUNFEI="..."`
3. `~/.hermes/config.yaml` — matched by the provider's `base_url`

Quick check that resolution works **without** making an API call:

```bash
python -c "
import yaml
from src.generator.llm_generator import _resolve_provider, resolve_api_key
cfg = yaml.safe_load(open('config/pipeline.yaml'))
print('provider url:', _resolve_provider(cfg)[0])
print('key length:', len(resolve_api_key(cfg)))
"
```

> To add a new OpenAI-compatible provider, just add another entry under
> `llm.providers` (e.g. `deepseek`, `moonshot`, a local vLLM) — same shape:
> `base_url` + `api_key_env`.

---

## 4. Use the scorer (standalone — the easiest on-ramp)

The scorer needs **no LLM, no API key, no config.** It's the fastest way to get value.

### CLI

```bash
# Score one or more HTML files (prints JSON)
anti-ai-score styles/bauhaus/reference.html
anti-ai-score a.html b.html --threshold 6     # custom pass threshold
anti-ai-score styles/bauhaus/reference.html --pretty

# From stdin
cat my-page.html | anti-ai-score -

# Exit code is non-zero if ANY file fails the threshold (handy for CI)
anti-ai-score page.html && echo "clean" || echo "AI taste detected"
```

Sample output:

```json
[{
  "font_cliche": 0, "purple_gradient": 0, "glassmorphism": 0,
  "uniform_radius": 0, "emoji_icons": 0, "placeholder_copy": 1,
  "heavy_shadow": 0, "element_density": 2,
  "total": 3, "file": "styles/bauhaus/reference.html", "pass": true
}]
```

### As a library

```python
from src.scorer import score_html, DIMENSIONS

html = open("my-page.html").read()
scores = score_html(html)
print(scores["total"])          # 0–16, lower is better
print([k for k,v in scores.items() if k!="total" and v>0])  # failing dimensions
```

### The 8 dimensions (each scored 0–2)

| Dimension | What it flags |
|-----------|---------------|
| `font_cliche` | Inter/Roboto/Lato/Open Sans/Helvetica Neue/Poppins as primary font |
| `purple_gradient` | AI-signature purple-blue gradient (#667eea, #764ba2, #8b5cf6, #a78bfa) |
| `glassmorphism` | `backdrop-filter: blur` + rgba-white overlay |
| `uniform_radius` | Every element the same 12px/16px radius |
| `emoji_icons` | Emoji used as icons |
| `placeholder_copy` | Marketing words (future, empower, seamless, revolutionary…) in visible text |
| `heavy_shadow` | Fluffy colored box-shadows with blur ≥ 20px |
| `element_density` | Widget-heavy pages (≥ 40 elements) |

---

## 5. Generate styles (needs an LLM)

### Realtime mode (`anti-ai-factory` / `python -m src.pipeline.run`)

```bash
anti-ai-factory --status                 # see what's generated / pending
anti-ai-factory --seed bauhaus           # generate one seed
anti-ai-factory --tier 1                 # generate all of Tier 1
anti-ai-factory --batch 5                # next 5 pending seeds
anti-ai-factory --workers 5              # 5 concurrent workers (rate-limit permitting)
anti-ai-factory --dry-run                # preview without calling the LLM
anti-ai-factory --force                  # regenerate even if already validated
```

A seed is skipped if its `styles/{id}/metadata.json` already says `status: validated`.

### Batch mode (`python -m src.pipeline.batch_runner`) — for xfyun only

Three-phase, async, cheaper for large runs:

```bash
python -m src.pipeline.batch_runner --submit-design --limit 100   # A: all DESIGN.md
python -m src.pipeline.batch_runner --poll                        # check progress
python -m src.pipeline.batch_runner --consume                     # A done → submit B (html)
python -m src.pipeline.batch_runner --finalize                    # B done → score + save
python -m src.pipeline.batch_runner --status                      # batch state
```

State is tracked in `state/batches.json`.

### What each generated style looks like

```
styles/bauhaus/
├── DESIGN.md          # full spec: colors, typography, components, do's/don'ts
├── reference.html     # single-file demo: nav, hero, dashboard, palette, components, form
└── metadata.json      # id, status, scores, iterations, log
```

Open any `reference.html` in a browser to see the style.

---

## 6. Regenerate the seed catalog

`scripts/seed_generator.py` produces the 15k+ seeds by crossing real movements ×
regions × media × eras. Re-run it if you want to extend the catalog:

```bash
python scripts/seed_generator.py      # regenerates catalog/SEEDS.md
```

---

## 7. A 5-minute first run

```bash
pip install -e .
# put a key in ~/.zshenv, e.g.:  export CHATXUNFEI="..."
python -c "from src.generator.llm_generator import resolve_api_key; import yaml; \
  print('key ok, len', len(resolve_api_key(yaml.safe_load(open('config/pipeline.yaml')))))"

anti-ai-factory --status                # see the catalog
anti-ai-factory --seed bauhaus --force  # regenerate one, watch it iterate
open styles/bauhaus/reference.html      # admire it
anti-ai-score styles/bauhaus/reference.html --pretty
```

---

## 8. Roadmap — what to do next

The P1 engineering cleanup (provider abstraction, scorer packaging, installable CLI)
is **done**. Per the original review, the remaining work that meaningfully improves
adoptability, in priority order:

### P2 — Adoption surface (next ~1 day)

- **Build an online preview gallery.** A static site that lists all 15k styles with
  thumbnails + links to each `reference.html`. This is the single highest-leverage
  thing for open-source traction — right now the styles are buried in a directory
  tree nobody will browse by hand. A simple generator (iterate `styles/*/metadata.json`
  → emit one HTML index + iframes) is half a day.
- **Add GitHub Actions CI.** Run `anti-ai-score` over every `reference.html` on push
  to enforce the ≤ 4 gate automatically, plus `pip install -e .` + import smoke test.
  ~1 hour. Prevents regressions in the rubric and the generated artifacts.
- **Add a handful of unit tests** for the scorer (`tests/test_scorer.py`): one
  passing fixture, one failing per dimension. The scorer is the project's IP — it
  should be locked with tests before external contribution.

### P2 — Generation quality

- **Raise the bar on `element_density` / `placeholder_copy`.** Many validated styles
  still score 1–2 on these two dimensions (e.g. bauhaus: `placeholder_copy=1,
  element_density=2`). Tightening the prompts or the threshold would push the corpus
  toward genuinely cleaner output.
- **Diff-aware regeneration.** Currently a retry regenerates the whole HTML; feeding
  only the failing section back would save tokens and iterations.

### P3 — Ecosystem (longer term)

- **VS Code / Figma plugin** that drops a chosen style's tokens into your project.
- **DESIGN.md → Tailwind / CSS-variables / style-dictionary export.** Right now the
  token format is Google DESIGN.md; a converter would make styles drop-in for real apps.
- **Community seed contributions** — a documented schema + validator for PR'd seeds.

### Deliberately not chasing
- **More style count for its own sake.** 15k validated is already far past the point
  of diminishing returns; the bottleneck is *discoverability and integration*, not
  volume. New styles should come from new *movements or materials*, not more palette
  permutations.

---

## 9. Troubleshooting

| Symptom | Fix |
|---------|-----|
| `Missing API key: set CHATXUNFEI…` | Put the key in the env var, `~/.zshenv`, or `~/.hermes/config.yaml`. |
| `Unknown llm.provider 'X'` | The name must match a key under `llm.providers` in `pipeline.yaml`. |
| LLM call fails / 401 | Run the provider-resolution one-liner in §3 to confirm the key resolves; check `base_url`. |
| `No module named 'yaml'` | Use the project venv (`.venv/bin/python`), or `pip install pyyaml`. |
| Styles keep failing the gate | Raise `scoring.max_iterations` or inspect which dimensions fail via `anti-ai-score`. |
| `python -m` double-import warning | Fixed in the current scorer; if it returns, ensure `src/scorer/__init__.py` uses lazy `__getattr__`. |

---

## 10. Quick command reference

```bash
# Scorer (no LLM needed)
anti-ai-score file.html [--threshold N] [--pretty]
python -m src.scorer.eight_dim file.html

# Generation (LLM needed)
anti-ai-factory --status
anti-ai-factory --seed <id> [--force]
anti-ai-factory --tier N
anti-ai-factory --batch N [--workers N]
python -m src.pipeline.run ...        # equivalent

# Batch (xfyun only)
python -m src.pipeline.batch_runner --submit-design --limit N
python -m src.pipeline.batch_runner --poll
python -m src.pipeline.batch_runner --consume
python -m src.pipeline.batch_runner --finalize

# Catalog
python scripts/seed_generator.py
```
