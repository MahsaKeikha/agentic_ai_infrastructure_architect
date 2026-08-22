from __future__ import annotations

from SKILLS.topology_design import assess_topology
from orchestration.state import InfrastructureState


class PlatformArchitectureAgent:
    name = "platform_architecture"

    def run(self, state: InfrastructureState) -> dict:
        result = assess_topology(state.case)
        if result["missing_capabilities"]:
            state.escalate(self.name, f"missing capabilities: {', '.join(result['missing_capabilities'])}")
        state.record(self.name, result)
        return result
