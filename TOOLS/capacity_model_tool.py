def utilization(demand: float, capacity: float) -> float:
    if capacity <= 0:
        return 1.0 if demand > 0 else 0.0
    return round(demand / capacity, 4)
