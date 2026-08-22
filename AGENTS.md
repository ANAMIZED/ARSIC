# AGENTS.md — Coding-Agent Contract for ARSIC

This document is the binding contract for any coding agent (human or automated) working in this repository.

## Non-negotiable invariants

1. **Paper-only.** Never introduce live-exchange credentials, live order paths, or any code path that can place real capital without an explicit, human-minted governance token *and* autonomy level L3. L3 is never granted in the reference build.
2. **Governance is external.** Agents may *file* tickets. Approvals for POLICY / ADAPTER / META levels require the human role. Do not auto-approve or forge human tokens.
3. **Audit everything.** Every privileged action, patch, freeze, promotion, and kill-switch event must land in the hash-chained `EventLog`. Do not bypass `audit.append`.
4. **Determinism preferred.** Seeded markets, frozen evaluators, and reproducible e2e runs are first-class. Prefer pure functions and explicit state over hidden globals.
5. **No network in core tests.** The 66 core tests must run with stdlib only and no network egress.
6. **Preserve the privilege ladder.** `OUTPUT < MEMORY < SKILL < POLICY < ADAPTER < META`. SKILL may auto-execute; higher levels stay gated.

## Preferred change process

1. File a ticket via `Governance.request(...)` (or the CLI / console equivalent).
2. For POLICY+, obtain human approval.
3. Apply only through the governed channels (`HarnessEvolution`, `MetaQueue`, etc.).
4. Re-run the relevant test suite and `python -m arsic verify`.
5. Update `docs/COMPLIANCE_MATRIX.md` if a new requirement or substitution is introduced.

## What an agent may do freely

- Add unit tests that strengthen existing invariants.
- Improve documentation, comments, and type hints.
- Refactor pure math or pure data structures behind the same interfaces.
- Export additional training JSONL or dashboard views that remain offline.

## What an agent must never do

- Mint or hard-code human tokens.
- Disable the live-trade rejection path.
- Remove or weaken the kill-switch / freeze hooks.
- Commit real API keys, secrets, or venue credentials.
- Claim live trading readiness.

## Surfaces an agent should know

- `arsic/governance.py` — contracts, tickets, kill-switch, scopes
- `arsic/events.py` — hash-chained audit log
- `arsic/improve.py` — harness co-evolution + sign-flip tests
- `arsic/trading.py` + `execution_l3.py` — paper gateway + L3 seams
- `tests/` — the contract is enforced here
- `docs/COMPLIANCE_MATRIX.md` — the living map of the specification

Fail closed. Prefer a clear error over a silent success that violates an invariant.
