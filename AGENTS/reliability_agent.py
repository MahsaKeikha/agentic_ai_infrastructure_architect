class ReliabilityAgent:
    name = "reliability"

    def run(self, case: dict) -> dict:
        return {"agent": self.name, "slo": case.get("slo", 0.99), "single_points_of_failure": case.get("single_points_of_failure", [])}
