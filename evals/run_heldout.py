from __future__ import annotations

import json
from pathlib import Path

from orchestration.orchestrator import InfrastructureOrchestrator


SCENARIOS = [
    ("healthy_multi_zone", {"required_capabilities": ["api", "queue"], "components": ["api", "queue", "database"], "expected_peak_rps": 100, "provisioned_rps": 180, "replicas": 3, "zones": 3, "backups": True, "restore_tested": True, "estimated_monthly_cost": 800, "monthly_budget": 1000, "security_reviewed": True, "rollback_tested": True, "human_approved": True}, "approved"),
    ("capacity_shortfall", {"required_capabilities": ["api"], "components": ["api"], "expected_peak_rps": 200, "provisioned_rps": 120, "replicas": 3, "zones": 3, "backups": True, "restore_tested": True, "estimated_monthly_cost": 700, "monthly_budget": 1000, "security_reviewed": True, "rollback_tested": True, "human_approved": True}, "review_required"),
    ("budget_overrun", {"required_capabilities": ["api"], "components": ["api"], "expected_peak_rps": 80, "provisioned_rps": 120, "replicas": 2, "zones": 2, "backups": True, "restore_tested": True, "estimated_monthly_cost": 1200, "monthly_budget": 900, "security_reviewed": True, "rollback_tested": True, "human_approved": True}, "review_required"),
    ("untested_restore", {"required_capabilities": ["api"], "components": ["api", "database"], "expected_peak_rps": 80, "provisioned_rps": 120, "replicas": 2, "zones": 2, "backups": True, "restore_tested": False, "estimated_monthly_cost": 600, "monthly_budget": 900, "security_reviewed": True, "rollback_tested": True, "human_approved": True}, "review_required"),
    ("missing_security_review", {"required_capabilities": ["api"], "components": ["api"], "expected_peak_rps": 80, "provisioned_rps": 120, "replicas": 2, "zones": 2, "backups": True, "restore_tested": True, "estimated_monthly_cost": 600, "monthly_budget": 900, "security_reviewed": False, "rollback_tested": True, "human_approved": True}, "review_required"),
    ("unapproved_but_ready", {"required_capabilities": ["api"], "components": ["api"], "expected_peak_rps": 80, "provisioned_rps": 120, "replicas": 2, "zones": 2, "backups": True, "restore_tested": True, "estimated_monthly_cost": 600, "monthly_budget": 900, "security_reviewed": True, "rollback_tested": True, "human_approved": False}, "awaiting_human_approval"),
    ("conflicting_budget_input", {"required_capabilities": ["api"], "components": ["api"], "expected_peak_rps": 80, "provisioned_rps": 120, "replicas": 2, "zones": 2, "backups": True, "restore_tested": True, "estimated_monthly_cost": 600, "monthly_budget": 900, "security_reviewed": True, "rollback_tested": True, "human_approved": True, "conflicts": [{"field": "monthly_budget", "values": [900, 5000]}]}, "review_required"),
    ("unresolved_dr_question", {"required_capabilities": ["api"], "components": ["api"], "expected_peak_rps": 80, "provisioned_rps": 120, "replicas": 2, "zones": 2, "backups": True, "restore_tested": True, "estimated_monthly_cost": 600, "monthly_budget": 900, "security_reviewed": True, "rollback_tested": True, "human_approved": True, "unresolved_questions": ["Is the target region included in disaster recovery exercises?"]}, "review_required"),
]


def main() -> None:
    orchestrator = InfrastructureOrchestrator()
    records = []
    for name, case, expected in SCENARIOS:
        result = orchestrator.run(case)
        passed = result["status"] == expected
        records.append({"name": name, "expected": expected, "actual": result["status"], "passed": passed})
        assert passed, records[-1]
    summary = {"system_id": "F40", "version": "1.0.0", "scenario_count": len(records), "passed": sum(1 for r in records if r["passed"]), "pass_rate": 1.0, "records": records}
    Path("artifacts").mkdir(exist_ok=True)
    Path("artifacts/heldout_results.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary))


if __name__ == "__main__":
    main()
