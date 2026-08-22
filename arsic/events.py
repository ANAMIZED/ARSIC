"""ARSIC persistence layer (spec S3 Audit Surface, S6 Audit Everything, S7 Persistence).

- EventLog: append-only, hash-chained JSONL. Every Patch / decision / harness diff
  is an event; tampering is detectable via verify().
- ObjectStore: content-addressed versioned object store (sha256 keyed).
- ExperimentTracker: local stand-in for W&B-style experiment tracking (S7).
"""
from __future__ import annotations

import hashlib
import json
import os
import time
from dataclasses import dataclass, asdict
from typing import Any, Iterable, Optional

GENESIS = "GENESIS"


def canon(obj: Any) -> str:
    """Canonical JSON used for all hashing (deterministic)."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=_default)


def _default(o: Any):
    if isinstance(o, set):
        return sorted(o)
    if hasattr(o, "__dict__"):
        return o.__dict__
    return str(o)


def sha(obj: Any) -> str:
    return hashlib.sha256(canon(obj).encode()).hexdigest()


@dataclass
class Event:
    seq: int
    ts: float
    kind: str
    actor: str
    payload: dict
    prev: str
    hash: str = ""

    def body(self) -> dict:
        return {"seq": self.seq, "ts": self.ts, "kind": self.kind,
                "actor": self.actor, "payload": self.payload, "prev": self.prev}


class EventLog:
    """Append-only hash chain. h_i = sha256(prev_hash + canon(body_i))."""

    def __init__(self, path: str):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self._seq = 0
        self._last = GENESIS
        if os.path.exists(path):
            for ev in self.all():
                self._seq = ev.seq + 1
                self._last = ev.hash

    def append(self, kind: str, payload: dict, actor: str = "system") -> Event:
        ev = Event(seq=self._seq, ts=time.time(), kind=kind, actor=actor,
                   payload=payload, prev=self._last)
        ev.hash = hashlib.sha256((ev.prev + canon(ev.body())).encode()).hexdigest()
        with open(self.path, "a") as f:
            f.write(canon(asdict(ev)) + "\n")
        self._seq += 1
        self._last = ev.hash
        return ev

    def all(self) -> Iterable[Event]:
        if not os.path.exists(self.path):
            return []
        out = []
        with open(self.path) as f:
            for line in f:
                if line.strip():
                    out.append(Event(**json.loads(line)))
        return out

    def tail(self, n: int = 20):
        evs = list(self.all())
        return evs[-n:]

    def verify(self) -> tuple[bool, Optional[int]]:
        """Recompute the chain; return (ok, first_bad_seq)."""
        prev = GENESIS
        for ev in self.all():
            expect = hashlib.sha256((prev + canon(ev.body())).encode()).hexdigest()
            if ev.prev != prev or ev.hash != expect:
                return False, ev.seq
            prev = ev.hash
        return True, None

    def count(self, kind: Optional[str] = None) -> int:
        return sum(1 for e in self.all() if kind is None or e.kind == kind)
