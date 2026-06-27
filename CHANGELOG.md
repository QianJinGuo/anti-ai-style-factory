# Changelog

All notable changes to this project will be documented in this file.

## [0.3.0] — 2026-06-27

### Added
- English README.md + Chinese README_zh.md
- Comprehensive test suite (62 tests covering all 8 scorer dimensions)
- GitHub Actions CI (pytest, lint, scorer self-test)
- CONTRIBUTING.md
- CHANGELOG.md
- .env.example template
- sample_styles/ with 10 curated examples
- gallery/ web-based preview and scorer UI
- scripts/ for gallery building and seed generation

### Fixed
- Font scorer now correctly detects multi-word AI fonts (Open Sans, Helvetica Neue)

### Changed
- API key resolution: env var + .env file (removed ~/.zshenv and ~/.hermes dependency)
- Default LLM provider: openai (was xfyun)
- Default model: gpt-4o-mini (was xopqwen36v35b)
- styles/ removed from git (439MB) — users generate their own

## [0.2.0] — 2026-06-17

### Added
- pyproject.toml with CLI entry points (anti-ai-score, anti-ai-factory)
- Concurrent generation with --workers
- 55 design movement seeds across 6 tiers
- 8-dimension scorer with pass/fail gate
- LLM-powered style generation with auto-retry

## [0.1.0] — 2026-06-15

### Added
- Initial prototype
- Basic scorer (font, gradient, glassmorphism detection)
- Single-seed generation pipeline
