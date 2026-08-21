#!/usr/bin/env python3
"""Fail-closed repository governance validator for Autopilot Kit."""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import os
import re
import subprocess
import sys
from copy import deepcopy
from datetime import UTC, datetime
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import urlparse


ZERO_HASH = "0" * 64
SHA = re.compile(r"^[0-9a-f]{40}$")
HASH = re.compile(r"^[0-9a-f]{64}$")
LOGIN = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$")
REPOSITORY_NAME = re.compile(r"^[A-Za-z0-9_.-]{1,100}$")
POLICY_PATH = re.compile(r"^(?!/)(?!.*(?:^|/)\.\.(?:/|$))[A-Za-z0-9._/-]+(?:/\*\*)?$")
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\b(?:github_pat_|gh[pousr]_|sk_live_|xox[baprs]-)[A-Za-z0-9_-]{8,}"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
)
MANDATORY_RESERVED = {
    ".aef/**", ".codex/**", ".github/**", "AGENTS.md", "CLAUDE.md", "docs/agentic/**", "governance/**",
    "scripts/aef_merge.py", "scripts/aef_scaffold_work_order.py", "scripts/aef_validate.py",
    "tests/test_aef_governance.py",
}
MANDATORY_ORDINARY = {"docs/work-orders/**"}
EXPECTED_CHECKS = {"AEF Validate / validate", "AEF Release Gate / release-gate"}
EXPECTED_APP_PERMISSIONS = {
    "actions": "read", "administration": "read", "checks": "read", "contents": "write",
    "environments": "read", "issues": "read", "metadata": "read", "pull_requests": "read",
}


class ValidationError(ValueError):
    pass


def canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()


def exact_object(value: Any, fields: set[str], where: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != fields:
        actual = set(value) if isinstance(value, dict) else set()
        raise ValidationError(f"{where} fields differ from the exact contract: {sorted(actual ^ fields)}")
    return value


def reject_secret_values(value: Any, where: str = "$") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            reject_secret_values(child, f"{where}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            reject_secret_values(child, f"{where}[{index}]")
    elif isinstance(value, str):
        lowered = value.lower()
        if any(pattern.search(value) for pattern in SECRET_PATTERNS) or "private key" in lowered or re.search(r"(?:token|secret|key|password)=", lowered):
            raise ValidationError(f"credential-like material detected in runtime contract: {where}")
        if any(ord(char) < 32 or ord(char) == 127 for char in value):
            raise ValidationError(f"control characters detected in runtime contract: {where}")


def valid_display(value: Any, maximum: int) -> bool:
    return (
        isinstance(value, str)
        and value == value.strip()
        and 1 <= len(value) <= maximum
        and not any(marker in value for marker in ("{{", "}}", "\\", "`", '"'))
    )


def valid_display_list(value: Any, maximum: int = 300) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and len(value) == len(set(value))
        and all(valid_display(item, maximum) for item in value)
    )


def valid_https(value: Any) -> bool:
    if not isinstance(value, str) or value != value.strip() or len(value) > 500:
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc) and not any((parsed.username, parsed.password, parsed.query, parsed.fragment))


def safe_policy_patterns(values: Any, field: str) -> list[str]:
    if not isinstance(values, list) or not values or any(not isinstance(item, str) for item in values):
        raise ValidationError(f"{field} must be a non-empty unique string list")
    if len(values) != len(set(values)):
        raise ValidationError(f"{field} must be a non-empty unique list")
    for item in values:
        if not isinstance(item, str) or not POLICY_PATH.fullmatch(item) or "//" in item or ("*" in item and not item.endswith("/**")):
            raise ValidationError(f"unsafe policy path pattern in {field}: {item}")
    return values


def patterns_overlap(left: str, right: str) -> bool:
    left_root = left.removesuffix("/**").rstrip("/")
    right_root = right.removesuffix("/**").rstrip("/")
    return left_root == right_root or left_root.startswith(right_root + "/") or right_root.startswith(left_root + "/")


