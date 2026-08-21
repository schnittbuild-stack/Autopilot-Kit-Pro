# Operating model

```text
human roadmap -> Owner-Orchestrator plan -> exact Work Order
              -> isolated Builder worktree -> tests + read-only review
              -> Owner exact-head comment -> protected GitHub checks
              -> credential-isolated ordinary-Class-B merge
```

The human owns product intent and reserved decisions. The Owner-Orchestrator decomposes the
roadmap, freezes interfaces before parallel work, assigns one writer per worktree, integrates
commits and binds acceptance to an immutable payload. Builders have no merge or live authority.

GitHub protects `main` through strict required checks, a no-bypass ruleset and
the `aef-merge-gateway` Environment. The Environment contains the customer-owned App
credentials; they never appear in repository files or chat. The merge workflow runs from
trusted `main`, reads the candidate, verifies its exact head and Work Order,
and can merge only ordinary repository-only Class B scope.

Work Order hashes bind content but do not authenticate people. At operation time the trusted merge
client requires the pull request to be opened by `@alexanderschnittcher-gif` and requires
`@schnittbuild-stack` to post exactly `AEF-APPROVE <candidate-head-sha>`. GitHub is the identity source.

The ordinary lane admits only paths matching the policy's explicit `ordinary_paths`; anything
unclassified is denied even when it is not named in `reserved_paths`.

Reserved paths are defined in `governance/policy.json`. Changes to them, live systems,
deployments, credentials, security boundaries, financial or legal behavior are never standing
autonomy. They require an exact human decision for the final candidate and a separate path.

## Lean execution contract

Each Work Order declares an effort class and bounded builder, review and reader counts. Small work
allows at most two builder rounds and one reader; standard or large work allows at most three
builder rounds and two readers. Every class allows at most two review rounds and exactly one final
full-regression run. The normal path is deterministic checks, focused implementation tests, final
regression, one independent review and acceptance. Only a material defect permits one correction
and re-review. Reaching a limit means stop and re-plan with the human; it never means looping.

`host_token_budget` may be null because Claude Code and Codex do not expose one portable, reliable
counter to repository code. When the host supports a limit, record it. Round limits, minimum-needed
context and evidence reuse are the mandatory cross-agent controls even when the field is null.
