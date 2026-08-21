def capacity_status(headroom: float) -> str:
    return "insufficient" if headroom < 0 else "sufficient"
