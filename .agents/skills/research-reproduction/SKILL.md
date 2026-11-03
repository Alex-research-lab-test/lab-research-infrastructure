---
name: research-reproduction
description: Use when planning, implementing or auditing a scientific reproduction, or maintaining research code, CI, dependencies, environments, Skills, agent configuration or research collaboration policy. Also use for documentation changes within these tasks to determine the appropriate review level.
---

# Research reproduction

Read the project's `AGENTS.md`, task and actual Git diff before choosing evidence,
execution or review. Preserve local work, history, datasets and scientific
acceptance criteria. Publication, hardware and unspecified training budgets need
separate authorization. For collaboration maintenance, apply the review policy
below without inventing a paper, dataset or experimental requirement.

## Research execution

1. For research implementation, identify the paper version, DOI/arXiv, official
   code revision, intended result and explicit adaptations. Read primary sources
   and the paper-to-implementation map. If absent, use the project's
   `docs/lab/templates/paper-implementation-map.md` or central
   `templates/paper-implementation-map.md` at the adopted source commit. Report
   unavailable evidence rather than guessing methods.
2. Record baseline, environment, dataset/split, input/output semantics,
   configuration and protocol when relevant. Search the research knowledge base
   before changing established architecture, interfaces, training, robot control
   or experiment procedures; account for documented failures.
3. Make the smallest supported change on an isolated branch. Preserve unrelated
   work. Separate engineering adaptations from faithful reproduction claims and
   infrastructure from algorithm changes.
4. Validate static checks and relevant CPU tests first. Run data/GPU/hardware
   work only with authorized procedure, inputs, output location and budget.
   Missing prerequisites remain explicit; continue independent work.
5. Record actual commands, versions, seeds, outputs, metrics and limitations in
   the experiment record when applicable. Never invent successful runs.

## Automatic review decision

The main agent owns this decision; the user need not name reviewers or request
review explicitly. Assess the task goal, full base/head diff (including pending
changes), project rules and scientific risk. Use the highest applicable level
across a mixed change; project requirements may raise, never lower, this minimum.
Reassess when scope changes. Filenames alone do not determine scientific impact.

| Level | Trigger | Required native reviewers |
| --- | --- | --- |
| L0 | README, comments, formatting or simple documentation with no effect on execution, results or safety | None; relevant format checks only |
| L1 | Ordinary code/bug fixes; CI, dependencies, environment/build; interfaces, exceptions, concurrency/resources; Skills, agent configuration or research collaboration policy | `code_reviewer` |
| L2 | Core algorithms, equations, loss/optimization; preprocessing, normalization or splits; training configuration, hyperparameters, metrics or protocols affecting conclusions; robot control, safety constraints or critical hardware interfaces; final scientific acceptance of a formal reproduction | Both `scientific_reviewer` and `code_reviewer` |

If scientific correctness impact is uncertain, choose L2. A prose change to an
experimental protocol can be L2; a Skill change is L1 even though it is Markdown.
Do not treat every use of this Skill as final scientific acceptance.

Record level, concrete trigger/rationale, reviewed paths, exclusions, base/head
SHA, pending diff identity and required roles before dispatch. Use the project's
`docs/lab/templates/review-record.md`, or central `templates/review-record.md` at
its adopted source commit. Missing templates do not excuse missing evidence.

## Native dispatch and resolution

1. Finish one bounded functional change and its applicable tests before review;
   do not dispatch on each edited line. Freeze a commit for review. If a dirty
   diff must be reviewed, supply its exact saved patch/hash as well as HEAD;
   a bare HEAD review does not cover uncommitted work.
2. L0: do not spawn a reviewer; record reviewer status as not applicable and
   format-check evidence. L1: invoke the actual native `code_reviewer` role.
   L2: separately invoke both native roles with `fork_turns="none"`; send the
   same fixed baseline/head, scope, task requirements and primary evidence to
   each, without either reviewer's conclusions. Dispatch both before collecting
   results so they independently assess the materials.
3. Use the native role selector (`agent_type` where exposed), not a task name or
   copied role prompt. Check that each required role is actually registered.
   Never substitute a default/general agent or parent-authored review. If a role
   is unavailable, a call fails, or a result cannot be verified, record review
   incomplete with the error; do not mark it passed. One completed L2 reviewer
   does not satisfy L2. Do not grant trust or permissions automatically to fix it.
4. Wait for every required result. Save actual agent type, native thread/session
   ID and role-binding evidence, reviewed SHA/scope, findings, supporting evidence
   and limitations. A spawn acknowledgement or plan is not a completed review.
   The orchestrator may attach verifiable runtime IDs if children cannot read them.
5. Resolve findings against evidence, rerun affected tests and record disposition
   and remaining risks. Do not silently weaken scientific acceptance criteria
   because a reviewer requests it; report proposed changes for an author decision.
   Unresolved actionable findings prevent a passed record.
6. If fixes materially change reviewed code/scientific logic, reassess the level
   and re-review affected scope with the required roles, at the new SHA. Keep old
   records as superseded. Documentation-only evidence appendices may cite the
   unchanged reviewed content, but must state that the new tip itself was not
   reviewed; never silently transfer approval between SHAs.
7. Before preparing a PR or starting a formal experiment, check that the final
   executable/scientific/configuration content is covered by the required review
   and tests, with exact SHA or an explicit content-equivalence diff. If changed
   content lacks coverage, leave review incomplete. Record publication/experiment
   permission separately from review completion.

This is agent workflow policy, not a GitHub-enforced security gate. Preserve
GitHub Actions, Rulesets, cloud Codex Review and human approvals. AI review and
CI are supporting evidence, never proof of scientific correctness.

End with demonstrated results, unresolved risks, unverified work and artifact
locations. Distinguish completed, incomplete, failed and not-applicable reviews.
