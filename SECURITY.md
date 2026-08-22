# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.x     | Yes       |

## Reporting a Vulnerability

Please open a private security advisory on GitHub or contact the maintainer directly. Do not file public issues for vulnerabilities that could affect the paper-trading gateway, governance token minting, or audit chain integrity.

## Hard invariants (non-negotiable)

- Live trade paths must remain rejected without a genuine human token + L3.
- Human tokens are minted only by `Governance.human_token` and verified with constant-time compare.
- The audit log is append-only and hash-chained; any break is detectable by `EventLog.verify()`.
- The independent sentinel process holds only cancel-scope credentials.

## Scope

This repository is research / simulation tooling. It is not a production trading system. Any deployment that places real capital is outside the supported scope and requires independent review, real market infrastructure, and legal compliance.
