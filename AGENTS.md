# Repository instructions

## Scope

Maintain the lab's collaboration policy, Codex metadata and project templates.
Use GitHub and Codex native features. Do not build an agent service, modify a
consumer's core algorithm, upgrade its training environment, or execute hardware.

## Workflow

- Work on a branch and inspect existing changes before editing. Preserve user
  modifications, Git history and datasets. Never use force push, reset or clean
  to prepare a research repository for this infrastructure.
- Before changing an established architecture, shared interface, training
  pipeline or experimental procedure, search the available research knowledge
  base with targeted terms and read only relevant notes.
- This test rollout requires explicit confirmation before remote repository
  creation, Fork creation, pushing, access changes and rule activation. A local
  preparation task does not authorize those remote operations or public comments.
- Keep public output free of credentials, internal deployment details, datasets
  and unpublished research. Use an approved public Git author identity.
- Native skill and reviewer sources live at the repository root. Do not maintain
  a second copy in `templates/project`; adoption copies the canonical files.
- Verify with `pre-commit run --all-files --show-diff-on-failure`,
  `python -m unittest discover -s tests -v` and actionlint against both workflows.
  Do not claim a remote check, model review or gate passed without its evidence.

## Code Review Rules

### Research and data boundaries

- Flag workflows that run camera/robot code, access real experiment data, expose
  secrets or execute PR code with elevated token permissions. Use GitHub hosted
  runners with read-only contents permission for ordinary PR checks.
- Flag claims of scientific reproduction inferred only from CI, template files
  or an experiment that was not run. State exactly what evidence was observed.

### Configuration behavior

- Changes to native Codex file layouts, agent keys or workflow dependencies must
  cite current official behavior and update the adoption instructions.
- An AI comment or local reviewer output is not a required GitHub status check.
  Bind merge rules only to observed check contexts and their verified source App.
- Keep mechanical formatting in CI. Focus review on broken behavior and evidence.
