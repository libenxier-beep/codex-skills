---
name: khub-deposition-update
description: Use when a validated KHub route-plan must become an Obsidian note creation or append operation with source trace, template mapping, write guards, and execution reporting.
---

# KHub Deposition Update

Turn a validated KHub `route-plan` into a safe Obsidian create or append operation. This is the execution layer only: it must not reclassify material, change routing, or recover from blocked decisions by guessing.

Follow the shared rules in `../workflow-principles.md`: preserve source trace, honor write gates, and report exactly what changed.

## Use When

- The input is a validated `route-plan` from `khub-classifier-router`.
- The requested operation is `create` or `append` for an Obsidian KHub note.
- The task needs a structured note payload before writing.
- The user asks for an execution report after KHub note creation or update.

## Do Not Use When

- The input is raw Flomo or an unclassified intake artifact.
- The input is a `decision-report`, `no_fit`, `needs_human_decision`, or `write_blocked: true`.
- The route operation is `skip_duplicate`; report it without vault mutation instead of using this execution layer.
- The task asks to choose a note type, area, or template. Use `khub-classifier-router`.
- The target is Feishu, a non-KHub Obsidian note, or a general writing task.

## Inputs

- A valid `route-plan`
- The original intake item for traceability
- The selected KHub template
- Existing note content when `operation=append`

## Procedure

1. Validate that input is a `route-plan` and that `write_blocked` is false.
2. Refuse immediately if any stop rule from [contract.md](contract.md) applies.
3. Load only the references needed for the operation:
   - [references/template-mapping.md](references/template-mapping.md) to confirm `final_type` and `template_id`.
   - [references/source-trace-policy.md](references/source-trace-policy.md) for provenance and fidelity.
   - [references/frontmatter-policy.md](references/frontmatter-policy.md) before rendering frontmatter.
   - [references/append-policy.md](references/append-policy.md) for append operations.
   - [references/conflict-handling.md](references/conflict-handling.md) when target content or placement is unclear.
   - [references/tool-contracts.md](references/tool-contracts.md) when renderer, writer, dry-run, or failure behavior is unclear.
4. Build a structured `note-payload` before rendering Markdown.
5. Render final Obsidian Markdown through the available Obsidian markdown path.
6. Execute vault operations through the available structured Obsidian path.
7. Return an `execution-report` that says whether writing was attempted and what changed.

## Output Contract

- Produce a structured `note-payload` before any write.
- Produce an `execution-report` for every attempted or refused execution.
- If blocked or conflicted, set `write_attempted: false` unless a write genuinely happened before the conflict was detected.
- Do not produce a new classification, target area, template, or route plan.

## Stop Rules

- If `write_blocked: true`, stop immediately.
- If `kind` is not `route-plan`, stop immediately.
- If `status` is `no_fit` or `needs_human_decision`, stop immediately.
- If `template_id`, `target_note_path`, or `final_type` is missing, stop immediately.
- If append placement is unsafe or unclear, return `conflict` instead of forcing a write.
- If Obsidian access is unavailable, stop with the exact blocker and do not emulate success.

## Validation

- Run [scripts/validate-note-payload.sh](scripts/validate-note-payload.sh) before rendering or writing a payload saved as YAML.
- Run [scripts/validate-execution-report.sh](scripts/validate-execution-report.sh) on the final report saved as YAML.
- Confirm the report's `write_attempted` value matches the actual command path.
- Confirm source trace remains present after create or append.
- For trigger maintenance, use [evals/trigger-prompts.csv](evals/trigger-prompts.csv).

## Common Mistakes

- Reclassifying or rerouting when the route plan feels imperfect.
- Writing a blocked `decision-report` into KHub.
- Rendering Markdown before preserving source trace in the structured payload.
- Appending into an unclear section instead of returning `conflict`.
- Reporting success without checking the actual vault operation.

See [contract.md](contract.md) for the execution contract and `../workflow-principles.md` for cross-layer workflow principles.
