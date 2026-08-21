import json
from orchestration.orchestrator import InfrastructureOrchestrator

if __name__ == "__main__":
    print(json.dumps(InfrastructureOrchestrator().run({"peak_demand": 70, "capacity": 100, "budget": 10000, "estimated_cost": 8000}), indent=2))
