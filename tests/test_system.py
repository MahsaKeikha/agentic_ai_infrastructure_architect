from orchestration.orchestrator import InfrastructureOrchestrator


def healthy_case(**overrides):
    case = {
        "required_capabilities": ["api", "queue"],
        "components": ["api", "queue", "database"],
        "expected_peak_rps": 100,
        "provisioned_rps": 180,
        "availability_target": 0.999,
        "replicas": 3,
        "zones": 3,
        "backups": True,
        "restore_tested": True,
        "estimated_monthly_cost": 800,
        "monthly_budget": 1000,
        "security_reviewed": True,
        "rollback_tested": True,
    }
    case.update(overrides)
    return case


def test_ready_requires_human_approval():
    result = InfrastructureOrchestrator().run(healthy_case())
    assert result["status"] == "awaiting_human_approval"
    assert len(result["trace"]) == 5
    assert len(result["evidence"]) == 5


def test_human_approval_promotes_ready_plan():
    result = InfrastructureOrchestrator().run(healthy_case(human_approved=True))
    assert result["status"] == "approved"


def test_capacity_shortfall_fails_closed():
    result = InfrastructureOrchestrator().run(healthy_case(provisioned_rps=50, human_approved=True))
    assert result["status"] == "review_required"
    assert result["analyses"]["capacity"]["sufficient"] is False


def test_missing_capability_fails_closed():
    result = InfrastructureOrchestrator().run(healthy_case(components=["api"], human_approved=True))
    assert result["status"] == "review_required"
    assert result["analyses"]["platform_architecture"]["missing_capabilities"] == ["queue"]


def test_reliability_requires_recovery_controls():
    result = InfrastructureOrchestrator().run(healthy_case(restore_tested=False, human_approved=True))
    assert result["status"] == "review_required"
    assert result["analyses"]["reliability"]["resilient"] is False


def test_budget_overrun_blocks_approval():
    result = InfrastructureOrchestrator().run(healthy_case(estimated_monthly_cost=1400, human_approved=True))
    assert result["status"] == "review_required"
    assert result["analyses"]["cost_governance"]["over_budget"] is True
