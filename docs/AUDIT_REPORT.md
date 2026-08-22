# ARSIC Audit Report

Scope: full build audit of the ARSIC reference implementation — unit and
end-to-end tests, a 30-day demo run, audit-chain verification, and the
spec-S9 invariants checklist. All numbers below are taken directly from
the actual run (`run/reports/RUN_REPORT.md`, `run/state/audit.jsonl`);
nothing is estimated.

## 1. Test suite

`python3 -m unittest discover -s tests` → **66 tests, 66 passed, 0 failed**
across 8 suites: events (hash chain + tamper detection), governance
(human-only approvals, freeze semantics, kill-switch rules, scope router,
contract lint), wiki (all five patch outcomes, arbiter queue, TTL
invalidation, surgical merge isolation, provenance trace), runtime/tools
(scope refusal + handoff, quota suspension, recursive spawn/report-up,
contract-tamper rejection, tool selftest gate, scope-denied calls),
trading (funding accrual sign, sizing caps, liquidation levels, frozen
gateway, live-trade rejection), improve (exact sign-flip p-values,
lint screen, unapproved-POLICY block, end-to-end promotion, verified-only
adapter fit with clamp, frozen-evaluator assertion, git commits), evaluate
(frozen immutability, ground-truth gate, selective erasure), and e2e
(deterministic 6-day system run, audit chain, zero live trades, dashboard
render).

Two real defects were found and fixed by the tests during this audit:
(1) `Harness.apply_diff` crashed on bare `topology` diff keys;
(2) the OI-spike circuit breaker false-positived during statistical warm-up
— it now z-scores one-step OI returns with a ≥7-observation warm-up.

## 2. Demo run verification (seed 7, 30 days)

Paper phase (L0): final equity 987,937 (pnl −12,063), 33 closed positions,
fp 3.0%, gross funding capture 37.3%, maxDD 2.07%. One organic kill-switch
trip analyzed and reset. Compounding on fresh world (seed 8): gap-to-oracle
closed +4.7% of the oracle bound across harness epochs.

## 3. Invariants checklist

audit_chain_ok **True** · live_trades **0** · policy_plus_applied_all_human
**True** · evaluator_frozen **True** · conflicts_awaiting_arbiter **0**.

## 4. Known limitations

Synthetic seeded market data; deterministic rule engine in the LLM slot;
sandbox isolation is directory/process-level; adapter fitting distills
parameters; single-process. Each substitution is itemised in
`COMPLIANCE_MATRIX.md`.

**Conclusion:** architecture, improvement loops, and governance gates
S1–S9 are implemented, exercised end-to-end, and covered by passing tests.
This system is paper-trading research tooling and is not suitable for live
capital without real market infrastructure, real-data validation, and
independent review.
