# Work Order specification

Every write task needs one strict JSON Work Order under `docs/work-orders/`. It binds:

- identifier, title, risk class and business outcome;
- repository, feature branch and immutable base commit;
- exact file allowlist and explicit out-of-scope effects;
- validation commands, rollback and expiration;
- a strict `execution_budget` containing effort class, optional host token budget, maximum builder
  and review rounds, maximum parallel readers, exactly one full regression run, minimum-needed
  context and stop-and-replan behavior;
- owner approval and, before protected merge, a PASS acceptance receipt;
- canonical payload and scope SHA-256 digests.

The candidate may change only allowlisted paths, including the Work Order itself. Approval
never grants live-system authority. Acceptance binds the final repository payload; changing
the candidate after binding invalidates the receipt and requires a fresh review and bind.
These local digests prove integrity, not human identity or reviewer independence. The protected
merge separately authenticates the configured owner's exact-head GitHub comment.

Use `python3 scripts/aef_scaffold_work_order.py new ...` to create a draft and
`python3 scripts/aef_scaffold_work_order.py bind ...` only after tests and independent review.
Use `--effort-class small|standard|large`; use `--host-token-budget` only when the current host
provides a reliable limit. A budget is a stopping rule, never permission to skip a required gate.
