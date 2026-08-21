from __future__ import annotations

from SKILLS.cost_governance import govern_cost
from orchestration.state import InfrastructureState


class CostGovernanceAgent:
    name = "cost_governance"

    def run(self, state: InfrastructureState) -> dict:
        result = govern_cost(state.case)
        if result["over_budget"]:
            state.escalate(self.name, "estimated monthly cost exceeds budget")
        state.record(self.name, result)
        return result
