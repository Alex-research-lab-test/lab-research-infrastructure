# Research project instructions

## Scope and evidence

- Read the task and applicable existing project instructions before editing.
  Preserve local changes, Git history, datasets, checkpoints and experiment logs.
- Before changing established architecture, interfaces, training or experiment
  procedures, search the available research knowledge base using targeted terms.
- For paper implementation, use the `research-reproduction` skill, primary
  sources and the paper-to-implementation map. Separate adaptations from claims
  of faithful reproduction. Never fabricate citations, results or successful runs.
- Infrastructure-only tasks must not modify core algorithms or training defaults.

## Verification and execution

- Inspect `.pre-commit-config.yaml` for the project's selected governance scope.
  Run `pre-commit run --all-files --show-diff-on-failure` and
  `python tools/lab/check_codex.py` using the collaboration tooling environment.
- Baseline collaboration checks do not prove algorithm correctness. For code
  changes, identify and execute the affected modules' suitable tests.
- Do not run the whole test directory without inspecting hardware/data effects.
  Do not run training, data conversion or hardware without the task's authorized
  procedure, inputs, output location and resource budget.
- Before publication, inspect explicitly staged paths and the diff. This test
  rollout requires confirmation before remote creation, pushes or access changes.

## Review

Start a fresh client session from this project's actual trusted Git root. Trust is
user-local; do not commit machine-specific trust paths or overwrite user config.
Standalone role files are discovered natively by supported clients; explicit
config_file registration is optional when that discovery already works.

Use `research-reproduction` for research work and collaboration configuration
maintenance. The main agent automatically selects the highest applicable level
from the task, actual diff, project rules and scientific risk: L0 format-only
changes need no reviewer; L1 code/configuration/Skill/policy changes require
native `code_reviewer`; L2 scientific logic/data/protocol/control changes or
formal reproduction acceptance require both native reviewers independently.
Uncertain scientific impact raises to L2. Follow the Skill's complete triggers
and resolution procedure; do not wait for the user to name roles.

Use the actual native agent_type selector with fork_turns="none" per role.
For L2 dispatch both before collecting conclusions; do not share findings.
Save reasons, fixed base/head SHA, scope, actual role/thread binding, findings,
tests and remaining risks in `docs/lab/templates/review-record.md`. Missing roles
or results mean incomplete review. Re-review material fixes and check final
content coverage before PR preparation or formal experiments. Reviewers are
read-only and inherit parent permissions. AI review is not a GitHub gate or
proof of scientific correctness and does not replace existing approvals.

## Code Review Rules

- Flag changes to data splits, normalization, camera/state/action semantics or
  evaluation metrics that lack a documented rationale and supporting validation.
- Flag CI or scripts that access real hardware, mutate experiment data or execute
  PR code with privileged tokens. Prefer isolated CPU checks and synthetic inputs.
- Flag unsupported reproduction claims and AI/CI success claims without evidence
  covering the current head SHA. Mechanical formatting is checked in CI.
