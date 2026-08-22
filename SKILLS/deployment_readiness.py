from __future__ import annotations


def assess_readiness(analyses: dict, case: dict, has_escalations: bool) -> dict:
    checks = {
        "architecture_valid": bool(analyses.get("platform_architecture", {}).get("architecture_valid", False)),
        "capacity_sufficient": bool(analyses.get("capacity", {}).get("sufficient", False)),
        "resilient": bool(analyses.get("reliability", {}).get("resilient", False)),
        "within_budget": not bool(analyses.get("cost_governance", {}).get("over_budget", False)),
        "security_reviewed": bool(case.get("security_reviewed", False)),
        "rollback_tested": bool(case.get("rollback_tested", False)),
    }
    return {"checks": checks, "ready": all(checks.values()) and not has_escalations}