def validate_policy(policy: dict[str, Any]) -> None:
    exact_object(policy, {
        "schema_version", "repository", "repository_visibility", "default_branch", "human_owner", "builder_login",
        "environment_name", "ruleset_name", "github_app_slug", "required_checks", "reserved_paths",
        "ordinary_paths", "work_order", "protected_merge",
    }, "policy")
    reject_secret_values(policy)
    if policy["schema_version"] != 1 or policy["default_branch"] != "main":
        raise ValidationError("policy schema/default branch is not the exact v1 contract")
    if policy["repository_visibility"] not in {"public", "private", "internal"}:
        raise ValidationError("policy repository visibility is invalid")
    try:
        owner, repository_name = policy["repository"].split("/", 1)
    except (AttributeError, ValueError) as exc:
        raise ValidationError("policy repository must be owner/name") from exc
    if not LOGIN.fullmatch(owner) or not REPOSITORY_NAME.fullmatch(repository_name):
        raise ValidationError("policy repository identity is invalid")
    if not isinstance(policy["human_owner"], str) or not isinstance(policy["builder_login"], str) or not LOGIN.fullmatch(policy["human_owner"]) or not LOGIN.fullmatch(policy["builder_login"]):
        raise ValidationError("policy owner/builder identity is invalid")
    if str(policy["human_owner"]).lower() == str(policy["builder_login"]).lower():
        raise ValidationError("policy must separate human-owner and builder identities")
    if not isinstance(policy["environment_name"], str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,254}", policy["environment_name"]):
        raise ValidationError("policy Environment name is invalid")
    if not valid_display(policy["ruleset_name"], 100) or not isinstance(policy["github_app_slug"], str) or not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,98}[a-z0-9])?", policy["github_app_slug"]):
        raise ValidationError("policy Ruleset/App identity is invalid")
    if not isinstance(policy["required_checks"], list) or len(policy["required_checks"]) != 2 or any(not isinstance(item, str) for item in policy["required_checks"]) or set(policy["required_checks"]) != EXPECTED_CHECKS:
        raise ValidationError("policy required checks differ from the exact v1 contract")
    reserved = safe_policy_patterns(policy["reserved_paths"], "reserved_paths")
    ordinary = safe_policy_patterns(policy["ordinary_paths"], "ordinary_paths")
    if not MANDATORY_RESERVED.issubset(set(reserved)):
        raise ValidationError("trusted policy is missing mandatory reserved paths")
    if not MANDATORY_ORDINARY.issubset(set(ordinary)):
        raise ValidationError("trusted policy is missing the mandatory Work Order ordinary path")
    if any(patterns_overlap(left, right) for left in reserved for right in ordinary):
        raise ValidationError("trusted policy reserved and ordinary paths overlap")
    if policy["work_order"] != {
        "max_valid_hours": 72,
        "ordinary_risk_class": "B",
        "required_status_for_merge": "verified",
        "required_acceptance_verdict": "PASS",
    }:
        raise ValidationError("policy Work Order settings differ from the exact v1 contract")
    if policy["protected_merge"] != {
        "allowed_risk_classes": ["B"],
        "reserved_paths_allowed": False,
        "allowed_activation_statuses": ["configuration_verified", "active_verified"],
        "require_exact_head_owner_comment": True,
        "token_environment_variable": "AEF_MERGE_TOKEN",
        "merge_method": "squash",
    }:
        raise ValidationError("policy protected-merge settings differ from the exact v1 contract")


