---
name: flomo-daily-intake
description: Use when Flomo memos for a date, relative day, or short time range must be collected and normalized before classification, KHub routing, Feishu writing, or Obsidian writing.
---

# Flomo Daily Intake

Collect Flomo memos for a bounded time scope and turn them into a reviewable intake artifact. This is an input-only skill: preserve source material, flag unusable items, and stop before routing or writing.

## Use When

- The user asks for Flomo notes from `today`, `yesterday`, a date, or a short range.
- Raw Flomo material is needed before KHub classification, routing, or deposition.
- A reviewable intake artifact is needed before Feishu or Obsidian writes.
- The task mentions Flomo export, memo IDs, tags, audio placeholders, blank memos, or daily intake.

## Do Not Use When

- The user is only asking to classify an already prepared intake artifact.
- The user is asking to create or append KHub/Obsidian notes from a route plan.
- The user wants long-term memory distillation, weekly review, or essay drafting.
- The task requires choosing the final destination system. Stop after intake and hand off.

## Procedure

1. Resolve the requested scope to concrete dates and preserve the user's original wording.
2. Read Flomo through the most structured available access path. If access is unavailable, stop with the exact blocker and do not invent notes.
3. Keep every retrieved memo visible in the intake unless it is an exact duplicate from the same source ID.
4. Preserve timestamp, source ID or memo link, tags, raw text, and any available media/transcript signal.
5. Mark unusable items explicitly: `blank_or_audio_placeholder`, `system_note`, or `unreadable`.
6. Add only a light first-pass `candidate_type`; do not decide final KHub type, area, template, or note path.
7. Return the standardized Markdown intake.

## Read Only If Needed

- Read [contract.md](contract.md) before producing the final artifact or when field names are uncertain.
- Read [references/access-paths.md](references/access-paths.md) when the Flomo source is not already explicit.
- Read [examples/intake-sample.md](examples/intake-sample.md) when output shape is unclear.
- Read [examples/empty-intake.md](examples/empty-intake.md) when no matching notes are found.
- Read `../workflow-principles.md` when the current task is part of the full Flomo-to-KHub workflow.
- Do not read classifier or deposition references from this skill unless the user also asks for downstream execution.

## Output Contract

- Default carrier: Markdown.
- Include a summary with `source`, `requested_scope`, `total_items`, `usable_items`, and `flagged_items`.
- Each item must include `source`, `timestamp`, `memo_ref` or stable ID, `tags`, `status`, `candidate_type`, `summary`, `raw_text`, and `notes`.
- Keep original wording in `raw_text`; summaries may be short, but must not replace the source text.
- If nothing usable is found, return an empty intake with the reason.

## Validation

- Check that the resolved date or range matches the user's request.
- Check that every item has a status and raw-text field, even when unusable.
- Check that no final KHub type, area, template, note path, Feishu record, or Obsidian write is produced.
- For trigger maintenance, use [evals/trigger-prompts.csv](evals/trigger-prompts.csv).

## Common Mistakes

- Dropping blank or audio-only memos without reporting them.
- Over-summarizing the memo so downstream skills lose source wording.
- Treating `candidate_type` as a final KHub classification.
- Continuing into routing or writing during the intake step.

See [contract.md](contract.md) for the required input and output structure.
