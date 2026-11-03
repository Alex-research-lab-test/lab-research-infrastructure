---
name: research-reproduction
description: Use when a research request involves paper reproduction, custom-data training or adaptation, algorithm development, numerical simulation, data analysis, model evaluation or experiment failure analysis. Also use for research code, CI, dependencies, environments, Skills, agents and collaboration policy maintenance, including documentation changes.
---

# Research task execution

Read the project's `AGENTS.md`, task and actual Git diff. Preserve local work,
history, datasets and scientific acceptance criteria. Keep this existing Skill
name and native reviewer integration; do not build another agent framework.

## Task Understanding

Before implementation, establish a concise task record using the project's
`docs/lab/templates/research-task.md` or central `templates/research-task.md`:

1. Identify the research question, intended outcome and success/failure criteria.
   Classify the goal as A official reproduction, B custom-data adaptation,
   C algorithm development, D analysis/simulation, or collaboration maintenance.
   Mixed goals may combine routes; failure diagnosis follows the relevant route
   with evidence from failed runs, rather than automatically rerunning a demo.
2. Inspect existing repository instructions, project docs, task/implementation
   maps, data metadata and relevant experiment records first. Search the research
   knowledge base before changing established architecture, interfaces, training,
   robot control or experiment procedures. Account for documented failures.
   Use targeted reads; do not load a whole vault or scan real datasets by default.
3. Record supplied/accessible papers, code revisions, data versions and semantics,
   experimental conditions, outputs, validation basis and execution permissions.
   Mark irrelevant fields not applicable; a numerical or maintenance task does
   not require an invented paper or official dataset. A source locator is not
   evidence that its contents were read.
4. Decide whether the information is sufficient for the next reliable step.
   If sufficient, record READY and proceed without redundant questions. Missing
   source access can be an evidence gap for later verification, not a reason to
   ask the user to restate an already clear goal. A provisional plan must label
   unverified reference values and cannot claim faithful results.

### Necessary clarification, including during execution

- If a missing or conflicting fact materially changes the technical plan,
  scientific interpretation, success criteria or safety boundary, clarify before
  the dependent operation. Do not choose the research goal, data meaning,
  Action definition or evaluation standard on the user's behalf.
- Search existing evidence first, then ask the most important 1–3 questions per
  round, with concrete choices/examples when useful. Use the client's question
  mechanism when available. Do not send a broad intake questionnaire or ask
  questions already answered in the project/user materials.
- For details that do not affect correctness, use reasonable defaults and record
  each assumption, its rationale and scope. Never promote an unconfirmed critical
  fact to a default. User-confirmed decisions and agent assumptions stay distinct.
- Recheck when new evidence appears. If Action metadata or an evaluation protocol
  contradicts an earlier agreement, pause affected conversion, implementation,
  training/evaluation or claims; explain the conflict and ask again. Continue
  independent safe work. A previous plan is not permission to guess new semantics.
- In an unattended/non-interactive run, persist or return a task record with
  status `NEEDS_USER_INPUT`, unresolved questions, evidence checked, blocked
  operations and safe next work. Do not fabricate answers, wait indefinitely or
  silently drop the questions. An interactive session also records unresolved
  blockers; resume dependent work only after a reliable answer resolves them.
- Track authorization separately from information sufficiency. A clear training
  request does not authorize unspecified data access, compute budget, output
  mutation, publication or hardware. Preserve existing authorizations; request
  only missing permissions when a concrete dependent step needs them.

## Select the research route

| Route | Required basis and validation |
| --- | --- |
| A Official paper reproduction | Pin paper/version, upstream revision, official dataset/splits, experiment protocol and reference metrics. Map sections/equations to implementation; reproduce faithfully and label deviations. A clear request for official Push-T uses the official route, without asking the user to redesign it. |
| B Custom-data adaptation | Understand structure, episode boundaries, Observation/Action shape and physical meaning, units/frames, timing/sample frequency, training goal and evaluation. Inspect how the existing code can consume these inputs; distinguish engineering adapters from algorithm changes. Never replace the user's data with official demo data by default. |
| C Algorithm development | Establish baseline, improvement hypothesis, controlled comparisons, metrics and ablation plan. Preserve comparable splits, budgets and protocols; separate a tested implementation from evidence that the hypothesis improves results. |
| D Analysis or numerical simulation | Establish inputs, analysis question, numerical/statistical method, result format and validation basis. Use appropriate analytic checks, synthetic cases, convergence/error or uncertainty analysis; do not force a training or official-demo workflow. |

For model evaluation and failed experiments, inspect actual configs, versions,
logs, metrics and resource conditions; separate observed failure from suspected
cause and propose discriminating checks. Route by the research goal, not just
keywords or repository name. Do not rerun expensive/unsafe work without authority.
Project-specific scientific validation may differ across routes; GitHub PRs,
Actions, Rulesets, reviews and reproducible records remain shared requirements.

## Research execution

1. Record the chosen route, evidence, baseline, environment, data/split and
   input/output semantics, configuration and protocol when relevant. Use primary
   sources and the paper-to-implementation map when a paper informs the work;
   otherwise map requirements/methods to code and validation without inventing a
   paper. Use the project's `docs/lab/templates/paper-implementation-map.md` or
   central `templates/paper-implementation-map.md` at the adopted source commit.
2. Make the smallest supported change on an isolated branch. Preserve unrelated
   work. Separate engineering adaptations from faithful reproduction claims and
   infrastructure from algorithm changes.
3. Validate static checks and relevant CPU tests first, then the route's specific
   scientific checks. Run data/GPU/hardware work only with authorized procedure,
   inputs, output location and budget. Keep missing prerequisites explicit and
   continue independent work; return to clarification if new ambiguity appears.
4. Record actual commands, versions, seeds, outputs, metrics, failed attempts and
   limitations in the experiment record when applicable. Never invent successful
   runs or treat a plan as experiment results.

Task type does not determine review level by itself. Apply the unchanged policy
below to the goal, full diff and scientific risk at the current stage. Clarifying
questions do not have to wait for reviewer approval; planned future reviews are
not completed reviews. Formal scientific acceptance remains L2 on every route.

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
