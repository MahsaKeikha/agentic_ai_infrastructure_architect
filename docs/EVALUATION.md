# Evaluation

F40 is evaluated at three levels.

1. Unit and behavioral tests verify agent contracts, fail-closed behavior, evidence generation, escalations, and approval gating.
2. Deterministic offline architecture scenarios verify healthy infrastructure, capacity shortfall, and missing security review.
3. CI executes lint, tests, scenarios, and a smoke run on Python 3.10, 3.11, and 3.12.

Current scenarios are intentionally small and reproducible. They are not evidence that the architecture covers every cloud, workload, compliance regime, or failure mode. L3 promotion should require larger held-out scenario suites, published result artifacts, and independent reproduction.
