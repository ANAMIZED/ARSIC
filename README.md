# ARSIC

[![CI](https://github.com/ANAMIZED/ARSIC/actions/workflows/ci.yml/badge.svg)](https://github.com/ANAMIZED/ARSIC/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-66%2B%20core%20passing-brightgreen.svg)](tests/)
[![CLI](https://img.shields.io/badge/CLI-arsic-orange.svg)](arsic/cli.py)
[![API](https://img.shields.io/badge/API-HTTP-009688.svg)](arsic/server.py)
[![SDK](https://img.shields.io/badge/SDK-Python-green.svg)](arsic/sdk.py)
[![MCP](https://img.shields.io/badge/MCP-server-purple.svg)](arsic/mcp_server.py)
[![Paper-only](https://img.shields.io/badge/trading-paper--only-success.svg)](#)
[![Governance](https://img.shields.io/badge/governance-human--gated-purple.svg)](arsic/governance.py)

**Autonomous Recursive Self-Improving Knowledge Wiki Constellation OS**

Reference implementation of a governed multi-agent runtime whose trading instantiation runs **paper-only** market-neutral funding / basis / RWA arbitrage research, with a temporal-knowledge-graph wiki as shared memory, four nested self-improvement loops, and a governance plane that keeps every privileged change behind a human gate.

**This is research / simulation tooling.** It never touches live venues: the execution gateway structurally rejects live orders without a governance-minted human token *and* autonomy level L3 (never granted in this build). Nothing here is financial advice.

## 🚀 Live Demo

[![Live Demo](https://img.shields.io/badge/%F0%9F%9A%80%20Live%20Demo-ARSIC%20Console-blue?style=for-the-badge)](https://ANAMIZED.github.io/ARSIC/ARSIC-4.html)

**Interactive offline-capable ops console** (fully self-contained single file) — governance, kill-switch, autonomy loop, harness evolution, audit chain, and paper trading dashboard.

→ [Open the live interactive demo](https://ANAMIZED.github.io/ARSIC/ARSIC-4.html)  
(or open `ARSIC-4.html` locally — works offline; auto-detects backend when `python -m arsic serve` is running)

---

A senior engineer who has never seen this repository can, using **only** the source and this `README.md`:

1. Run the full test suite (`python3 -m unittest discover -s tests`)
2. Execute a deterministic 30-day paper demo
3. Verify the hash-chained audit log end-to-end
4. Wire the HTML console to the live Python backend

**[Support Agentic Research Kernels ($99)](https://buy.stripe.com/bJecN63wObPv6Bf7Zm43S02)** · **[Agentic Research Cycle ($0.75)](https://buy.stripe.com/3cI14o8R8dXD3p3frO43S04)** · **[Public Goods Support](https://donate.stripe.com/00w5kE3wOg5L8Jn2F243S00)**

### Non-custodial USDC (preferred for agents)

| Network | Address | Explorer |
|---------|---------|----------|
| **Base** | `0xD3d0E9eDAe3Ac7bb199a8EAA761BdA423b878438` | [basescan](https://basescan.org/address/0xD3d0E9eDAe3Ac7bb199a8EAA761BdA423b878438) |
| **Ethereum** | `0xD3d0E9eDAe3Ac7bb199a8EAA761BdA423b878438` | [etherscan](https://etherscan.io/address/0xD3d0E9eDAe3Ac7bb199a8EAA761BdA423b878438) |
| **Solana** | `ETQwWf19axArsY493UfC6bxe2BmEzmzvCb58PPnC38A` | [solscan](https://solscan.io/account/ETQwWf19axArsY493UfC6bxe2BmEzmzvCb58PPnC38A) |

*Related:* [OpenMesha](https://github.com/ANAMIZED/OpenMesha) · [rui](https://github.com/ANAMIZED/rui) · [server-os](https://github.com/ANAMIZED/server-os)

## Surfaces

| Surface | Entry |
|---------|-------|
| **Live Demo (GitHub Pages)** | [ARSIC-4.html](https://ANAMIZED.github.io/ARSIC/ARSIC-4.html) |
| **Web control plane** | [`ARSIC-4.html`](ARSIC-4.html) (offline + remote) |
| REST / HTTP API | `python -m arsic serve --root run --port 8787` |
| CLI | `python -m arsic demo` / `verify` / `serve` / `sentinel` |
| MCP Server | `python -m arsic.mcp_server` (stdio JSON-RPC tools) |
| SDK | `from arsic.sdk import ArsicClient` |
| Multi-agent workflows | constellation + runtime (`arsic/constellation.py`, `arsic/runtime.py`) |
| Skills | [`skills/*/SKILL.md`](skills/) |
| Core package | `arsic/` (full tree inside [`arsic.zip`](arsic.zip) + extracted in CI) |
| Tests | `tests/` via `arsic.zip` extract (66+ core) |
| CI | [`.github/workflows/ci.yml`](.github/workflows/ci.yml) |
| AGENTS.md | Coding-agent contract at repo root |
| Spec compliance | [`docs/COMPLIANCE_MATRIX.md`](docs/COMPLIANCE_MATRIX.md) |
| Audit report | [`docs/AUDIT_REPORT.md`](docs/AUDIT_REPORT.md) |
| Original design notes | [`docs/ORIGINAL_README.md`](docs/ORIGINAL_README.md) |

## Quick Start

```bash
# Core invariants (stdlib only, no network)
python3 -m unittest discover -s tests   # 66+ core tests pass

# 30-day deterministic paper demo
python3 -m arsic demo --root run --days 30

# Re-verify the audit hash chain
python3 -m arsic verify --root run

# Live console + backend
python3 -m arsic serve --root run_srv --port 8787 --html ARSIC-4.html
# open http://127.0.0.1:8787/

# MCP stdio server
python -m arsic.mcp_server

# SDK
python -c "from arsic.sdk import ArsicClient; print(ArsicClient().health())"
```

Python ≥ 3.10, standard library only. `git` is used if available for the harness repo (falls back to a plain versioned file).

Outputs of a demo run land in `run/`:
`reports/RUN_REPORT.md`, `reports/dashboard.html`, `reports/training_data/` (SFT/pref/critic JSONL), `harness_repo/`, and `state/audit.jsonl` (hash-chained).

## Design principles

1. Least privilege by construction (privilege ladder + human gates for POLICY+)
2. Paper-only by structural rejection (gateway + autonomy L3 never granted)
3. Fail closed (named circuit breakers + independent sentinel)
4. Honest offline simulation (deterministic core, seeded regimes)
5. Every privileged change is audited and ticketed
6. Statistical rigor on self-improvement (sign-flip tests, frozen evaluators)

## Architecture ↔ Spec Map

| Spec plane | Module(s) |
|---|---|
| S3 Knowledge Wiki substrate | `arsic/wiki.py`, `arsic/exg.py`, `arsic/events.py` |
| S2/S4 Constellation runtime | `arsic/runtime.py`, `arsic/tools.py`, `arsic/constellation.py` |
| S2 Perception & tool plane | `arsic/perception.py` |
| S4 Execution & risk | `arsic/trading.py`, `arsic/strategy_math.py` |
| S5 Recursive improvement | `arsic/improve.py`, `arsic/evaluate.py`, `arsic/llm.py` |
| S6 Governance & safety | `arsic/governance.py` |
| S7 Stack | `arsic/improve.py`, `arsic/events.py` |
| S8 Bootstrap + daily cycle | `arsic/bootstrap.py`, `arsic/cycle.py` |
| S9 Metrics & invariants | audit report + test suite |
| S10 Autonomy loop | `arsic/autonomy.py` |
| L3 execution + sentinel | `arsic/execution_l3.py`, `arsic/sentinel.py`, `arsic/venue_*.py` |

Full mapping and status: [`docs/COMPLIANCE_MATRIX.md`](docs/COMPLIANCE_MATRIX.md)

## Verification

```bash
python3 -m unittest discover -s tests
python3 -m arsic verify --root run   # after a demo
```

Core 66 tests (events, governance, wiki, runtime, trading, improve, evaluate, e2e) are deterministic and pass with stdlib only. Additional suites exercise L3 mandates, external venue routing, and the independent sentinel process.

## License

Apache-2.0

---

*Original package artifacts are preserved without modification. Surfaces (SDK, MCP, Skills, badges) expose what ARSIC already provides — they do not invent live-trading or network capabilities.*
