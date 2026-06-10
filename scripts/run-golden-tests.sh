#!/bin/sh
set -eu

ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"

python3 "$ROOT/skills/scripts/khub-validate.py" line-endings "$ROOT/skills"

bash "$ROOT/skills/khub-classifier-router/scripts/validate-route-plan.sh" \
  "$ROOT/skills/khub-classifier-router/examples/output-route-plan.create.yaml"
bash "$ROOT/skills/khub-classifier-router/scripts/validate-route-plan.sh" \
  "$ROOT/skills/khub-classifier-router/examples/output-route-plan.append.yaml"
bash "$ROOT/skills/khub-classifier-router/scripts/validate-route-plan.sh" \
  "$ROOT/skills/khub-classifier-router/examples/output-decision-report.no-fit.md"
bash "$ROOT/skills/khub-classifier-router/scripts/validate-route-plan.sh" \
  "$ROOT/skills/khub-classifier-router/examples/output-decision-report.needs-human.md"
bash "$ROOT/skills/khub-classifier-router/scripts/validate-route-plan.sh" \
  "$ROOT/skills/khub-classifier-router/examples/output-decision-report.skip-duplicate.yaml"

bash "$ROOT/skills/khub-deposition-update/scripts/validate-note-payload.sh" \
  "$ROOT/skills/khub-deposition-update/examples/note-payload.seed.yaml"
bash "$ROOT/skills/khub-deposition-update/scripts/validate-execution-report.sh" \
  "$ROOT/skills/khub-deposition-update/examples/create-seed.md"
bash "$ROOT/skills/khub-deposition-update/scripts/validate-execution-report.sh" \
  "$ROOT/skills/khub-deposition-update/examples/blocked-report.md"
bash "$ROOT/skills/khub-deposition-update/scripts/validate-execution-report.sh" \
  "$ROOT/skills/khub-deposition-update/examples/conflict-report.md"

python3 - <<'PY' "$ROOT"
import csv
import pathlib
import re
import sys

root = pathlib.Path(sys.argv[1])
errors = []
for csv_path in root.glob("skills/*/evals/trigger-prompts.csv"):
    with csv_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows or list(rows[0].keys()) != ["id", "should_trigger", "prompt", "expected_evidence"]:
        errors.append(f"{csv_path}: bad trigger eval header")
    for row in rows:
        if row.get("should_trigger") not in {"true", "false"}:
            errors.append(f"{csv_path}: invalid should_trigger in {row.get('id')}")

for md in root.glob("skills/*/SKILL.md"):
    text = md.read_text(encoding="utf-8")
    for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if "://" in link or link.startswith("#"):
            continue
        if not (md.parent / link).resolve().exists():
            errors.append(f"{md}: broken link {link}")

if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)
print("trigger evals and markdown links ok")
PY

echo "golden tests ok"
