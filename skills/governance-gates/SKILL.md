# Skill: Governance Gates

## Purpose
Keep every privileged change behind the human gate. Privilege ladder:

`OUTPUT < MEMORY < SKILL < POLICY < ADAPTER < META`

## Rules
- SKILL and below may auto-execute when approved by policy threshold
- POLICY / ADAPTER / META require the **human** role
- Human tokens are minted only by `Governance.human_token` (HMAC)
- Kill-switch freezes the scheduler; independent sentinel can flatten risk

## Entry points
- Tickets: `Governance.request(level, title, payload, actor)`
- Approve: human role only for POLICY+
- Console: governance tab in `ARSIC.html`
- CLI / API governance endpoints when server is running

## Never
- Forge human tokens
- Auto-approve POLICY+
- Disable the live-trade rejection path
