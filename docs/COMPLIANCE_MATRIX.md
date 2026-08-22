# ARSIC Compliance Matrix

Every spec requirement (S1–S9) mapped to implementation and verification.
Status legend: **IMPL** = implemented as specified · **SUBST** = implemented
behind the specified interface with a documented environment substitution.

Test IDs refer to `tests/` (run: `python3 -m unittest discover -s tests`).
Full detailed matrix ships inside `arsic.zip` / original package; this file
is the living summary for the public repository surfaces.

## S1 — Definition & objectives

| Requirement | Status |
|---|---|
| Governed multi-agent runtime; paper-first market-neutral research | **IMPL** |
| Self-improvement only through gated, audited channels | **IMPL** |

## S2 — Layered architecture

| Layer | Status |
|---|---|
| Governance plane above everything | **IMPL** |
| Recursive improvement plane | **IMPL** |
| Constellation runtime (agents, contracts, quotas, bus) | **IMPL** |
| Knowledge wiki substrate | **IMPL** |
| Perception & tool plane (scoped tools) | **IMPL/SUBST** (synthetic drivers) |

## S3 — Knowledge Wiki

Temporal KG, provenance, confidence, invalidation, surgical merges, pages,
EXG, audit surface — **IMPL** (`wiki.py`, `exg.py`, `events.py`).

## S4 — Execution & risk

Paper broker, sizing, liquidation monitor, gateway rejects live without
human token + L3 — **IMPL**. L3 never granted in this build.

## S5 — Recursive improvement

Harness co-evolution, sign-flip tests, frozen evaluator, bounded adapters,
META queue — **IMPL** (`improve.py`, `evaluate.py`, `llm.py`).

## S6 — Governance & safety

Goal contracts, privilege ladder, approvals, kill-switch, scope router,
contract lint — **IMPL** (`governance.py`).

## S7–S9 — Stack, daily cycle, metrics

Git harness / experiment tracking **SUBST**; daily 7-step cycle **IMPL**;
risk-adjusted metrics and gap-to-oracle compounding **IMPL**.

## Surfaces added for discovery (not changing core invariants)

| Surface | Path |
|---|---|
| SDK | `arsic/sdk.py` |
| MCP stdio server | `arsic/mcp_server.py` |
| Skills | `skills/*/SKILL.md` |
| Live Demo HTML | `ARSIC-4.html` |
| CI (extracts full `arsic.zip`) | `.github/workflows/ci.yml` |