def validate_runtime_activation(root: Path, policy: dict[str, Any], allowed_statuses: list[str]) -> None:
    validate_policy(policy)
    if allowed_statuses != ["configuration_verified", "active_verified"]:
        raise ValidationError("trusted policy has an unsafe activation-status contract")
    profile = load_json(root / ".aef/profile.json")
    state = load_json(root / ".aef/onboarding-state.json")
    exact_object(profile, {"schema_version", "project", "distribution", "repository", "governance", "github_app"}, "profile")
    project = exact_object(profile["project"], {"name", "business_goal", "primary_users", "stack"}, "profile.project")
    distribution = exact_object(profile["distribution"], {"product_name", "vendor_name", "support_url", "license_name"}, "profile.distribution")
    repository = exact_object(profile["repository"], {"owner", "name", "default_branch", "visibility", "protected_features_confirmed"}, "profile.repository")
    governance = exact_object(profile["governance"], {"owner_login", "builder_login", "environment_name", "ruleset_name", "required_checks", "reserved_paths", "ordinary_paths"}, "profile.governance")
    app = exact_object(profile["github_app"], {"name", "slug", "homepage_url", "callback_url", "setup_url", "installation_scope", "permissions"}, "profile.github_app")
    reject_secret_values(profile)
    if profile["schema_version"] != 1 or not all((
        valid_display(project["name"], 200),
        valid_display(project["business_goal"], 500),
        valid_display_list(project["primary_users"]),
        valid_display_list(project["stack"]),
        valid_display(distribution["product_name"], 200),
        valid_display(distribution["vendor_name"], 200),
        valid_https(distribution["support_url"]),
        valid_display(distribution["license_name"], 200),
    )):
        raise ValidationError("runtime profile project or distribution is invalid")
    if repository != {
        "owner": policy["repository"].split("/", 1)[0],
        "name": policy["repository"].split("/", 1)[1],
        "default_branch": policy["default_branch"],
        "visibility": policy["repository_visibility"],
        "protected_features_confirmed": True,
    } or repository["visibility"] not in {"public", "private", "internal"}:
        raise ValidationError("runtime profile repository differs from trusted policy")
    if governance != {
        "owner_login": policy["human_owner"],
        "builder_login": policy["builder_login"],
        "environment_name": policy["environment_name"],
        "ruleset_name": policy["ruleset_name"],
        "required_checks": policy["required_checks"],
        "reserved_paths": policy["reserved_paths"],
        "ordinary_paths": policy["ordinary_paths"],
    }:
        raise ValidationError("runtime profile governance differs from trusted policy")
    if not valid_display(governance["ruleset_name"], 100):
        raise ValidationError("runtime profile Ruleset name is invalid")
    if (
        not valid_display(app["name"], 34)
        or app["slug"] != policy["github_app_slug"]
        or not all(valid_https(app[field]) for field in ("homepage_url", "callback_url", "setup_url"))
        or app["installation_scope"] != "selected_repository"
        or app["permissions"] != EXPECTED_APP_PERMISSIONS
    ):
        raise ValidationError("runtime profile GitHub App differs from trusted policy")
    exact_object(state, {"schema_version", "repository", "profile_sha256", "created_at", "updated_at", "activation_status", "steps"}, "onboarding state")
    reject_secret_values(state)
    if state["schema_version"] != 1 or state["repository"] != policy["repository"] or state["profile_sha256"] != digest(profile):
        raise ValidationError("onboarding state profile/repository binding is stale")
    if state["activation_status"] not in allowed_statuses:
        raise ValidationError("onboarding state has not reached configuration_verified")
    created = parse_time(state["created_at"], "state.created_at")
    updated = parse_time(state["updated_at"], "state.updated_at")
    if updated < created:
        raise ValidationError("onboarding state updated_at precedes created_at")
    expected_steps = [
        ("profile_validated", False), ("repository_rendered", False), ("local_checks_green", False),
        ("bootstrap_pr_merged", True), ("canary_checks_observed", False), ("github_app_registered", True),
        ("github_app_installed", True), ("environment_configured", True), ("ruleset_activated", True),
        ("activation_readback_verified", True), ("owner_canary_passed", True),
    ]
    steps = state["steps"]
    complete_count = 10 if state["activation_status"] == "configuration_verified" else 11
    if not isinstance(steps, list) or len(steps) != len(expected_steps):
        raise ValidationError("onboarding state step set is incomplete")
    previous_time = created
    for index, ((step_id, human_gate), entry) in enumerate(zip(expected_steps, steps, strict=True)):
        expected_status = "complete" if index < complete_count else "pending"
        expected_fields = {"id", "human_gate", "status", "actor_type", "completed_at", "evidence_ref"} if expected_status == "complete" else {"id", "human_gate", "status"}
        exact_object(entry, expected_fields, f"onboarding state step {step_id}")
        if entry["id"] != step_id or entry["human_gate"] is not human_gate or entry["status"] != expected_status:
            raise ValidationError(f"onboarding state step is malformed or out of order: {step_id}")
        if expected_status == "complete":
            expected_actor = "human_owner" if human_gate else "local_tool"
            if entry["actor_type"] != expected_actor or not isinstance(entry["evidence_ref"], str) or not entry["evidence_ref"]:
                raise ValidationError(f"onboarding state actor/evidence is invalid for {step_id}")
            completed = parse_time(entry["completed_at"], f"state.steps.{step_id}.completed_at")
            if completed < previous_time or completed > updated:
                raise ValidationError(f"onboarding state timestamp order is invalid for {step_id}")
            if "://" in entry["evidence_ref"]:
                parsed = urlparse(entry["evidence_ref"])
                if parsed.query or parsed.fragment or parsed.username or parsed.password:
                    raise ValidationError(f"onboarding evidence URL is unsafe for {step_id}")
            previous_time = completed
    if previous_time != updated:
        raise ValidationError("onboarding state updated_at does not equal the latest completed step")


