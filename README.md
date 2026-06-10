# Codex Skills

Public Codex skill collection for reusable agent workflows.

## Skills

- `flomo-daily-intake`: collect raw Flomo notes for a specific day or time range before routing or deposition.
- `khub-classifier-router`: classify intake material and produce a route plan before writing KHub notes.
- `khub-deposition-update`: create or append Obsidian KHub notes from validated route plans.

Shared workflow guidance lives in `skills/workflow-principles.md`.

## Layout

```text
skills/
  flomo-daily-intake/
  khub-classifier-router/
  khub-deposition-update/
  workflow-principles.md
```

Each skill directory contains a `SKILL.md` entry point. Some skills also include contracts, templates, examples, references, validation scripts, and trigger evals.

## Install

Copy the desired skill directories into your Codex skills directory:

```bash
mkdir -p "$CODEX_HOME/skills"
cp -R skills/flomo-daily-intake "$CODEX_HOME/skills/"
cp -R skills/khub-classifier-router "$CODEX_HOME/skills/"
cp -R skills/khub-deposition-update "$CODEX_HOME/skills/"
```

Set `CODEX_HOME` to your local Codex configuration directory if it is not already defined.

## Validation

Run the full package check:

```bash
bash scripts/run-golden-tests.sh
```

Or run individual validators:

```bash
bash skills/khub-classifier-router/scripts/validate-route-plan.sh \
  skills/khub-classifier-router/examples/output-route-plan.create.yaml

bash skills/khub-deposition-update/scripts/validate-note-payload.sh \
  skills/khub-deposition-update/examples/note-payload.seed.yaml

bash skills/khub-deposition-update/scripts/validate-execution-report.sh \
  skills/khub-deposition-update/examples/create-seed.md
```

Review `skills/*/evals/trigger-prompts.csv` when changing skill names, descriptions, or activation boundaries.

## Sanitization

This repository should not contain private local paths, tokens, credentials, personal identifiers, or private project details. Use placeholders such as `$CODEX_HOME`, `PROJECT_ROOT`, and `OBSIDIAN_VAULT`.
