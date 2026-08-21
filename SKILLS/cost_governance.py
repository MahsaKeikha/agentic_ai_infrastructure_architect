def cost_gate(over_budget: bool, exception_approved: bool = False) -> bool:
    return not over_budget or exception_approved
