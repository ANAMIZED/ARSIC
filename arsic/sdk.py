"""ARSIC Python SDK — thin client over the HTTP control plane and local package.

Usage:
    from arsic.sdk import ArsicClient
    c = ArsicClient("http://127.0.0.1:8787")
    print(c.health())
    print(c.audit_tail(20))
"""
from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any, Optional


class ArsicClient:
    """HTTP client for `python -m arsic serve`."""

    def __init__(self, base_url: str = "http://127.0.0.1:8787", timeout: float = 30.0):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _req(self, method: str, path: str, body: Optional[dict] = None) -> Any:
        url = f"{self.base_url}{path}"
        data = None
        headers = {"Accept": "application/json"}
        if body is not None:
            data = json.dumps(body).encode()
            headers["Content-Type"] = "application/json"
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                raw = resp.read().decode()
                return json.loads(raw) if raw else None
        except urllib.error.HTTPError as e:
            detail = e.read().decode() if e.fp else str(e)
            raise RuntimeError(f"ARSIC API {method} {path} → {e.code}: {detail}") from e

    def health(self) -> dict:
        return self._req("GET", "/api/health")

    def audit_tail(self, n: int = 20) -> list:
        return self._req("GET", f"/api/audit/tail?n={n}") or []

    def selftest(self) -> dict:
        return self._req("POST", "/api/selftest", {})

    def auto_tick(self) -> dict:
        return self._req("POST", "/api/auto/tick", {})

    def tickets(self) -> list:
        return self._req("GET", "/api/tickets") or []

    def approve(self, tid: str, actor: str = "human:sdk") -> dict:
        return self._req("POST", f"/api/tickets/{tid}/approve", {"actor": actor, "role": "human"})

    def reject(self, tid: str, actor: str = "human:sdk") -> dict:
        return self._req("POST", f"/api/tickets/{tid}/reject", {"actor": actor, "role": "human"})


__all__ = ["ArsicClient"]
