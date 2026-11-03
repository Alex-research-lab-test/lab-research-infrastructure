# Review record

Status: incomplete. Replace instructions with observed evidence; never prefill a pass.

## Decision and fixed scope

| Field | Value |
| --- | --- |
| Task / repository / date | Task identifier, repository and UTC timestamp |
| Policy source | Central repository and full adopted commit SHA |
| Level and trigger | L0/L1/L2, concrete task/diff/risk rationale; uncertainty raises to L2 |
| Scope and exclusions | Reviewed paths and relevant scientific evidence |
| Base / head SHA | Full immutable commit IDs |
| Pending changes | Clean, or saved patch path and hash; do not imply HEAD covers a dirty diff |
| Required roles | None / code_reviewer / both native reviewers |
| Checks | Exact commands, exit status, output/artifact references and tested SHA |

## Actual native execution

For L0 write “not applicable; zero reviewer calls” with the task-session trace.
For L1/L2 fill one row per required role, including failed or unavailable calls.

| Native agent_type | Thread/session ID | Native binding evidence | Reviewed SHA / scope | Completion / result evidence |
| --- | --- | --- | --- | --- |
| Actual selector or unavailable role | Actual runtime ID, or unavailable | Call and runtime role metadata/role instructions | Reviewer-returned SHA and paths | Completed / failed / incomplete, with actual response reference |

For L2 record separate thread IDs, `fork_turns="none"` and independent input
packets; neither packet may include the other's findings. Preserve raw traces
privately with a sanitized public extract; never publish credentials or datasets.

## Findings and resolution

| Role / severity | Concrete issue and supporting evidence | Disposition / fix SHA | Retest and re-review evidence | Unresolved risk |
| --- | --- | --- | --- | --- |
| Finding, or explicit no-actionable-findings result | File:line/source and trigger; distinguish unknowns | Fixed / evidence-based disagreement / unresolved | Commands and affected-scope review at new SHA | Remaining limitation |

## Final coverage and disposition

Record final tip SHA and whether it equals reviewed SHA. For an evidence-only
appendix, include `git diff reviewed..final -- paths` showing unchanged reviewed
content and identify appended paths as unreviewed. Material changes need a new
review; a previous pass cannot cover them by assertion.

State completed / incomplete / failed / not applicable, missing roles/results,
remaining findings and authorization for the next action separately. No AI review
proves scientific correctness or replaces CI, cloud review or human approval.