def payload_view(work_order: dict[str, Any]) -> dict[str, Any]:
    value = deepcopy(work_order)
    value["approval"]["payload_sha256"] = ZERO_HASH
    value["acceptance_review"] = {
        "verdict": "PENDING",
        "reviewer_subject": None,
        "reviewed_at": None,
        "reviewed_payload_sha256": None,
        "reviewed_scope_sha256": None,
        "evidence_ref": None,
    }
    return value


def payload_sha256(work_order: dict[str, Any]) -> str:
    return digest(payload_view(work_order))


def scope_sha256(work_order: dict[str, Any]) -> str:
    return digest(sorted(work_order["file_allowlist"]))


def candidate_payload_sha256(work_order: dict[str, Any], root: Path, work_order_path: str) -> str:
    entries = []
    for relative in sorted(work_order["file_allowlist"]):
        path = root / relative
        if path.is_symlink():
            raise ValidationError(f"symbolic links are forbidden in governed payloads: {relative}")
        if relative == work_order_path:
            file_digest = payload_sha256(work_order)
            mode = "100755" if path.is_file() and path.stat().st_mode & 0o111 else "100644"
            kind = "work_order"
        else:
            if path.exists() and not path.is_file():
                raise ValidationError(f"governed payload path is not a regular file: {relative}")
            file_digest = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else "absent"
            mode = "100755" if path.is_file() and path.stat().st_mode & 0o111 else "100644" if path.is_file() else None
            kind = "file" if path.is_file() else "absent"
        entries.append({"path": relative, "kind": kind, "mode": mode, "sha256": file_digest})
    return digest(entries)


def strict_json_loads(text: str, *, source: str = "JSON input") -> Any:
    """Parse JSON while rejecting duplicate object keys at every nesting level."""

    def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValidationError(f"duplicate JSON key {key!r} in {source}")
            result[key] = value
        return result

    try:
        return json.loads(text, object_pairs_hook=unique_object)
    except json.JSONDecodeError as exc:
        raise ValidationError(f"strict JSON failed for {source}: {exc}") from exc


def load_json(path: Path) -> dict[str, Any]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ValidationError(f"strict JSON failed for {path}: {exc}") from exc
    value = strict_json_loads(text, source=str(path))
    if not isinstance(value, dict):
        raise ValidationError(f"expected object in {path}")
    return value


