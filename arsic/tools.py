"""ARSIC tool plane — scoped tools with self-tests (S2)."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Optional


@dataclass
class Tool:
    name: str
    scope: str
    fn: Callable
    selftest: Optional[Callable] = None
    description: str = ""

    def call(self, *args, **kwargs):
        return self.fn(*args, **kwargs)


class ToolRegistry:
    def __init__(self):
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool):
        self._tools[tool.name] = tool

    def get(self, name: str) -> Optional[Tool]:
        return self._tools.get(name)

    def call(self, name: str, scope: str, *args, **kwargs):
        t = self._tools.get(name)
        if t is None:
            raise KeyError(f"unknown tool: {name}")
        if t.scope != scope and scope != "*":
            raise PermissionError(f"tool {name} requires scope {t.scope}, got {scope}")
        return t.call(*args, **kwargs)

    def selftest_all(self) -> dict:
        results = {}
        for name, t in self._tools.items():
            if t.selftest:
                try:
                    results[name] = ("ok", t.selftest())
                except Exception as e:
                    results[name] = ("fail", str(e))
            else:
                results[name] = ("skip", None)
        return results
