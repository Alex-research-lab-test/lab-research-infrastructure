---
name: research-reproduction
description: Plan, implement or audit a scientific paper reproduction using author-provided sources, a paper-to-code map and reproducible experiment records. Use for research implementation or reproduction tasks, not routine formatting-only changes.
---

# Research reproduction

Read the project's `AGENTS.md` and the specific task before deciding what evidence
or execution is needed. Preserve the user's scope, local modifications, Git
history and dataset boundaries. A reproduction request does not authorize
publishing code, accessing hardware or consuming an unspecified training budget.

1. Identify the paper version, DOI or arXiv identifier, official code revision,
   intended reproduced result and explicit engineering adaptations. Read supplied
   primary sources; if unavailable, report the gap rather than infer the method
   from a title. Use the project's paper-to-implementation map, or create one
   from `docs/lab/templates/paper-implementation-map.md`. In the central repository,
   the maintained source is `templates/paper-implementation-map.md`; when a local
   copy is unavailable, use the source commit recorded by the project's adoption.
2. Record the code baseline, environment, dataset version and split, input/output
   semantics, configuration and evaluation protocol. Search an available research
   knowledge base for relevant prior failures before changing an established
   training pipeline, interface, control procedure or experimental protocol.
3. Implement the smallest supported change on an isolated branch. Keep
   algorithmic changes separate from infrastructure-only changes. Do not reset,
   stash, overwrite or commit unrelated user work. Treat differences from the
   official implementation as adaptations with an explicit rationale.
4. Validate in layers: static checks, an appropriate CPU unit/smoke test, then
   data/GPU experiments only when the required inputs and resource budget are
   authorized. Hardware tests need the project's explicit execution procedure.
   Stop at the first missing prerequisite and continue independent work.
5. Record exact commands, code and dataset versions, seeds, outputs, metrics and
   limitations using the project's experiment record. Separate actual runs from
   planned runs; do not fabricate metrics, citations or successful reproduction.
6. When independent review is requested or required by project instructions,
   ask the parent to invoke `scientific_reviewer` for evidence and methodology,
   and `code_reviewer` for implementation risks. Supply the base/head SHA and
   relevant sources. Reviewers return findings; the parent resolves them.

End with what was demonstrated, what remains unverified, and artifact locations.
Never describe CI success alone as a scientific reproduction result.
