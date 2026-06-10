#!/bin/sh
set -eu

DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
VALIDATOR="$DIR/../../scripts/khub-validate.py"
INPUT="${1:-}"

if [ -n "$INPUT" ]; then
  python3 "$VALIDATOR" report "$INPUT"
else
  python3 "$VALIDATOR" report
fi
