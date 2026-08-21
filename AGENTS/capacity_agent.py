class CapacityAgent:
    name = "capacity"

    def run(self, case: dict) -> dict:
        demand = float(case.get("peak_demand", 0))
        capacity = float(case.get("capacity", 0))
        return {"agent": self.name, "peak_demand": demand, "capacity": capacity, "headroom": capacity - demand}
