# Skill: Harness Co-Evolution

## Purpose
Outer improvement loop: propose harness diffs → lint against contract → run sibling sandboxes on held-out regimes → promote only on statistical significance (paired sign-flip) with no regime regression.

## Entry points
- `arsic/improve.py` — `HarnessEvolution.epoch(...)`
- META tickets for acceptance-criteria changes
- Console: Evolve tab

## Invariants
- Evaluator is frozen during A/B
- Promotions versioned in git harness repo when available
- Verified sibling trajectories only feed adapter updates (bounded)

## Related
- `arsic/evaluate.py` — frozen evaluator, selective erasure
- `arsic/llm.py` — DeterministicCore / ProviderCore seam
