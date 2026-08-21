#!/usr/bin/env python3
"""Protected ordinary-Class-B merge client for Autopilot Kit.

The client intentionally reuses GitHub's server-side rules. It checks only the immutable
head, exact Work Order/scope and required checks, then performs one squash merge when
--execute is present and the dedicated Environment App token is available.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

import aef_validate


class MergeError(RuntimeError):
    pass


def api(method: str, endpoint: str, token: str, body: dict[str, Any] | None = None) -> Any:
    if method not in {"GET", "PUT"}:
        raise MergeError(f"unsupported method: {method}")
    url = "https://api.github.com" + endpoint
    data = json.dumps(body).encode("utf-8") if body is not None else None
    request = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "aef-protected-merge/1.0",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            try:
                return aef_validate.strict_json_loads(
                    response.read().decode("utf-8"), source=f"GitHub response for {endpoint}"
                )
            except aef_validate.ValidationError as exc:
                raise MergeError(f"GitHub API returned invalid or duplicate-key JSON for {endpoint}: {exc}") from exc
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise MergeError(f"GitHub API {method} {endpoint} failed with {exc.code}: {detail[:500]}") from exc


def pull_files(repository: str, number: int, token: str) -> list[str]:
    files: list[str] = []
    for page in range(1, 31):
        result = api("GET", f"/repos/{repository}/pulls/{number}/files?per_page=100&page={page}", token)
        if not isinstance(result, list):
            raise MergeError("GitHub pull files response is not a list")
        for item in result:
            if not isinstance(item, dict) or not item.get("filename"):
                continue
            files.append(item["filename"])
            if item.get("status") == "renamed" and item.get("previous_filename"):
                files.append(item["previous_filename"])
        if len(result) < 100:
            return sorted(set(files))
    raise MergeError("pull request exceeds the 3000-file protected merge limit")


def validate_candidate(root: Path, files: list[str], work_order: str, expected_base: str, expected_branch: str, trusted_policy: Path) -> None:
    trusted_validator = Path(__file__).resolve().parent / "aef_validate.py"
    command = [
        sys.executable,
        str(trusted_validator),
        "--root", str(root),
        "--policy", str(trusted_policy),
        "--work-order", work_order,
        "--expected-base", expected_base,
        "--expected-branch", expected_branch,
        "--require-acceptance",
        "--ordinary-only",
    ]
    for path in files:
        command.extend(["--changed-file", path])
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    if result.returncode != 0:
        raise MergeError(result.stderr.strip() or "candidate governance validation failed")


def validate_activation(root: Path, policy: dict[str, Any], allowed_statuses: list[str]) -> None:
    try:
        aef_validate.validate_runtime_activation(root, policy, allowed_statuses)
    except aef_validate.ValidationError as exc:
        raise MergeError(str(exc)) from exc


def paged_list(endpoint: str, token: str, *, object_key: str | None = None) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    separator = "&" if "?" in endpoint else "?"
    for page in range(1, 31):
        result = api("GET", f"{endpoint}{separator}per_page=100&page={page}", token)
        page_items = result.get(object_key, []) if object_key and isinstance(result, dict) else result
        if not isinstance(page_items, list) or any(not isinstance(item, dict) for item in page_items):
            raise MergeError(f"GitHub pagination response is malformed for {endpoint}")
        items.extend(page_items)
        if len(page_items) < 100:
            return items
    raise MergeError(f"GitHub list exceeds the 3000-item protected limit: {endpoint}")


def verify_lineage(repository: str, base: str, head: str, token: str) -> None:
    comparison = api("GET", f"/repos/{repository}/compare/{base}...{head}", token)
    if comparison.get("merge_base_commit", {}).get("sha") != base or comparison.get("status") not in {"ahead", "identical"}:
        raise MergeError("pull-request base is not the exact ancestor/merge-base of the candidate head")


def require_exact_head_owner_comment(repository: str, number: int, head: str, owner_login: str, token: str) -> None:
    comments = paged_list(f"/repos/{repository}/issues/{number}/comments", token)
    directive = f"AEF-APPROVE {head}"
    matching = [
        comment for comment in comments
        if isinstance(comment, dict)
        and str(comment.get("user", {}).get("login", "")).lower() == owner_login.lower()
        and str(comment.get("body", "")).strip() == directive
    ]
    if len(matching) != 1:
        raise MergeError(f"the configured human owner must post exactly one directive: {directive}")


def required_checks(repository: str, head: str, token: str, expected: list[str]) -> None:
    runs = paged_list(f"/repos/{repository}/commits/{head}/check-runs?filter=latest", token, object_key="check_runs")
    failed = []
    for name in expected:
        matching = [item for item in runs if item.get("name") == name]
        run = matching[0] if len(matching) == 1 else {}
        app = run.get("app", {}) if isinstance(run.get("app", {}), dict) else {}
        if len(matching) != 1 or run.get("conclusion") != "success" or app.get("slug") != "github-actions":
            failed.append(name)
    if failed:
        raise MergeError(f"required checks are not successful for exact head {head}: {failed}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", required=True)
    parser.add_argument("--pull-request", type=int, required=True)
    parser.add_argument("--expected-head", required=True)
    parser.add_argument("--candidate-root", default="candidate")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.pull_request <= 0 or len(args.expected_head) != 40 or any(char not in "0123456789abcdef" for char in args.expected_head):
            raise MergeError("pull request number and expected head must be exact canonical values")
        token_name = "AEF_MERGE_TOKEN" if args.execute else "GH_TOKEN"
        token = os.environ.get(token_name)
        if not token:
            raise MergeError(f"{token_name} is required")
        if args.execute and os.environ.get("GITHUB_TOKEN") == token:
            raise MergeError("ambient GITHUB_TOKEN is not accepted as dedicated merge authority")
        root = Path(args.candidate_root).resolve()
        trusted_root = Path(__file__).resolve().parents[1]
        trusted_policy = trusted_root / "governance/policy.json"
        policy = aef_validate.load_json(trusted_policy)
        try:
            aef_validate.validate_policy(policy)
        except aef_validate.ValidationError as exc:
            raise MergeError(str(exc)) from exc
        if args.repository != policy["repository"]:
            raise MergeError("repository argument differs from trusted customer policy")
        pull = api("GET", f"/repos/{args.repository}/pulls/{args.pull_request}", token)
        actual_head = pull.get("head", {}).get("sha")
        if actual_head != args.expected_head or pull.get("state") != "open" or pull.get("draft") is True:
            raise MergeError("pull request is not an open non-draft candidate at the exact expected head")
        if pull.get("base", {}).get("ref") != policy["default_branch"]:
            raise MergeError("pull request does not target the protected default branch")
        if str(pull.get("user", {}).get("login", "")).lower() != str(policy["builder_login"]).lower():
            raise MergeError("pull request must be opened by the configured builder identity, not the human owner")
        files = pull_files(args.repository, args.pull_request, token)
        work_orders = [path for path in files if path.startswith("docs/work-orders/") and path.endswith(".json")]
        if len(work_orders) != 1:
            raise MergeError("exactly one changed Work Order is required")
        base_sha = pull.get("base", {}).get("sha", "")
        validate_candidate(root, files, work_orders[0], base_sha, pull.get("head", {}).get("ref", ""), trusted_policy)
        validate_activation(root, policy, policy["protected_merge"]["allowed_activation_statuses"])
        verify_lineage(args.repository, base_sha, args.expected_head, token)
        if policy["protected_merge"].get("require_exact_head_owner_comment") is not True:
            raise MergeError("trusted policy must require an exact-head human-owner directive")
        require_exact_head_owner_comment(args.repository, args.pull_request, args.expected_head, policy["human_owner"], token)
        required_checks(args.repository, args.expected_head, token, policy["required_checks"])
        if not args.execute:
            print(json.dumps({"eligible": True, "mode": "dry_run", "head": args.expected_head, "work_order": work_orders[0]}, sort_keys=True))
            return 0
        result = api(
            "PUT",
            f"/repos/{args.repository}/pulls/{args.pull_request}/merge",
            token,
            {"sha": args.expected_head, "merge_method": policy["protected_merge"]["merge_method"]},
        )
        if result.get("merged") is not True:
            raise MergeError(f"GitHub did not merge the exact candidate: {result.get('message', 'unknown reason')}")
        print(json.dumps({"merged": True, "head": args.expected_head, "merge_sha": result.get("sha")}, sort_keys=True))
        return 0
    except (MergeError, OSError, KeyError, json.JSONDecodeError) as exc:
        print(f"AEF protected merge failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