def parse_time(value: Any, field: str) -> datetime:
    if not isinstance(value, str):
        raise ValidationError(f"{field} must be an ISO timestamp")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValidationError(f"{field} must be an ISO timestamp") from exc
    if result.tzinfo is None:
        raise ValidationError(f"{field} must be timezone-aware")
    return result.astimezone(UTC)


def safe_paths(values: Any, field: str) -> list[str]:
    if not isinstance(values, list) or not values:
        raise ValidationError(f"{field} must be a non-empty list")
    if any(not isinstance(item, str) or not item for item in values):
        raise ValidationError(f"{field} contains an invalid path")
    if len(values) != len(set(values)):
        raise ValidationError(f"{field} contains duplicates")
    for item in values:
        path = PurePosixPath(item)
        if path.is_absolute() or ".." in path.parts or item.startswith("./") or any(char in item for char in "*?["):
            raise ValidationError(f"unsafe path in {field}: {item}")
    return values


def changed_files(base_ref: str) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{base_ref}...HEAD"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise ValidationError(result.stderr.strip() or f"cannot compare against {base_ref}")
    return [line for line in result.stdout.splitlines() if line]


def is_reserved(path: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatchcase(path, pattern) for pattern in patterns)


def verify_no_credentials(paths: list[str], root: Path) -> None:
    for relative in paths:
        path = root / relative
        if not path.is_file() or path.stat().st_size > 2_000_000:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                raise ValidationError(f"credential-like material detected in {relative}")


