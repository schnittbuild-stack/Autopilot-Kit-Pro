# Acceptance gate

Acceptance is a final-candidate receipt, not broad permission. Before a PASS receipt:

1. freeze the exact candidate head and file list;
2. run focused tests while building, then the full regression suite once for the final candidate;
3. run deterministic governance, secret, scope and diff checks before model-based review;
4. run one independent read-only review that reports only material correctness, security, scope or
   operability defects; harmless additions and style preferences are non-blocking advisories;
5. if that review fails materially, permit one correction and one re-review, then stop and re-plan;
6. confirm rollback and absence of live effects;
7. bind payload and scope digests with the human-owner evidence reference.

Any later candidate change invalidates acceptance. The protected merge workflow independently
checks the pull-request head, changed paths, Work Order receipt and required GitHub checks.
It cannot authorize reserved or live-effect scope.
The local receipt is not an identity proof. Operation-time owner identity comes from the exact
GitHub comment `AEF-APPROVE <candidate-head-sha>` by the configured human owner.
Do not rerun an unchanged valid check or review on the same candidate merely for reassurance.
