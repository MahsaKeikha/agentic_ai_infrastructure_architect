from orchestration.orchestrator import InfrastructureOrchestrator


def test_run():
    result = InfrastructureOrchestrator().run({"peak_demand": 10, "capacity": 20, "budget": 100, "estimated_cost": 50})
    assert result["system_id"] == "F40"
    assert result["status"] == "complete"


def test_capacity_blocker():
    result = InfrastructureOrchestrator().run({"peak_demand": 30, "capacity": 20})
    assert result["status"] == "review_required"
