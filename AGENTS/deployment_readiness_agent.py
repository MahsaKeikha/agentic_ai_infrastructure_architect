class DeploymentReadinessAgent:
    name = "deployment_readiness"

    def run(self, case: dict) -> dict:
        blockers = case.get("deployment_blockers", [])
        return {"agent": self.name, "blockers": blockers, "ready": not blockers}
