#!/usr/bin/env python3
"""Create and bind strict AEF Work Orders without external effects."""

from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime, timedelta
from pathlib import Path

from aef_validate import ZERO_HASH, candidate_payload_sha256, load_json, payload_sha256, scope_sha256


def now() -> datetime:
    return datetime.now(UTC).replace(microsecond=0)


def iso(value: datetime) -> str:
    return value.isoformat().replace("+00:00", "Z")


def write(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def command_new(args: argparse.Namespace) -> int:
    if args.host_token_budget is not None and not 1000 <= args.host_token_budget <= 500000:
        raise SystemExit("--host-token-budget must be between 1000 and 500000")
    issued = now()
    work_order_path = f"docs/work-orders/{args.id}-{args.slug}.json"
    allowlist = sorted(set([work_order_path, *args.allow_path]))
    builder_rounds = {"small": 2, "standard": 3, "large": 3}[args.effort_class]
    parallel_readers = 1 if args.effort_class == "small" else 2
    document = {
        "id": args.id,
        "title": args.title,
        "status": "executing",
        "risk_class": args.risk_class,
        "business_outcome": args.business_outcome,
        "repository_context": {
            "repository": "schnittbuild-stack/Autopilot-Kit-Pro",
            "branch": args.branch,
            "base_commit": args.base_commit,
        },
        "in_scope": args.in_scope,
        "out_of_scope": args.out_of_scope,
        "file_allowlist": allowlist,
        "validation": args.validation,
        "rollback": args.rollback,
        "execution_budget": {
            "effort_class": args.effort_class,
            "host_token_budget": args.host_token_budget,
            "max_builder_rounds": builder_rounds,
            "max_review_rounds": 2,
            "max_parallel_readers": parallel_readers,
            "full_regression_runs": 1,
            "context_mode": "minimum_necessary",
            "on_exhaustion": "stop_and_replan",
        },
        "approval": {
            "approver_subject": "github-owner:schnittbuild-stack",
            "issued_at": iso(issued),
            "valid_until": iso(issued + timedelta(hours=args.valid_hours)),
            "payload_sha256": ZERO_HASH,
            "proof_ref": args.approval_proof_ref,
        },
        "acceptance_review": {
            "verdict": "PENDING",
            "reviewer_subject": None,
            "reviewed_at": None,
            "reviewed_payload_sha256": None,
            "reviewed_scope_sha256": None,
            "evidence_ref": None,
        },
    }
    target = Path(work_order_path)
    if target.exists():
        raise SystemExit(f"Refusing to overwrite {target}")
    write(target, document)
    print(target)
    return 0


def command_bind(args: argparse.Namespace) -> int:
    path = Path(args.work_order)
    try:
        work_order_path = path.resolve().relative_to(Path.cwd().resolve()).as_posix()
    except ValueError as exc:
        raise SystemExit("Work Order must be inside the current repository") from exc
    document = load_json(path)
    if work_order_path not in document.get("file_allowlist", []):
        raise SystemExit("Work Order must allowlist its own repository-relative path")
    if not args.reviewer_subject.startswith("readonly-process:") or args.reviewer_subject == document.get("approval", {}).get("approver_subject"):
        raise SystemExit("Reviewer must be a distinct readonly-process identity")
    if not args.evidence_ref.startswith("readonly-review:"):
        raise SystemExit("Review evidence must be a readonly-review reference")
    document["status"] = "verified"
    document["approval"]["payload_sha256"] = ZERO_HASH
    document["acceptance_review"] = {
        "verdict": "PENDING",
        "reviewer_subject": None,
        "reviewed_at": None,
        "reviewed_payload_sha256": None,
        "reviewed_scope_sha256": None,
        "evidence_ref": None,
    }
    approval_payload = payload_sha256(document)
    document["approval"]["payload_sha256"] = approval_payload
    candidate_payload = candidate_payload_sha256(document, Path.cwd(), work_order_path)
    document["acceptance_review"] = {
        "verdict": "PASS",
        "reviewer_subject": args.reviewer_subject,
        "reviewed_at": iso(now()),
        "reviewed_payload_sha256": candidate_payload,
        "reviewed_scope_sha256": scope_sha256(document),
        "evidence_ref": args.evidence_ref,
    }
    write(path, document)
    print(json.dumps({"bound": str(path), "approval_payload_sha256": approval_payload, "candidate_payload_sha256": candidate_payload, "scope_sha256": scope_sha256(document)}, sort_keys=True))
    return 0


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser()
    commands = root.add_subparsers(dest="command", required=True)
    new = commands.add_parser("new")
    new.add_argument("--id", required=True)
    new.add_argument("--slug", required=True)
    new.add_argument("--title", required=True)
    new.add_argument("--branch", required=True)
    new.add_argument("--base-commit", required=True)
    new.add_argument("--risk-class", default="B", choices=("A", "B", "C", "D", "X"))
    new.add_argument("--business-outcome", required=True)
    new.add_argument("--in-scope", action="append", required=True)
    new.add_argument("--out-of-scope", action="append", required=True)
    new.add_argument("--allow-path", action="append", required=True)
    new.add_argument("--validation", action="append", required=True)
    new.add_argument("--rollback", required=True)
    new.add_argument("--effort-class", choices=("small", "standard", "large"), default="small")
    new.add_argument("--host-token-budget", type=int)
    new.add_argument("--approval-proof-ref", required=True)
    new.add_argument("--valid-hours", type=int, default=72, choices=range(1, 73))
    bind = commands.add_parser("bind")
    bind.add_argument("work_order")
    bind.add_argument("--reviewer-subject", required=True)
    bind.add_argument("--evidence-ref", required=True)
    return root


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    return command_new(args) if args.command == "new" else command_bind(args)


if __name__ == "__main__":
    raise SystemExit(main())
