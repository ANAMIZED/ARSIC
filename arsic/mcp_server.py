"""ARSIC MCP-style stdio server (stdlib JSON-RPC).

Exposes ARSIC tools over stdin/stdout for agent hosts.

Run:
    python -m arsic.mcp_server

Tools: arsic_demo, arsic_verify, arsic_health, arsic_selftest
"""
from __future__ import annotations

import json
import sys
import traceback
from typing import Any


TOOLS = [
    {
        "name": "arsic_demo",
        "description": "Run a short paper-only demo cycle (stdlib, no network).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "root": {"type": "string", "default": "run_mcp"},
                "days": {"type": "integer", "default": 3},
                "seed": {"type": "integer", "default": 7},
            },
        },
    },
    {
        "name": "arsic_verify",
        "description": "Re-verify the hash-chained audit log under root.",
        "inputSchema": {
            "type": "object",
            "properties": {"root": {"type": "string", "default": "run_mcp"}},
        },
    },
    {
        "name": "arsic_selftest",
        "description": "Run the core unittest suite (discover tests/).",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "arsic_health",
        "description": "Return package version and paper-only invariant note.",
        "inputSchema": {"type": "object", "properties": {}},
    },
]


def _ok(id_: Any, result: Any) -> dict:
    return {"jsonrpc": "2.0", "id": id_, "result": result}


def _err(id_: Any, code: int, message: str) -> dict:
    return {"jsonrpc": "2.0", "id": id_, "error": {"code": code, "message": message}}


def handle_tools_list(id_: Any) -> dict:
    return _ok(id_, {"tools": TOOLS})


def handle_tools_call(id_: Any, params: dict) -> dict:
    name = params.get("name") or params.get("tool")
    args = params.get("arguments") or params.get("args") or {}
    try:
        if name == "arsic_health":
            from arsic import __version__
            return _ok(id_, {
                "version": __version__,
                "paper_only": True,
                "note": "L3 never granted; live orders structurally rejected",
            })
        if name == "arsic_selftest":
            import unittest
            loader = unittest.TestLoader()
            suite = loader.discover("tests")
            result = unittest.TextTestRunner(verbosity=0).run(suite)
            return _ok(id_, {
                "ran": result.testsRun,
                "failures": len(result.failures),
                "errors": len(result.errors),
                "ok": result.wasSuccessful(),
            })
        if name == "arsic_demo":
            from arsic.cli import main as cli_main
            root = str(args.get("root", "run_mcp"))
            days = int(args.get("days", 3))
            seed = int(args.get("seed", 7))
            import sys as _sys
            old = _sys.argv
            try:
                _sys.argv = ["arsic", "demo", "--root", root, "--days", str(days), "--seed", str(seed)]
                try:
                    cli_main()
                except SystemExit as e:
                    if e.code not in (0, None):
                        raise
            finally:
                _sys.argv = old
            return _ok(id_, {"root": root, "days": days, "seed": seed, "status": "completed"})
        if name == "arsic_verify":
            from arsic.cli import main as cli_main
            root = str(args.get("root", "run_mcp"))
            import sys as _sys
            old = _sys.argv
            try:
                _sys.argv = ["arsic", "verify", "--root", root]
                try:
                    cli_main()
                except SystemExit as e:
                    if e.code not in (0, None):
                        raise
            finally:
                _sys.argv = old
            return _ok(id_, {"root": root, "status": "verified"})
        return _err(id_, -32601, f"unknown tool: {name}")
    except Exception as e:
        return _err(id_, -32000, f"{type(e).__name__}: {e}\n{traceback.format_exc()}")


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        id_ = msg.get("id")
        method = msg.get("method", "")
        params = msg.get("params") or {}
        if method in ("tools/list", "list_tools"):
            out = handle_tools_list(id_)
        elif method in ("tools/call", "call_tool"):
            out = handle_tools_call(id_, params)
        elif method == "initialize":
            out = _ok(id_, {
                "protocolVersion": "2024-11-05",
                "serverInfo": {"name": "arsic", "version": "1.0.0"},
                "capabilities": {"tools": {}},
            })
        else:
            out = _err(id_, -32601, f"method not found: {method}")
        sys.stdout.write(json.dumps(out) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
