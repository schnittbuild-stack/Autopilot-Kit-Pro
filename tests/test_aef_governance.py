from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from copy import deepcopy
from datetime import UTC, datetime, timedelta
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import aef_validate  # noqa: E402
import aef_merge  # noqa: E402


class GovernanceTests(unittest.TestCase):
    def setUp(self) -> None:
        github_head_ref = patch.dict(os.environ, {"GITHUB_HEAD_REF": ""})
        github_head_ref.start()
        self.addCleanup(github_head_ref.stop)
        self.policy = json.loads((ROOT / "governance/policy.json").read_text(encoding="utf-8"))
        issued = datetime.now(UTC).replace(microsecond=0)
        self.path = "docs/work-orders/WO-20990101-001-example.json"
        self.work_order = {
            "id": "WO-20990101-001",
            "title": "Example ordinary change",
            "status": "executing",
            "risk_class": "B",
            "business_outcome": "Create one tested ordinary source file.",
            "repository_context": {
                "repository": self.policy["repository"],
                "branch": "feature/example",
                "base_commit": "a" * 40,
            },
            "in_scope": ["Create src/example.py"],
            "out_of_scope": ["No deployment or live effect"],
            "file_allowlist": [self.path, "src/example.py"],
            "validation": ["python3 -m unittest"],
            "rollback": "Revert the feature commit through a reviewed Work Order.",
            "execution_budget": {
                "effort_class": "small",
                "host_token_budget": None,
                "max_builder_rounds": 2,
                "max_review_rounds": 2,
                "max_parallel_readers": 1,
                "full_regression_runs": 1,
                "context_mode": "minimum_necessary",
                "on_exhaustion": "stop_and_replan",
            },
            "approval": {
                "approver_subject": f"github-owner:{self.policy['human_owner']}",
                "issued_at": issued.isoformat(),
                "valid_until": (issued + timedelta(hours=1)).isoformat(),
                "payload_sha256": aef_validate.ZERO_HASH,
                "proof_ref": "authenticated-owner-session:example",
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

    def test_executing_ordinary_scope_validates_before_acceptance(self) -> None:
        aef_validate.validate_work_order(
            self.work_order,
            work_order_path=self.path,
            files=[self.path, "src/example.py"],
            policy=self.policy,
            require_acceptance=False,
            ordinary_only=True,
        )

    def test_reserved_path_is_rejected_by_protected_merge(self) -> None:
        candidate = deepcopy(self.work_order)
        candidate["file_allowlist"].append(".github/workflows/changed.yml")
        with self.assertRaisesRegex(aef_validate.ValidationError, "reserved"):
            aef_validate.validate_work_order(
                candidate,
                work_order_path=self.path,
                files=[self.path, ".github/workflows/changed.yml"],
                policy=self.policy,
                require_acceptance=False,
                ordinary_only=True,
            )
        candidate["file_allowlist"] = [self.path, ".codex/config.toml"]
        with self.assertRaisesRegex(aef_validate.ValidationError, "reserved"):
            aef_validate.validate_work_order(
                candidate,
                work_order_path=self.path,
                files=[self.path, ".codex/config.toml"],
                policy=self.policy,
                require_acceptance=False,
                ordinary_only=True,
            )

    def test_unclassified_or_deployment_path_is_default_denied(self) -> None:
        for dangerous in ("Dockerfile", "vercel.json", "scripts/deploy.py"):
            candidate = deepcopy(self.work_order)
            candidate["file_allowlist"] = [self.path, dangerous]
            with self.assertRaisesRegex(aef_validate.ValidationError, "outside ordinary_paths"):
                aef_validate.validate_work_order(
                    candidate,
                    work_order_path=self.path,
                    files=[self.path, dangerous],
                    policy=self.policy,
                    require_acceptance=False,
                    ordinary_only=True,
                )

    def test_acceptance_digest_is_bound_to_semantic_payload(self) -> None:
        candidate = deepcopy(self.work_order)
        candidate["status"] = "verified"
        approval_payload = aef_validate.payload_sha256(candidate)
        candidate["approval"]["payload_sha256"] = approval_payload
        candidate_payload = aef_validate.candidate_payload_sha256(candidate, ROOT, self.path)
        candidate["acceptance_review"] = {
            "verdict": "PASS",
            "reviewer_subject": "readonly-process:example",
            "reviewed_at": datetime.now(UTC).isoformat(),
            "reviewed_payload_sha256": candidate_payload,
            "reviewed_scope_sha256": aef_validate.scope_sha256(candidate),
            "evidence_ref": "readonly-review:pass",
        }
        aef_validate.validate_work_order(
            candidate,
            work_order_path=self.path,
            files=[self.path, "src/example.py"],
            policy=self.policy,
            require_acceptance=True,
            ordinary_only=True,
            root=ROOT,
        )
        candidate["business_outcome"] = "Changed after acceptance"
        with self.assertRaisesRegex(aef_validate.ValidationError, "stale"):
            aef_validate.validate_work_order(
                candidate,
                work_order_path=self.path,
                files=[self.path, "src/example.py"],
                policy=self.policy,
                require_acceptance=True,
                ordinary_only=True,
            )

    def test_candidate_digest_changes_with_allowed_file_content(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "src").mkdir()
            target = root / "src/example.py"
            target.write_text("VALUE = 1\n", encoding="utf-8")
            first = aef_validate.candidate_payload_sha256(self.work_order, root, self.path)
            target.write_text("VALUE = 2\n", encoding="utf-8")
            second = aef_validate.candidate_payload_sha256(self.work_order, root, self.path)
            self.assertNotEqual(first, second)
            target.chmod(0o755)
            executable = aef_validate.candidate_payload_sha256(self.work_order, root, self.path)
            self.assertNotEqual(second, executable)
            target.unlink()
            target.symlink_to("outside.py")
            with self.assertRaisesRegex(aef_validate.ValidationError, "symbolic links"):
                aef_validate.candidate_payload_sha256(self.work_order, root, self.path)

    def test_work_order_allowlist_rejects_globs(self) -> None:
        with self.assertRaisesRegex(aef_validate.ValidationError, "unsafe path"):
            aef_validate.safe_paths(["src/**"], "file_allowlist")

    def test_execution_budget_prevents_open_ended_agent_loops(self) -> None:
        for field, value in (
            ("max_builder_rounds", 3),
            ("max_review_rounds", 3),
            ("max_parallel_readers", 2),
            ("full_regression_runs", 2),
            ("full_regression_runs", True),
            ("context_mode", "load_everything"),
            ("on_exhaustion", "continue_anyway"),
        ):
            candidate = deepcopy(self.work_order)
            candidate["execution_budget"][field] = value
            with self.assertRaisesRegex(aef_validate.ValidationError, "execution_budget"):
                aef_validate.validate_work_order(
                    candidate,
                    work_order_path=self.path,
                    files=[self.path, "src/example.py"],
                    policy=self.policy,
                    require_acceptance=False,
                    ordinary_only=True,
                )
        for invalid_token_budget in (True, 999, 500001):
            candidate = deepcopy(self.work_order)
            candidate["execution_budget"]["host_token_budget"] = invalid_token_budget
            with self.assertRaisesRegex(aef_validate.ValidationError, "host_token_budget"):
                aef_validate.validate_work_order(
                    candidate,
                    work_order_path=self.path,
                    files=[self.path, "src/example.py"],
                    policy=self.policy,
                    require_acceptance=False,
                    ordinary_only=True,
                )

    def test_strict_json_rejects_duplicate_top_level_and_nested_keys(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "duplicate.json"
            for content in (
                '{"status":"executing","status":"verified"}',
                '{"approval":{"proof_ref":"first","proof_ref":"second"}}',
            ):
                path.write_text(content, encoding="utf-8")
                with self.assertRaisesRegex(aef_validate.ValidationError, "duplicate JSON key"):
                    aef_validate.load_json(path)

    def test_merge_guard_uses_trusted_validator_and_checks_rename_source(self) -> None:
        merge_guard = (ROOT / "scripts/aef_merge.py").read_text(encoding="utf-8")
        drift_guard = (ROOT / ".github/workflows/aef-drift-monitor.yml").read_text(encoding="utf-8")
        protected_workflow = (ROOT / ".github/workflows/aef-protected-merge.yml").read_text(encoding="utf-8")
        self.assertIn("trusted_validator", merge_guard)
        self.assertIn("trusted_policy", merge_guard)
        self.assertIn("previous_filename", merge_guard)
        self.assertIn("aef_validate.load_json(trusted_policy)", merge_guard)
        self.assertIn("permission-actions: read", drift_guard)
        self.assertIn("deployment_protection_rules", drift_guard)
        self.assertIn("total_count", drift_guard)
        self.assertIn("additional pull-request parameters", drift_guard)
        quoted_environment = json.dumps(self.policy["environment_name"])
        self.assertIn(f"environment: {quoted_environment}", drift_guard)
        self.assertIn(f"ENVIRONMENT_NAME: {quoted_environment}", drift_guard)
        self.assertIn(f"environment: {quoted_environment}", protected_workflow)

        shape_cases = [
            (
                'type == "object" and .name == $n and .deployment_branch_policy == {"protected_branches":false,"custom_branch_policies":true} and (.protection_rules | type == "array" and length == 1 and all(.[]; type == "object" and .type == "branch_policy"))',
                ["--arg", "n", self.policy["environment_name"]],
                {"name": self.policy["environment_name"], "deployment_branch_policy": {"protected_branches": False, "custom_branch_policies": True}, "protection_rules": [{"type": "branch_policy"}]},
                {"name": self.policy["environment_name"], "deployment_branch_policy": {"protected_branches": False, "custom_branch_policies": True}, "protection_rules": {"forged": {"type": "branch_policy"}}},
            ),
            (
                'type == "array" and length >= 1 and all(.[]; type == "object" and has("branch_policies") and (.branch_policies | type == "array") and has("total_count") and (.total_count | type == "number" and . >= 0 and floor == .)) and ([.[].branch_policies[]] as $items | all($items[]; type == "object" and (.name | type == "string")) and ([.[].total_count] | unique) == [($items | length)] and [$items[].name] == [$b])',
                ["--arg", "b", self.policy["default_branch"]],
                [{"total_count": 1, "branch_policies": [{"name": self.policy["default_branch"]}]}],
                [{"total_count": 1, "branch_policies": {"forged": {"name": self.policy["default_branch"]}}}],
            ),
            (
                'type == "array" and length >= 1 and all(.[]; type == "object" and has("secrets") and (.secrets | type == "array") and has("total_count") and (.total_count | type == "number" and . >= 0 and floor == .)) and ([.[].secrets[]] as $items | all($items[]; type == "object" and (.name | type == "string" and length > 0)) and ([.[].total_count] | unique) == [($items | length)] and ($items | map(.name) | unique | length) == ($items | length) and (["AEF_APP_ID", "AEF_PRIVATE_KEY"] - ($items | map(.name)) | length) == 0)',
                [],
                [{"total_count": 3, "secrets": [{"name": "AEF_APP_ID"}, {"name": "AEF_PRIVATE_KEY"}, {"name": "CUSTOMER_SECRET"}]}],
                [{"total_count": 2, "secrets": {"first": {"name": "AEF_APP_ID"}, "second": {"name": "AEF_PRIVATE_KEY"}}}],
            ),
            (
                'type == "array" and length >= 1 and all(.[]; type == "object" and has("custom_deployment_protection_rules") and (.custom_deployment_protection_rules | type == "array") and has("total_count") and (.total_count | type == "number" and . >= 0 and floor == .)) and ([.[].custom_deployment_protection_rules[]] as $items | all($items[]; type == "object") and ([.[].total_count] | unique) == [($items | length)] and $items == [])',
                [],
                [{"total_count": 0, "custom_deployment_protection_rules": []}],
                [{"total_count": 0, "custom_deployment_protection_rules": {}}],
            ),
            (
                'type == "array" and length >= 1 and all(.[]; type == "object" and has("repositories") and (.repositories | type == "array") and has("total_count") and (.total_count | type == "number" and . >= 0 and floor == .)) and ([.[].repositories[]] as $items | all($items[]; type == "object" and (.full_name | type == "string")) and ([.[].total_count] | unique) == [($items | length)] and [$items[].full_name] == [$r])',
                ["--arg", "r", self.policy["repository"]],
                [{"total_count": 1, "repositories": [{"full_name": self.policy["repository"]}]}],
                [{"total_count": 1, "repositories": {"forged": {"full_name": self.policy["repository"]}}}],
            ),
        ]
        for expression, arguments, valid_payload, malformed_payload in shape_cases:
            self.assertIn(expression, drift_guard)
            valid = subprocess.run(
                ["jq", "-e", *arguments, expression],
                input=json.dumps(valid_payload),
                check=False,
                capture_output=True,
                text=True,
            )
            malformed = subprocess.run(
                ["jq", "-e", *arguments, expression],
                input=json.dumps(malformed_payload),
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(valid.returncode, 0, valid.stderr)
            self.assertNotEqual(malformed.returncode, 0, malformed.stdout + malformed.stderr)

        secret_expression = shape_cases[2][0]
        for invalid_secrets in (
            [{"total_count": 1, "secrets": [{"name": "AEF_APP_ID"}]}],
            [{"total_count": 3, "secrets": [{"name": "AEF_APP_ID"}, {"name": "AEF_APP_ID"}, {"name": "AEF_PRIVATE_KEY"}]}],
        ):
            result = subprocess.run(
                ["jq", "-e", secret_expression],
                input=json.dumps(invalid_secrets),
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0, invalid_secrets)

        ruleset_expression = 'type == "object" and .enforcement == "active" and .target == "branch" and .conditions == {"ref_name":{"include":["~DEFAULT_BRANCH"],"exclude":[]}} and .bypass_actors == [] and (.rules | type == "array" and all(.[]; type == "object" and (.type | type == "string" and length > 0)) and ([.[].type] as $types | ($types | map(select(. == "deletion")) | length) == 1 and ($types | map(select(. == "non_fast_forward")) | length) == 1 and ($types | map(select(. == "pull_request")) | length) == 1 and ($types | map(select(. == "required_status_checks")) | length) == 1))'
        status_expression = '[.rules[] | select(.type == "required_status_checks")] as $rules | ($rules | length) == 1 and ($rules[0].parameters | type == "object" and has("strict_required_status_checks_policy") and has("do_not_enforce_on_create") and has("required_status_checks") and .strict_required_status_checks_policy == true and .do_not_enforce_on_create == false and (.required_status_checks | type == "array" and all(.[]; type == "object" and (keys | sort) == ["context","integration_id"] and (.context | type == "string" and length > 0) and (.integration_id | type == "number" and . >= 1 and floor == .)) and ([.[].context] | unique | length) == length and (($expected - .) | length) == 0))'
        pull_expression = '[.rules[] | select(.type == "pull_request")] as $rules | ($rules | length) == 1 and ($rules[0].parameters | type == "object" and .dismiss_stale_reviews_on_push == true and .require_code_owner_review == true and .require_last_push_approval == false and .required_approving_review_count == 0 and .required_review_thread_resolution == true)'
        self.assertIn(f"'{ruleset_expression}' ruleset.json", drift_guard)
        self.assertIn(f"'{status_expression}' ruleset.json", drift_guard)
        self.assertIn(f"'{pull_expression}' ruleset.json", drift_guard)
        expected_checks = [
            {"context": name, "integration_id": 15368}
            for name in self.policy["required_checks"]
        ]
        ruleset = {
            "enforcement": "active",
            "target": "branch",
            "conditions": {"ref_name": {"include": ["~DEFAULT_BRANCH"], "exclude": []}},
            "bypass_actors": [],
            "rules": [
                {"type": "deletion"},
                {"type": "non_fast_forward"},
                {"type": "pull_request", "parameters": {
                    "dismiss_stale_reviews_on_push": True,
                    "require_code_owner_review": True,
                    "require_last_push_approval": False,
                    "required_approving_review_count": 0,
                    "required_review_thread_resolution": True,
                }},
                {"type": "required_status_checks", "parameters": {
                    "strict_required_status_checks_policy": True,
                    "do_not_enforce_on_create": False,
                    "required_status_checks": expected_checks,
                }},
            ],
        }
        detail_valid = subprocess.run(
            ["jq", "-e", ruleset_expression],
            input=json.dumps(ruleset),
            check=False,
            capture_output=True,
            text=True,
        )
        status_valid = subprocess.run(
            ["jq", "-e", "--argjson", "expected", json.dumps(expected_checks), status_expression],
            input=json.dumps(ruleset),
            check=False,
            capture_output=True,
            text=True,
        )
        pull_valid = subprocess.run(
            ["jq", "-e", pull_expression],
            input=json.dumps(ruleset),
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(detail_valid.returncode, 0, detail_valid.stderr)
        self.assertEqual(status_valid.returncode, 0, status_valid.stderr)
        self.assertEqual(pull_valid.returncode, 0, pull_valid.stderr)

        additive = deepcopy(ruleset)
        additive["rules"].append({"type": "required_signatures"})
        additive["rules"][2]["parameters"]["future_github_field"] = True
        additive["rules"][3]["parameters"]["required_status_checks"].append(
            {"context": "Customer Integration / verify", "integration_id": 15368}
        )
        for command, expression in (
            (["jq", "-e", ruleset_expression], ruleset_expression),
            (["jq", "-e", "--argjson", "expected", json.dumps(expected_checks), status_expression], status_expression),
            (["jq", "-e", pull_expression], pull_expression),
        ):
            result = subprocess.run(
                command,
                input=json.dumps(additive),
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, expression + result.stderr)

        for invalid_checks in (
            [deepcopy(expected_checks[0]), deepcopy(expected_checks[0]), deepcopy(expected_checks[1])],
            [deepcopy(expected_checks[0])],
        ):
            malformed = deepcopy(ruleset)
            malformed["rules"][3]["parameters"]["required_status_checks"] = invalid_checks
            result = subprocess.run(
                ["jq", "-e", "--argjson", "expected", json.dumps(expected_checks), status_expression],
                input=json.dumps(malformed),
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0, invalid_checks)
        for invalid_id in (True, "15368", -1, 1.5):
            malformed = deepcopy(ruleset)
            malformed["rules"][3]["parameters"]["required_status_checks"][0]["integration_id"] = invalid_id
            result = subprocess.run(
                ["jq", "-e", "--argjson", "expected", json.dumps(expected_checks), status_expression],
                input=json.dumps(malformed),
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0, invalid_id)
        invalid_rule_sets = (
            [*deepcopy(ruleset["rules"]), "MALFORMED"],
            deepcopy(ruleset["rules"][1:]),
            [deepcopy(ruleset["rules"][0]), *deepcopy(ruleset["rules"])],
        )
        for invalid_rules in invalid_rule_sets:
            malformed = deepcopy(ruleset)
            malformed["rules"] = invalid_rules
            result = subprocess.run(
                ["jq", "-e", ruleset_expression],
                input=json.dumps(malformed),
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0, invalid_rules)

    def test_mandatory_reserved_guards_cannot_be_removed(self) -> None:
        weakened = deepcopy(self.policy)
        weakened["reserved_paths"].remove(".aef/**")
        with self.assertRaisesRegex(aef_validate.ValidationError, "mandatory reserved"):
            aef_validate.validate_work_order(
                self.work_order,
                work_order_path=self.path,
                files=[self.path, "src/example.py"],
                policy=weakened,
                require_acceptance=False,
                ordinary_only=True,
            )

    def test_owner_directive_and_check_producer_are_exact(self) -> None:
        original_api = aef_merge.api
        head = "a" * 40
        try:
            aef_merge.api = lambda method, endpoint, token: [
                {"user": {"login": self.policy["human_owner"]}, "body": f"AEF-APPROVE {head}"}
            ]
            aef_merge.require_exact_head_owner_comment(
                self.policy["repository"], 1, head, self.policy["human_owner"], "token"
            )
            aef_merge.api = lambda method, endpoint, token: {
                "check_runs": [
                    {"name": self.policy["required_checks"][0], "conclusion": "success", "app": {"slug": "github-actions"}},
                    {"name": self.policy["required_checks"][0], "conclusion": "failure", "app": {"slug": "github-actions"}},
                ]
            }
            with self.assertRaisesRegex(aef_merge.MergeError, "required checks"):
                aef_merge.required_checks(
                    self.policy["repository"], head, "token", [self.policy["required_checks"][0]]
                )
        finally:
            aef_merge.api = original_api

    def test_activation_profile_is_bound_to_trusted_policy(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / ".aef").mkdir()
            profile = json.loads((ROOT / ".aef/profile.json").read_text(encoding="utf-8"))
            state = json.loads((ROOT / ".aef/onboarding-state.json").read_text(encoding="utf-8"))
            completed_at = datetime.now(UTC).isoformat()
            for entry in state["steps"][:10]:
                entry.update({
                    "status": "complete",
                    "actor_type": "human_owner" if entry["human_gate"] else "local_tool",
                    "completed_at": completed_at,
                    "evidence_ref": f"test:{entry['id']}",
                })
            state["activation_status"] = "configuration_verified"
            state["updated_at"] = completed_at
            (root / ".aef/profile.json").write_text(json.dumps(profile), encoding="utf-8")
            (root / ".aef/onboarding-state.json").write_text(json.dumps(state), encoding="utf-8")
            aef_merge.validate_activation(
                root, self.policy, self.policy["protected_merge"]["allowed_activation_statuses"]
            )
            profile["governance"]["builder_login"] = self.policy["human_owner"]
            (root / ".aef/profile.json").write_text(json.dumps(profile), encoding="utf-8")
            with self.assertRaisesRegex(aef_merge.MergeError, "differs from trusted policy"):
                aef_merge.validate_activation(
                    root, self.policy, self.policy["protected_merge"]["allowed_activation_statuses"]
                )

    def test_runtime_contracts_reject_unknown_fields_and_secret_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / ".aef").mkdir()
            profile = json.loads((ROOT / ".aef/profile.json").read_text(encoding="utf-8"))
            state = json.loads((ROOT / ".aef/onboarding-state.json").read_text(encoding="utf-8"))
            completed_at = datetime.now(UTC).isoformat()
            for entry in state["steps"][:10]:
                entry.update({
                    "status": "complete",
                    "actor_type": "human_owner" if entry["human_gate"] else "local_tool",
                    "completed_at": completed_at,
                    "evidence_ref": f"test:{entry['id']}",
                })
            state["activation_status"] = "configuration_verified"
            state["updated_at"] = completed_at
            profile["unexpected"] = "value"
            state["profile_sha256"] = aef_validate.digest(profile)
            (root / ".aef/profile.json").write_text(json.dumps(profile), encoding="utf-8")
            (root / ".aef/onboarding-state.json").write_text(json.dumps(state), encoding="utf-8")
            with self.assertRaisesRegex(aef_merge.MergeError, "profile fields"):
                aef_merge.validate_activation(root, self.policy, self.policy["protected_merge"]["allowed_activation_statuses"])
            profile.pop("unexpected")
            state["profile_sha256"] = aef_validate.digest(profile)
            state["steps"][0]["evidence_ref"] = "AKIA1234567890ABCDEF"
            (root / ".aef/profile.json").write_text(json.dumps(profile), encoding="utf-8")
            (root / ".aef/onboarding-state.json").write_text(json.dumps(state), encoding="utf-8")
            with self.assertRaisesRegex(aef_merge.MergeError, "credential-like"):
                aef_merge.validate_activation(root, self.policy, self.policy["protected_merge"]["allowed_activation_statuses"])


if __name__ == "__main__":
    unittest.main()
