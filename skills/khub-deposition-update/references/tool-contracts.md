# Tool Contracts

This skill writes only through structured Obsidian paths. Do not claim success from rendered text alone.

## Required Capabilities

- Render structured note payloads into Obsidian Markdown.
- Support dry-run or preview mode before mutation when available.
- Create a new note at `target_note_path`.
- Append to an existing note at an explicit section or template-defined update area.
- Return a clear success, blocked, or conflict signal.

## Expected Inputs

- `target_note_path`
- rendered Markdown or structured note payload
- operation: `create`, `append`, or `split_new_note`
- source trace fields: `source`, `source_id`, optional `memo_ref`, optional `timestamp`

## Failure Handling

- If the renderer is unavailable, stop before vault mutation.
- If the writer is unavailable, return `execution-report` with `result: blocked` and `write_attempted: false`.
- If append placement is unclear, return `result: conflict`.
- If a write partially succeeds and later validation fails, report the exact state and do not hide the partial write.

## Dry-Run Rule

When a dry-run mode exists, run it before mutation for append or conflict-prone writes. The dry-run output must preserve target path, operation, source trace, and rendered section placement.
