from orchestration.orchestrator import InfrastructureOrchestrator


def base_case() -> dict:
    return {
        "required_capabilities": ["api"],
        "components": ["api", "database"],
        "expected_peak_rps": 100,
        "provisioned_rps": 200,
        "replicas": 3,
        "zones": 3,
        "backups": True,
        "restore_tested": True,
        "estimated_monthly_cost": 800,
        "monthly_budget": 1000,
        "security_reviewed": True,
        "rollback_tested": True,
        "human_approved": True,
    }


def test_human_approval_cannot_override_security_failure():
    case = base_case()
    case["security_reviewed"] = False
    result = InfrastructureOrchestrator().run(case)
    assert result["status"] == "review_required"


def test_conflicting_inputs_fail_closed():
    case = base_case()
    case["conflicts"] = [{"field": "monthly_budget", "values": [1000, 5000]}]
    result = InfrastructureOrchestrator().run(case)
    assert result["status"] == "review_required"
    assert result["conflicts"]
    assert result["open_risks"]


def test_unresolved_question_fails_closed():
    case = base_case()
    case["unresolved_questions"] = ["Has disaster recovery been exercised in the target region?"]
    result = InfrastructureOrchestrator().run(case)
    assert result["status"] == "review_required"
    assert result["unresolved_questions"]


def test_missing_required_capability_blocks_deployment():
    case = base_case()
    case["required_capabilities"] = ["api", "queue"]
    case["components"] = ["api", "database"]
    result = InfrastructureOrchestrator().run(case)
    assert result["status"] == "review_required"
