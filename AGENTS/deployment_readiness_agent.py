from __future__ import annotations

from SKILLS.deployment_readiness import assess_readiness
from orchestration.state import InfrastructureState


class DeploymentReadinessAgent:
    name = "deployment_readiness"

    def run(self, state: InfrastructureState) -> dict:
        result = assess_readiness(state.analyses, state.case, bool(state.escalations))
        if not result["ready"]:
            state.escalate(self.name, "deployment readiness gate failed")
        state.record(self.name, result)
        return result
