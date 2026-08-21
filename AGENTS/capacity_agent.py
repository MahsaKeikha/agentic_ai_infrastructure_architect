from __future__ import annotations

from SKILLS.capacity_planning import assess_capacity
from orchestration.state import InfrastructureState


class CapacityAgent:
    name = "capacity"

    def run(self, state: InfrastructureState) -> dict:
        result = assess_capacity(state.case)
        if not result["sufficient"]:
            state.escalate(self.name, "provisioned capacity is below expected peak demand", "critical")
        state.record(self.name, result)
        return result
