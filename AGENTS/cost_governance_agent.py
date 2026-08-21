class CostGovernanceAgent:
    name = "cost_governance"

    def run(self, case: dict) -> dict:
        budget = float(case.get("budget", 0))
        estimate = float(case.get("estimated_cost", 0))
        return {"agent": self.name, "budget": budget, "estimated_cost": estimate, "over_budget": estimate > budget if budget else False}
