from orchestration.orchestrator import InfrastructureOrchestrator


case = {
    "required_capabilities": ["api", "queue", "database"],
    "components": ["api", "queue", "database", "cache"],
    "expected_peak_rps": 500,
    "provisioned_rps": 900,
    "replicas": 4,
    "zones": 3,
    "backups": True,
    "restore_tested": True,
    "estimated_monthly_cost": 4200,
    "monthly_budget": 5000,
    "security_reviewed": True,
    "rollback_tested": True,
    "human_approved": True,
    "assumptions": ["traffic estimate reflects p95 peak demand"],
    "conflicts": [],
    "unresolved_questions": [],
}

result = InfrastructureOrchestrator().run(case)
assert result["status"] == "approved"
assert len(result["trace"]) == 5
assert result["evidence"]
print(result["status"])
