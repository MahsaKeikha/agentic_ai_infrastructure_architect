from AGENTS.platform_architecture_agent import PlatformArchitectureAgent
from AGENTS.capacity_agent import CapacityAgent
from AGENTS.reliability_agent import ReliabilityAgent
from AGENTS.cost_governance_agent import CostGovernanceAgent
from AGENTS.deployment_readiness_agent import DeploymentReadinessAgent


class InfrastructureOrchestrator:
    def __init__(self):
        self.agents = [PlatformArchitectureAgent(), CapacityAgent(), ReliabilityAgent(), CostGovernanceAgent(), DeploymentReadinessAgent()]

    def run(self, case: dict) -> dict:
        analyses, trace = {}, []
        for step, agent in enumerate(self.agents, 1):
            analyses[agent.name] = agent.run(case)
            trace.append({"step": step, "actor": agent.name, "event": "completed"})
        blocked = analyses["capacity"]["headroom"] < 0 or analyses["cost_governance"]["over_budget"] or not analyses["deployment_readiness"]["ready"]
        return {"system_id": "F40", "system_name": "Agentic AI Infrastructure Architect", "version": "0.1.0", "analyses": analyses, "status": "review_required" if blocked else "complete", "trace": trace}
