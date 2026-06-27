# Contributing to Anti-AI Style Factory

Thanks for your interest in contributing! Here's how to get involved.

## Ways to Contribute

### 1. Add a New Design Movement Seed

The seed catalog (`catalog/SEEDS.md`) is the heart of the project. To add a new movement:

1. Research the movement: era, region, core principles, visual characteristics
2. Add a row to the appropriate tier table in `catalog/SEEDS.md`
3. The ID should be lowercase, hyphenated (e.g., `art-nouveau`, `pixel-art`)
4. The "anti-AI signal" column should describe what makes this movement distinctly NOT AI-looking

**What makes a good seed:**
- Based on a real, documented design movement or visual tradition
- Has clear, distinctive visual characteristics that differ from AI defaults
- Can be expressed as concrete CSS/typography choices

### 2. Improve the Scorer Rubric

The 8-dimension scorer (`src/scorer/eight_dim.py`) is pure Python with zero dependencies. To add or modify dimensions:

1. Open an issue first to discuss the proposed change
2. Add test cases in `tests/test_scorer.py`
3. Implement the change
4. Ensure all existing tests still pass

**Guidelines for new dimensions:**
- Must be detectable via regex/string analysis (no browser rendering)
- Must have a clear "AI taste" signal vs "human design" signal
- Score range: 0-2 per dimension

### 3. Submit Generated Styles

If you've generated styles that pass the rubric (≤ 4/16), you can submit them as samples:

1. Run `anti-ai-factory --seed <your-seed>`
2. Verify: `anti-ai-score styles/<your-seed>/reference.html`
3. Submit a PR with the `styles/<seed>/` directory

### 4. Improve Documentation

Fix typos, add examples, translate to other languages — all welcome.

## Development Setup

```bash
# Clone and install
git clone https://github.com/anthropics/anti-ai-style-factory.git
cd anti-ai-style-factory
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Run linter
ruff check .
ruff format --check .
```

## Code Style

- Python 3.9+ compatible
- Type hints on public functions
- Docstrings on public modules, classes, and functions
- Tests for any scorer changes

## Pull Request Process

1. Fork the repo
2. Create a feature branch (`git checkout -b add-movement-xyz`)
3. Make your changes
4. Run `pytest tests/ -v` — all tests must pass
5. Submit a PR with a clear description

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
