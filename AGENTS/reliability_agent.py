from __future__ import annotations

from SKILLS.reliability_design import design_reliability
from orchestration.state import InfrastructureState


class ReliabilityAgent:
    name = "reliability"

    def run(self, state: InfrastructureState) -> dict:
        result = design_reliability(state.case)
        if not result["resilient"]:
            state.escalate(self.name, "resilience controls do not satisfy multi-zone and recoverability expectations")
        state.record(self.name, result)
        return result
