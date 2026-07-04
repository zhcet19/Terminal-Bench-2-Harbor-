#!/bin/bash
set -uo pipefail

VERIFIER_DIR="/logs/verifier"
mkdir -p "$VERIFIER_DIR"

pytest /tests/test_outputs.py \
  --json-ctrf "$VERIFIER_DIR/ctrf.json" \
  -rA
result=$?

if [ $result -eq 0 ]; then
  echo 1 > "$VERIFIER_DIR/reward.txt"
else
  echo 0 > "$VERIFIER_DIR/reward.txt"
fi

exit 0
