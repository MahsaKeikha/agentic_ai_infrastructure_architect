from orchestration.orchestrator import InfrastructureOrchestrator


case = {
    "required_capabilities": ["api"],
    "components": ["api", "database"],
    "expected_peak_rps": 50,
    "provisioned_rps": 100,
    "replicas": 2,
    "zones": 2,
    "backups": True,
    "restore_tested": True,
    "estimated_monthly_cost": 400,
    "monthly_budget": 600,
    "security_reviewed": True,
    "rollback_tested": True,
    "human_approved": False,
}

result = InfrastructureOrchestrator().run(case)
assert result["status"] == "awaiting_human_approval"
print(result["status"])
