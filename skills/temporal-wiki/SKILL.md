# Skill: Temporal Knowledge Wiki

## Purpose
Shared memory for the constellation: temporal KG with provenance, confidence, TTL invalidation, surgical merges, compiled pages, and Experience Graph trajectories.

## Entry points
- `arsic/wiki.py`, `arsic/exg.py`
- Agents read via wiki-compiled stats, not raw firehose
- Nightly curator rebuild + surgical on-change compile

## Patch outcomes
Insert / merge / relate / conflict (arbiter queue) / reject — all audited.

## Verification
`tests/test_wiki.py` covers all five patch outcomes, TTL, surgical isolation, provenance trace.
