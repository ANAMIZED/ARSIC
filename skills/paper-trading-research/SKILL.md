# Skill: Paper Trading Research

## Purpose
Run market-neutral funding / basis / RWA arbitrage **research** in paper-only mode. Never place live capital.

## Entry points
- CLI: `python -m arsic demo --root run --days 30`
- API: `POST /api/...` via `python -m arsic serve`
- SDK: `from arsic.sdk import ArsicClient`

## Constraints (hard)
- `paper_only=True` on the system contract
- Live orders rejected without human token **and** autonomy L3 (L3 never granted in this build)
- Max drawdown / leverage / liq score from GoalContract

## Outputs
- `run/reports/RUN_REPORT.md`
- `run/state/audit.jsonl` (hash-chained)
- `run/reports/training_data/` (SFT / preference / critic JSONL)

## Verification
```bash
python -m unittest discover -s tests
python -m arsic verify --root run
```
