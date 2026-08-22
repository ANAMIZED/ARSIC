# ARSIC — Autonomous Recursive Self-Improving Knowledge Wiki Constellation OS

Reference implementation of the ARSIC blueprint: a governed multi-agent
runtime whose trading instantiation runs **paper-only** market-neutral
funding / basis / RWA arbitrage research, with a temporal-knowledge-graph
wiki as shared memory, four nested self-improvement loops, and a
governance plane that keeps every privileged change behind a human gate.

**This is research / simulation tooling.** It never touches live venues:
the execution gateway structurally rejects live orders without a
governance-minted human token *and* autonomy level L3 (never granted in
this build). Nothing here is financial advice.

## Quick start

```bash
python3 -m unittest discover -s tests   # 66 tests, stdlib only
python3 -m arsic demo --root run --days 30
python3 -m arsic verify --root run      # re-verify the audit hash chain
```

Python ≥ 3.10, standard library only. `git` is used if available for the
harness repo (falls back to a plain versioned file).

Outputs of a demo run land in `run/`:
`reports/RUN_REPORT.md` (full transcript + daily table),
`reports/dashboard.html` (static offline ops console),
`reports/training_data/` (sft/pref/critic JSONL from verified sibling
trajectories), `harness_repo/` (git-versioned harness), and
`state/audit.jsonl` (hash-chained audit log).

## Architecture ↔ spec map

See the full COMPLIANCE_MATRIX.md and AUDIT_REPORT.md in this repository for the complete mapping and verification results.

The original package is preserved without modification.
