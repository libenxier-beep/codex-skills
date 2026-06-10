---
name: khub-classifier-router
description: Use when standardized intake material must be classified for KHub, routed to an area, matched to a template, deduped, or blocked before any Obsidian note is created or updated.
---

# KHub Classifier Router

Classify standardized intake into a write-safe KHub route decision. This is the decision layer only: it may produce a `route-plan` or a `decision-report`, but it must not create or update Obsidian notes.

Follow the shared rules in `../workflow-principles.md`: route before writing, dedupe before writing, preserve source trace, and stop instead of forcing weak material into heavy templates.

## Use When

- A prepared intake item needs final KHub type selection: `seed`, `cognition`, `concept`, `viewpoint`, `playbook`, or `prediction`.
- The task asks where a memo belongs in KHub, which template fits, whether to create or append, or whether a note should be blocked.
- Duplicate, append, split, no-fit, or human-decision handling is needed before deposition.
- Source material may be too thin for a heavy template and needs a density check.

## Do Not Use When

- The user only needs raw Flomo collection. Use `flomo-daily-intake` first.
- The input is an already validated `route-plan` and the task is to write notes. Use `khub-deposition-update`.
- The user is asking to draft prose, summarize an article, or update non-KHub notes.
- There is no standardized intake or source material to classify.

## Inputs

- A standardized intake artifact such as the output of `flomo-daily-intake`
- Current KHub taxonomy and folder layout
- Current KHub template map
- Existing-note candidates from vault search when dedupe or append is needed

## Procedure

1. Parse each intake item into the required fields from [contract.md](contract.md).
2. Load only the references needed for the current decision:
   - [references/taxonomy.md](references/taxonomy.md) for note type selection.
   - [references/area-routing.md](references/area-routing.md) for target area and bucket.
   - [references/dedupe-policy.md](references/dedupe-policy.md) when existing notes may match.
   - [references/fit-check-policy.md](references/fit-check-policy.md) when type, area, template, or density is uncertain.
   - [references/decision-states.md](references/decision-states.md) when choosing the final state.
3. Choose the smallest stable final type that does not overstate source maturity.
4. Route to a valid existing KHub area and bucket; never create a new area silently.
5. Select the mapped template and check whether its weight fits the source density.
6. Search for duplicate or append candidates when source ID, title, or meaning may overlap.
7. Emit exactly one output for each item: a write-safe `route-plan` or a blocked `decision-report`.

## Output Contract

- Return `route-plan` only when the item is safe for downstream deposition.
- Return `decision-report` when no-fit, ambiguity, resolved duplicate, or human choice remains.
- Do not return both for the same intake item.
- For `no_fit` and `needs_human_decision`, set `write_blocked: true`.
- A `route-plan` must include the fields required by [contract.md](contract.md).

## Stop Rules

- If no valid KHub type can be chosen, output `no_fit`.
- If type, template, or target area cannot be matched safely, output `no_fit`.
- If multiple candidates remain too close to call, output `needs_human_decision`.
- If the item is already covered with no material delta, output `skip_duplicate` for reporting and do not hand it to deposition for mutation.
- Never create or update Obsidian notes from this skill.

## Validation

- Run [scripts/validate-route-plan.sh](scripts/validate-route-plan.sh) on any `route-plan` or `decision-report` saved as YAML.
- Check that blocked outputs have `write_blocked: true`.
- Check that no final Obsidian Markdown or vault mutation was produced.
- For trigger maintenance, use [evals/trigger-prompts.csv](evals/trigger-prompts.csv).

## Common Mistakes

- Classifying directly from raw Flomo without an intake artifact.
- Picking a heavier template because the idea feels important, even though the source is thin.
- Returning a `route-plan` for `no_fit` or `needs_human_decision`.
- Treating `skip_duplicate` as permission to mutate the vault.
- Hiding uncertainty instead of producing a decision report.

See [contract.md](contract.md) for the I/O shape and `../workflow-principles.md` for cross-layer workflow principles.
