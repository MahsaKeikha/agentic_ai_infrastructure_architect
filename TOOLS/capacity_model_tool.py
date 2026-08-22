from __future__ import annotations


def model_capacity(demand: float, capacity: float) -> dict[str, float | bool]:
    demand = max(0.0, float(demand))
    capacity = max(0.0, float(capacity))
    headroom = capacity - demand
    utilization = (demand / capacity) if capacity > 0 else (1.0 if demand > 0 else 0.0)
    ratio = (capacity / demand) if demand > 0 else 1.0
    return {
        "demand": demand,
        "capacity": capacity,
        "headroom": round(headroom, 3),
        "utilization": round(utilization, 4),
        "capacity_ratio": round(ratio, 4),
        "sufficient": capacity >= demand,
    }
