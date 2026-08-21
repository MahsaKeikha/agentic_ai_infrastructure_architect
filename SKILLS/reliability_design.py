def reliability_review(points: list[str]) -> dict:
    return {"pass": not points, "single_points_of_failure": points}
