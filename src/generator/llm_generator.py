"""
LLM-powered style generator.
Calls OpenAI-compatible API to generate DESIGN.md + reference HTML,
then scores with 8-dim rubric, iterates until passing.
"""

import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Optional

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from src.scorer.eight_dim import score_html, DIMENSIONS

# LLM client (OpenAI-compatible)
from openai import OpenAI


def _resolve_provider(config: dict) -> tuple[str, str]:
    """Return (base_url, api_key_env) for the active provider in config.

    Supports the `llm.providers` map (selected by `llm.provider`) and, for
    backward compatibility, the legacy flat `llm.base_url` / `llm.api_key_env`.
    """
    llm = config.get("llm", {})
    providers = llm.get("providers")
    if providers:
        name = llm.get("provider") or "openai"
        if name not in providers:
            raise ValueError(
                f"Unknown llm.provider '{name}'. "
                f"Available: {', '.join(providers)}"
            )
        prov = providers[name]
        return prov["base_url"], prov["api_key_env"]
    # Legacy flat config
    if "base_url" in llm and "api_key_env" in llm:
        return llm["base_url"], llm["api_key_env"]
    raise ValueError(
        "config.llm must define either `providers` (+`provider`) "
        "or flat `base_url`+`api_key_env`"
    )


def resolve_api_key(config: dict) -> str:
    """Resolve the active provider's API key.

    Order: env var  ->  .env file in project root.
    Shared by the realtime generator and the batch runner.
    """
    _base_url, env_var = _resolve_provider(config)

    # Load .env file from project root if present
    env_path = Path(__file__).resolve().parent.parent.parent / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith(f"export {env_var}=") or line.startswith(f"{env_var}="):
                val = line.split("=", 1)[1].strip().strip('"').strip("'")
                if val:
                    os.environ.setdefault(env_var, val)

    api_key = os.environ.get(env_var, "")
    if not api_key:
        raise ValueError(
            f"Missing API key: set {env_var} env var or add it to .env file"
        )
    return api_key


def get_client(config: dict) -> OpenAI:
    """Create an OpenAI-compatible client for the active provider."""
    base_url, _env_var = _resolve_provider(config)
    api_key = resolve_api_key(config)
    return OpenAI(
        base_url=base_url,
        api_key=api_key,
    )


SYSTEM_PROMPT = """You are a world-class design systems architect. You create original
design style specifications inspired by real historical design movements.

Your output must be ANTI-AI-TASTE. That means:
1. NO Inter, Roboto, Lato, Open Sans, Helvetica Neue, or Poppins fonts
2. NO purple-blue gradients (#667eea, #764ba2, #8b5cf6, #a78bfa)
3. NO glassmorphism (backdrop-filter: blur + rgba white)
4. NO uniform 12px or 16px border-radius everywhere
5. NO emoji as icons
6. NO marketing language ("future", "next-gen", "empower", "seamless", "revolutionary")
7. NO fluffy colored box-shadows with blur >= 20px

You must follow the design principles of the specified movement faithfully.
Every visual choice must be justified by the movement's philosophy."""


def build_design_md_prompt(seed: dict) -> str:
    """Build prompt for generating DESIGN.md."""
    return f"""Generate a complete DESIGN.md specification for the "{seed['name']}" design style.

Movement: {seed['name']}
Era: {seed['era']}
Region: {seed['region']}
Core principles: {seed['principle']}
Anti-AI signals: {seed['anti_ai_signal']}

Output a Google DESIGN.md format file with:
1. YAML front matter with: version, name, description, colors (primary/secondary/tertiary/neutral/muted), typography (h1/h2/h3/body-md/caption with fontFamily/fontSize/fontWeight/lineHeight/letterSpacing), rounded (sm/md/lg), spacing (sm/md/lg/xl), components (button-primary, card, table, etc.)
2. Markdown body with sections: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts

Rules:
- Font choices must match the movement's character, NOT AI defaults
- Color palette must be historically grounded
- Every component must serve the content, not decorate it
- The description should capture the movement's philosophy in one sentence

Output ONLY the DESIGN.md content, no extra commentary."""


def build_reference_html_prompt(seed: dict, design_md: str) -> str:
    """Build prompt for generating reference HTML."""
    return f"""Generate a single-file reference HTML implementation for the "{seed['name']}" style.

Here is the DESIGN.md specification to follow:

{design_md}

The reference HTML must include ALL of these sections:
1. NAV — top navigation bar
2. HERO — headline + subtitle + CTA buttons
3. DASHBOARD — 3 key metrics + data table with 4 rows
4. PALETTE — color swatches showing all named colors
5. COMPONENTS — cards demonstrating the style's key components
6. FORM — input fields + select + submit button

Rules:
- Use Google Fonts CDN for the specified fonts
- ALL CSS must be inline in a <style> tag
- Use CSS custom properties matching the DESIGN.md tokens
- ZERO border-radius unless the DESIGN.md specifies non-zero
- ZERO box-shadow with blur (hard offset shadows only if specified)
- ZERO linear-gradient
- ZERO emoji
- ZERO marketing language
- Concrete, specific content (workshop data, production metrics) — NOT "Lorem ipsum"
- The page must look like it belongs to the {seed['name']} movement, not like a generic SaaS template

Output ONLY the complete HTML file, no extra commentary."""


