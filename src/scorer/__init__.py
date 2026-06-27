"""
Anti-AI Style Factory — 8-Dimension Scorer
===========================================
Scores HTML against the AI-taste rubric. Pure Python, no deps.

The implementation lives in :mod:`src.scorer.eight_dim`; this module re-exports
the public surface so consumers can `from src.scorer import score_html`.

Re-exports are lazy (PEP 562) so that running `python -m src.scorer.eight_dim`
does not trigger a double import of the module.
"""

__all__ = [
    "score_html",
    "score_file",
    "DIMENSIONS",
    "CLICHE_FONTS",
    "PURPLE_GRAD_COLORS",
    "MARKETING_STEMS",
]


def __getattr__(name: str):
    if name in __all__:
        from src.scorer import eight_dim

        return getattr(eight_dim, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
