def missing_redundancy(components: list[dict]) -> list[str]:
    return [c.get("name", "unknown") for c in components if c.get("critical") and int(c.get("replicas", 1)) < 2]
