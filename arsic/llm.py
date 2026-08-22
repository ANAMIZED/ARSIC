"""ARSIC LLM seam (S5). DeterministicCore stands in for offline; ProviderCore is the live seam."""
from __future__ import annotations

from typing import Any, Optional


class DeterministicCore:
    """Rule engine that responds to prompt directives so prompt diffs change behavior."""
    def __init__(self, seed: int = 0):
        self.seed = seed

    def complete(self, prompt: str, **kwargs) -> str:
        # Minimal deterministic stand-in: echo key directives
        out = []
        if "[[EXTREME_DISCOUNT]]" in prompt:
            out.append("extreme_discount=0.7")
        if "funding" in prompt.lower():
            out.append("funding_persistence=observed")
        if "basis" in prompt.lower():
            out.append("basis_gap=present")
        return " | ".join(out) if out else "noop"


class ProviderCore:
    """Live LLM provider seam — raises offline in this reference build."""
    def complete(self, prompt: str, **kwargs) -> str:
        raise RuntimeError("ProviderCore offline: no network / API key in reference build")


def bounded_adapter_update(params: dict, signals: list, clamp: float = 0.15) -> dict:
    """Bounded parameter distillation from verified trajectories (S5)."""
    out = dict(params)
    if not signals:
        return out
    # Very small deterministic update for the reference implementation
    for k in ("risk_aversion", "extreme_discount"):
        if k in out:
            delta = 0.01 * (1 if signals else 0)
            out[k] = max(0.1, min(2.0, out[k] + delta))
            if abs(out[k] - params.get(k, out[k])) > clamp:
                out[k] = params[k] + (clamp if out[k] > params[k] else -clamp)
    return out
