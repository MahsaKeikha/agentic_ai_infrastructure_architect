from __future__ import annotations

from AGENTS.capacity_agent import CapacityAgent
from AGENTS.cost_governance_agent import CostGovernanceAgent
from AGENTS.deployment_readiness_agent import DeploymentReadinessAgent
from AGENTS.platform_architecture_agent import PlatformArchitectureAgent
from AGENTS.reliability_agent import ReliabilityAgent
from orchestration.state import InfrastructureState


class InfrastructureOrchestrator:
    def __init__(self) -> None:
        self.agents = [PlatformArchitectureAgent(), CapacityAgent(), ReliabilityAgent(), CostGovernanceAgent(), DeploymentReadinessAgent()]

    def run(self, case: dict) -> dict:
        state = InfrastructureState(case=dict(case))
        state.approval = {"required": True, "approved": bool(case.get("human_approved", False))}
        for agent in self.agents:
            agent.run(state)
        ready = bool(state.analyses["deployment_readiness"]["ready"])
        approved = bool(state.approval["approved"])
        status = "approved" if ready and approved else "awaiting_human_approval" if ready else "review_required"
        return {
            "system_id": "F40",
            "system_name": "Agentic AI Infrastructure Architect",
            "version": "0.2.0",
            "analyses": state.analyses,
            "status": status,
            "approval": state.approval,
            "escalations": state.escalations,
            "evidence": state.evidence,
            "trace": state.trace,
        }


def run(case: dict) -> dict:
    return InfrastructureOrchestrator().run(case)