def call_llm(client: OpenAI, config: dict, system: str, prompt: str) -> Optional[str]:
    """Call LLM and return response content."""
    try:
        resp = client.chat.completions.create(
            model=config["llm"]["model"],
            max_tokens=config["llm"]["max_tokens"],
            temperature=config["llm"]["temperature"],
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
        )
        return resp.choices[0].message.content
    except Exception as e:
        print(f"  LLM call failed: {e}")
        return None


def extract_code_block(text: str) -> str:
    """Extract content from markdown code blocks if present.
    Strips ```html, ```yaml, ```markdown etc. fences from LLM output.
    """
    stripped = text.strip()
    # Pattern: opening fence ```lang, content, closing fence ```
    m = re.search(r"^```(?:\w+)?\s*\n(.*?)```\s*$", stripped, re.DOTALL)
    if m:
        return m.group(1).strip()
    # If starts with ``` but no clean match, strip manually
    if stripped.startswith("```"):
        # Remove opening fence line
        first_newline = stripped.index("\n") if "\n" in stripped else len(stripped)
        content = stripped[first_newline + 1:]
        # Remove trailing ```
        if content.rstrip().endswith("```"):
            content = content.rstrip()[:-3].rstrip()
        return content.strip()
    # Try --- front matter (DESIGN.md with YAML)
    if stripped.startswith("---"):
        return stripped
    return stripped


def generate_style(client: OpenAI, config: dict, seed: dict) -> dict:
    """
    Full generation pipeline for one style seed.
    Returns dict with status, design_md, html, scores, iterations.
    """
    result = {
        "seed_id": seed["id"],
        "seed_name": seed["name"],
        "status": "failed",
        "design_md": None,
        "html": None,
        "scores": None,
        "iterations": 0,
        "log": [],
    }

    max_iter = config["scoring"]["max_iterations"]
    target = config["scoring"]["eight_dim_max"]

    # Step 1: Generate DESIGN.md
    print(f"[{seed['id']}] Generating DESIGN.md...")
    design_prompt = build_design_md_prompt(seed)
    design_raw = call_llm(client, config, SYSTEM_PROMPT, design_prompt)
    if not design_raw:
        result["log"].append("DESIGN.md generation failed (LLM error)")
        return result

    design_md = extract_code_block(design_raw)
    result["design_md"] = design_md
    result["log"].append(f"DESIGN.md generated ({len(design_md)} chars)")

    # Step 2: Generate reference HTML (with iteration)
    for attempt in range(1, max_iter + 1):
        result["iterations"] = attempt
        print(f"[{seed['id']}] Generating reference HTML (attempt {attempt}/{max_iter})...")

        html_prompt = build_reference_html_prompt(seed, design_md)
        # On retry, add feedback from previous score
        if result["scores"] and attempt > 1:
            failing = [k for k, v in result["scores"].items() if k != "total" and v > 0]
            html_prompt += f"""

PREVIOUS ATTEMPT scored {result['scores']['total']}/16 on the 8-dim anti-AI rubric.
Failing dimensions: {', '.join(failing)}.
You MUST fix these. Here is what each failing dimension means:
{chr(10).join(f'- {k}: {DIMENSIONS.get(k, "unknown")}' for k in failing)}

This is attempt {attempt} of {max_iter}. You MUST pass this time."""

        html_raw = call_llm(client, config, SYSTEM_PROMPT, html_prompt)
        if not html_raw:
            result["log"].append(f"HTML generation attempt {attempt} failed (LLM error)")
            continue

        html = extract_code_block(html_raw)
        result["html"] = html

        # Step 3: Score
        scores = score_html(html)
        result["scores"] = scores
        result["log"].append(
            f"Attempt {attempt}: {scores['total']}/16 "
            f"({', '.join(f'{k}={v}' for k, v in scores.items() if k != 'total' and v > 0) or 'all clean'})"
        )

        if scores["total"] <= target:
            result["status"] = "validated"
            result["log"].append(f"PASSED on attempt {attempt}")
            print(f"[{seed['id']}] PASSED: {scores['total']}/16 (attempt {attempt})")
            return result

        print(f"[{seed['id']}] Score: {scores['total']}/16 — need ≤{target}, retrying...")

    result["log"].append(f"FAILED after {max_iter} attempts (best: {result['scores']['total']}/16)")
    print(f"[{seed['id']}] FAILED after {max_iter} attempts: {result['scores']['total']}/16")
    return result


def save_result(result: dict, output_dir: Path):
    """Save a generation result to the styles directory."""
    style_dir = output_dir / result["seed_id"]
    style_dir.mkdir(parents=True, exist_ok=True)

    if result["design_md"]:
        (style_dir / "DESIGN.md").write_text(result["design_md"])
    if result["html"]:
        (style_dir / "reference.html").write_text(result["html"])

    metadata = {
        "id": result["seed_id"],
        "name": result["seed_name"],
        "status": result["status"],
        "scores": result["scores"],
        "iterations": result["iterations"],
        "log": result["log"],
    }
    (style_dir / "metadata.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False))

    return style_dir
