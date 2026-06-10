# Decision States

## Write-Mutating States

- `create`
- `append`
- `split_new_note`

These may produce a downstream `route-plan` when all write gates pass.

## Resolved No-Write State

- `skip_duplicate`

Use this when the intake item is already covered and has no material delta. It is resolved, but it must not mutate the vault. Prefer a `decision-report` with `write_blocked: true` so the deposition layer is not invoked.

## Blocked States

- `no_fit`
- `needs_human_decision`

Blocked states must produce a `decision-report` with `write_blocked: true`.

## Rule

Only `create`, `append`, and `split_new_note` may enter the deposition layer. `skip_duplicate`, `no_fit`, and `needs_human_decision` are reporting outcomes, not write operations.
