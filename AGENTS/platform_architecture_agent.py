class PlatformArchitectureAgent:
    name = "platform_architecture"

    def run(self, case: dict) -> dict:
        return {"agent": self.name, "components": case.get("components", []), "constraints": case.get("constraints", [])}
