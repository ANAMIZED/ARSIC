#!/usr/bin/env bash
set -euo pipefail
echo "==> Core test suite"
python3 -m unittest discover -s tests
echo "==> Optional short demo + audit verify"
ROOT="${1:-/tmp/arsic_verify_$$}"
python3 -m arsic demo --root "$ROOT" --days 2 --seed 7
python3 -m arsic verify --root "$ROOT"
echo "==> OK"
