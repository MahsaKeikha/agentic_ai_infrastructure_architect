from orchestration.orchestrator import InfrastructureOrchestrator


SCENARIOS = [
    {
        "name": "healthy_multi_zone",
        "case": {
            "required_capabilities": ["api", "queue"],
            "components": ["api", "queue", "database"],
            "expected_peak_rps": 100,
            "provisioned_rps": 180,
            "replicas": 3,
            "zones": 3,
            "backups": True,
            "restore_tested": True,
            "estimated_monthly_cost": 800,
            "monthly_budget": 1000,
            "security_reviewed": True,
            "rollback_tested": True,
            "human_approved": True,
        },
        "expected_status": "approved",
    },
    {
        "name": "capacity_shortfall",
        "case": {
            "required_capabilities": ["api"],
            "components": ["api"],
            "expected_peak_rps": 200,
            "provisioned_rps": 120,
            "replicas": 3,
            "zones": 3,
            "backups": True,
            "restore_tested": True,
            "estimated_monthly_cost": 700,
            "monthly_budget": 1000,
            "security_reviewed": True,
            "rollback_tested": True,
            "human_approved": True,
        },
        "expected_status": "review_required",
    },
    {
        "name": "unreviewed_security",
        "case": {
            "required_capabilities": ["api"],
            "components": ["api"],
            "expected_peak_rps": 80,
            "provisioned_rps": 120,
            "replicas": 2,
            "zones": 2,
            "backups": True,
            "restore_tested": True,
            "estimated_monthly_cost": 600,
            "monthly_budget": 900,
            "security_reviewed": False,
            "rollback_tested": True,
            "human_approved": True,
        },
        "expected_status": "review_required",
    },
]


def main() -> None:
    orchestrator = InfrastructureOrchestrator()
    for scenario in SCENARIOS:
        result = orchestrator.run(scenario["case"])
        assert result["status"] == scenario["expected_status"], (scenario["name"], result)
        print(f"PASS {scenario['name']}: {result['status']}")


if __name__ == "__main__":
    main()