def validate_work_order(
    work_order: dict[str, Any],
    *,
    work_order_path: str,
    files: list[str],
    policy: dict[str, Any],
    require_acceptance: bool,
    ordinary_only: bool,
    root: Path | None = None,
    expected_base: str | None = None,
    expected_branch: str | None = None,
) -> None:
    validate_policy(policy)
    required = {
        "id", "title", "status", "risk_class", "business_outcome", "repository_context",
        "in_scope", "out_of_scope", "file_allowlist", "validation", "rollback", "execution_budget",
        "approval", "acceptance_review",
    }
    if set(work_order) != required:
        raise ValidationError(f"Work Order fields differ from the exact v1 contract: {sorted(set(work_order) ^ required)}")
    if not re.fullmatch(r"WO-[0-9]{8}-[0-9]{3}", str(work_order["id"])):
        raise ValidationError("invalid Work Order id")
    if work_order["risk_class"] not in {"A", "B", "C", "D", "X"}:
        raise ValidationError("invalid risk class")
    if work_order["status"] not in {"planned", "executing", "verified", "closed"}:
        raise ValidationError("invalid Work Order status")
    context = work_order["repository_context"]
    if not isinstance(context, dict) or set(context) != {"repository", "branch", "base_commit"}:
        raise ValidationError("invalid repository_context")
    if context["repository"] != policy["repository"] or not SHA.fullmatch(str(context["base_commit"])):
        raise ValidationError("Work Order repository or base commit does not match policy")
    if expected_base and (not SHA.fullmatch(expected_base) or context["base_commit"] != expected_base):
        raise ValidationError("Work Order base commit differs from the exact pull-request base")
    if context["branch"] == policy["default_branch"]:
        raise ValidationError("Work Order branch must not be the default branch")
    github_head = os.environ.get("GITHUB_HEAD_REF")
    if (github_head and github_head != context["branch"]) or (expected_branch and expected_branch != context["branch"]):
        raise ValidationError("Work Order branch differs from the pull-request head branch")
    allowlist = safe_paths(work_order["file_allowlist"], "file_allowlist")
    if work_order_path not in allowlist:
        raise ValidationError("Work Order must allowlist itself")
    unexpected = sorted(set(files) - set(allowlist))
    if unexpected:
        raise ValidationError(f"changed paths outside Work Order allowlist: {unexpected}")
    if not isinstance(work_order["in_scope"], list) or not work_order["in_scope"]:
        raise ValidationError("in_scope must be non-empty")
    if not isinstance(work_order["out_of_scope"], list) or not work_order["out_of_scope"]:
        raise ValidationError("out_of_scope must be non-empty")
    if not isinstance(work_order["validation"], list) or not work_order["validation"]:
        raise ValidationError("validation must be non-empty")
    if not isinstance(work_order["rollback"], str) or not work_order["rollback"].strip():
        raise ValidationError("rollback must be documented")

    budget = work_order["execution_budget"]
    budget_fields = {
        "effort_class", "host_token_budget", "max_builder_rounds", "max_review_rounds",
        "max_parallel_readers", "full_regression_runs", "context_mode", "on_exhaustion",
    }
    if not isinstance(budget, dict) or set(budget) != budget_fields:
        raise ValidationError("execution_budget differs from the exact lean-execution contract")
    effort = budget["effort_class"]
    if effort not in {"small", "standard", "large"}:
        raise ValidationError("execution_budget effort_class is invalid")
    maximum_builder_rounds = 2 if effort == "small" else 3
    maximum_parallel_readers = 1 if effort == "small" else 2
    if type(budget["max_builder_rounds"]) is not int or not 1 <= budget["max_builder_rounds"] <= maximum_builder_rounds:
        raise ValidationError("execution_budget max_builder_rounds exceeds the effort-class limit")
    if type(budget["max_review_rounds"]) is not int or not 1 <= budget["max_review_rounds"] <= 2:
        raise ValidationError("execution_budget max_review_rounds must be one or two")
    if type(budget["max_parallel_readers"]) is not int or not 0 <= budget["max_parallel_readers"] <= maximum_parallel_readers:
        raise ValidationError("execution_budget max_parallel_readers exceeds the effort-class limit")
    token_budget = budget["host_token_budget"]
    if token_budget is not None and (type(token_budget) is not int or not 1000 <= token_budget <= 500000):
        raise ValidationError("execution_budget host_token_budget is invalid")
    if type(budget["full_regression_runs"]) is not int or budget["full_regression_runs"] != 1 or budget["context_mode"] != "minimum_necessary" or budget["on_exhaustion"] != "stop_and_replan":
        raise ValidationError("execution_budget must require one final regression, minimum context and stop-and-replan")

    approval = work_order["approval"]
    expected_approval = {"approver_subject", "issued_at", "valid_until", "payload_sha256", "proof_ref"}
    if not isinstance(approval, dict) or set(approval) != expected_approval:
        raise ValidationError("approval differs from the exact v1 contract")
    issued = parse_time(approval["issued_at"], "approval.issued_at")
    valid_until = parse_time(approval["valid_until"], "approval.valid_until")
    max_hours = policy["work_order"]["max_valid_hours"]
    if valid_until <= issued or (valid_until - issued).total_seconds() > max_hours * 3600:
        raise ValidationError("approval validity window is invalid or too long")
    if valid_until <= datetime.now(UTC):
        raise ValidationError("approval has expired")
    if not approval["approver_subject"] or not approval["proof_ref"]:
        raise ValidationError("approval identity and proof reference are required")
    if approval["approver_subject"] != f"github-owner:{policy['human_owner']}":
        raise ValidationError("approval subject differs from the configured human owner")

    if ordinary_only:
        if work_order["risk_class"] not in policy["protected_merge"]["allowed_risk_classes"]:
            raise ValidationError("protected merge admits only configured ordinary risk classes")
        reserved = [path for path in files if is_reserved(path, policy["reserved_paths"])]
        if reserved:
            raise ValidationError(f"protected merge cannot admit reserved paths: {reserved}")
        unclassified = [path for path in files if not is_reserved(path, policy["ordinary_paths"])]
        if unclassified:
            raise ValidationError(f"protected merge denies paths outside ordinary_paths: {unclassified}")

    if require_acceptance:
        expected_approval_payload = payload_sha256(work_order)
        expected_candidate_payload = candidate_payload_sha256(work_order, root, work_order_path) if root else expected_approval_payload
        if work_order["status"] != policy["work_order"]["required_status_for_merge"]:
            raise ValidationError("Work Order is not verified")
        if approval["payload_sha256"] == ZERO_HASH or approval["payload_sha256"] != expected_approval_payload:
            raise ValidationError("approval payload digest is missing or stale")
        review = work_order["acceptance_review"]
        expected_review = {"verdict", "reviewer_subject", "reviewed_at", "reviewed_payload_sha256", "reviewed_scope_sha256", "evidence_ref"}
        if not isinstance(review, dict) or set(review) != expected_review:
            raise ValidationError("acceptance_review differs from the exact v1 contract")
        if review["verdict"] != policy["work_order"]["required_acceptance_verdict"]:
            raise ValidationError("acceptance verdict is not PASS")
        if review["reviewed_payload_sha256"] != expected_candidate_payload or review["reviewed_scope_sha256"] != scope_sha256(work_order):
            raise ValidationError("acceptance digests are missing or stale")
        if not review["reviewer_subject"] or not review["reviewed_at"] or not review["evidence_ref"]:
            raise ValidationError("acceptance identity, time and evidence are required")
        if not review["reviewer_subject"].startswith("readonly-process:") or review["reviewer_subject"] == approval["approver_subject"]:
            raise ValidationError("acceptance reviewer must be a distinct readonly-process identity")
        if not review["evidence_ref"].startswith("readonly-review:"):
            raise ValidationError("acceptance evidence must be a readonly-review reference")
        parse_time(review["reviewed_at"], "acceptance_review.reviewed_at")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref")
    parser.add_argument("--changed-file", action="append", default=[])
    parser.add_argument("--work-order")
    parser.add_argument("--policy")
    parser.add_argument("--expected-base")
    parser.add_argument("--expected-branch")
    parser.add_argument("--require-acceptance", action="store_true")
    parser.add_argument("--ordinary-only", action="store_true")
    parser.add_argument("--root", default=".")
    args = parser.parse_args(argv)
    try:
        root = Path(args.root).resolve()
        policy = load_json(Path(args.policy).resolve() if args.policy else root / "governance/policy.json")
        files = safe_paths(args.changed_file, "changed_file") if args.changed_file else changed_files(args.base_ref or "origin/main")
        work_orders = [path for path in files if path.startswith("docs/work-orders/") and path.endswith(".json")]
        work_order_path = args.work_order or (work_orders[0] if len(work_orders) == 1 else None)
        if not work_order_path or (not args.work_order and len(work_orders) != 1):
            raise ValidationError("exactly one changed Work Order is required")
        expected_base = args.expected_base
        if not expected_base and args.base_ref:
            resolved = subprocess.run(["git", "rev-parse", f"{args.base_ref}^{{commit}}"], check=False, capture_output=True, text=True)
            if resolved.returncode != 0 or not SHA.fullmatch(resolved.stdout.strip()):
                raise ValidationError(f"cannot resolve exact base {args.base_ref}")
            expected_base = resolved.stdout.strip()
            ancestor = subprocess.run(["git", "merge-base", "--is-ancestor", expected_base, "HEAD"], check=False)
            if ancestor.returncode != 0:
                raise ValidationError("exact Work Order base is not an ancestor of the candidate head")
        work_order = load_json(root / work_order_path)
        validate_work_order(
            work_order,
            work_order_path=work_order_path,
            files=files,
            policy=policy,
            require_acceptance=args.require_acceptance,
            ordinary_only=args.ordinary_only,
            root=root,
            expected_base=expected_base,
            expected_branch=args.expected_branch,
        )
        verify_no_credentials(files, root)
        print(json.dumps({"valid": True, "work_order": work_order["id"], "changed_files": len(files)}, sort_keys=True))
        return 0
    except ValidationError as exc:
        print(f"AEF validation failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
