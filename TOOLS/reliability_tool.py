def reliability_gap(target: float, observed: float) -> float:
    return round(max(target - observed, 0.0), 6)
