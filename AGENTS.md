# Autopilot Kit – Operating Constitution

This file is the mandatory entry point for every coding agent in this repository.

- Project: **Autopilot Kit**
- Business goal: Menschen, die eine KI-Schulung abgeschlossen haben, aber danach nicht ins Tun kommen, bekommen ein Download-Kit: Ihr eigenes LLM richtet sich damit selbst zu einem persoenlichen Assistenten-Setup ein und erledigt in rund 30 Minuten die erste echte Arbeitsaufgabe.
- Primary users: Teilnehmer abgeschlossener KI-Schulungen ohne Programmier- oder Terminalkenntnisse, Solo-Selbststaendige und kleine Vertriebsteams, Schulungsanbieter, die das Kit als After-Sales-Produkt weitergeben
- Initial stack: Markdown, Python, GitHub Actions, Claude Code

## Authority

1. `@schnittbuild-stack` is the human owner and final approver for reserved, live-effect,
   deployment, legal, financial and credential-bearing decisions.
2. The Owner-Orchestrator owns scope, architecture, sequencing, delegation and acceptance.
   It may create and integrate commits only in an assigned feature worktree. For an ordinary
   repository-only Class B change, it may request the protected merge workflow after every
   exact gate passes. It never pushes directly to `main` and never uses ambient
   chat credentials as standing merge authority.
3. Builder agents implement only an approved, time-bounded and file-bounded Work Order in
   an isolated feature branch. The GitHub builder identity is `@alexanderschnittcher-gif`, distinct from
   the owner. A builder never merges, self-approves or deploys.
4. Read-only reviewers try to disprove the candidate from a separate process or session.
5. Runtime or business-system agents receive no authority from this repository framework.

The human product/programming conversation sets the roadmap. The Owner-Orchestrator turns
that roadmap into small, independently verifiable Work Orders and delegates them to builders.
If the user asks to continue onboarding, inspect `.aef/onboarding-state.json`, resume at the first
pending milestone and never repeat a completed step. Follow the distributor's Owner Onboarding;
GitHub login, credentials, protection activation and bootstrap/final merges remain human gates.

## Mandatory start

1. Read `git status --short --branch`.
2. Read this file and the active Work Order. Do not preload every governance document.
3. Identify the branch, base commit, exact file allowlist and `execution_budget`.
4. Read only the relevant reference: the autonomy matrix for classification, the Work Order
   specification for writes, and the acceptance gate only when preparing final acceptance.
5. Write a short plan and target-state evidence before editing.
6. Use a feature branch and one writer per worktree.

## Lean execution

- Use deterministic searches, validation and focused tests before model-based review.
- Load only the files needed for the current decision; cite paths instead of repeating documents.
- Run focused checks while building and the complete regression suite once on the final candidate.
- Use readers only for distinct questions and never exceed the Work Order's parallel-reader limit.
- Perform one final independent review. If it finds a material defect, allow one correction and
  one re-review; style preferences and harmless additions are advisories, not another loop.
- Reuse evidence that is still bound to the same candidate. Never repeat an unchanged check merely
  to increase confidence.
- Stop and re-plan when any round or host token budget is exhausted. Do not silently continue.

## Hard rules

- Never push directly to `main`, force-push or bypass repository protections.
- Never commit credentials, private keys, `.env` files, tokens, raw customer exports or dumps.
- Never perform a live or deployment action because a Work Order or chat message exists.
- Never change a path outside the active Work Order allowlist.
- The ordinary lane is default-deny: every changed path must match an explicit `ordinary_paths`
  pattern; unclassified paths are forbidden.
- Never stage the whole repository; stage exact paths.
- Reserved paths require exact human-owner approval for the immutable candidate head.
- Ordinary repository-only Class B work needs a valid Work Order and PASS acceptance receipt.
- Local hashes prove integrity, not human identity. Before merge, `@schnittbuild-stack` must post
  exactly `AEF-APPROVE <candidate-head-sha>` on the builder-authored pull request.
- Only the trusted protected workflow on `main` may use the dedicated App token.
- Stop on unexpected concurrent edits, changed base, missing evidence or protection drift.

## Completion

A task is complete only when focused tests, one final regression run, governance validation,
secret scan, diff hygiene, scope verification and an independent read-only review pass. Deployment is not proof of live
or business impact. Record facts as `[PROVEN]` and unverified conclusions as `[ASSUMPTION]`.
