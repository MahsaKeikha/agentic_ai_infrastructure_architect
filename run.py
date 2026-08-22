from orchestration.orchestrator import InfrastructureOrchestrator


def main() -> None:
    case = {
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
    }
    print(InfrastructureOrchestrator().run(case))


if __name__ == "__main__":
    main()
