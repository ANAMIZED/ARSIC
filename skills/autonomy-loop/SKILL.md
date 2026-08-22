# Skill: Autonomy Loop (S10)

## Purpose
Close the knowledge → improvement loop: scan wiki gaps → gather via governed agents → mine improvement candidates with evidence cids → evolution epochs on a cadence.

## Entry points
- `POST /api/auto/tick` (server)
- Console: **Autonomy loop** button
- `arsic/autonomy.py`

## Envelope
- SKILL promotions may auto-execute
- POLICY / ADAPTER still queue for human keys
- Standing human approval can transfer to identical re-proposal (audited)
- Breaker trip halts the loop until human reset

## Safety
Autonomy level advances only via approved META tickets. L3 (live-eligible) is never granted in this reference build.
