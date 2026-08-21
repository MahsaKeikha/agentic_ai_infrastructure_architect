# F40 Agentic AI Infrastructure Architect

Reference multi-agent architecture for infrastructure design, capacity planning, reliability, cost governance, and deployment readiness.

## Agent workflow

1. Platform Architecture Agent validates required capabilities and component coverage.
2. Capacity Agent checks provisioned capacity against expected peak demand.
3. Reliability Agent checks redundancy and recoverability controls.
4. Cost Governance Agent checks budget variance.
5. Deployment Readiness Agent synthesizes upstream evidence and applies security and rollback gates.

The orchestrator records evidence, traces, escalations, and human approval state. A human approval cannot override failed architecture, capacity, reliability, budget, security, or rollback gates.

## Run

```bash
python -m pip install -e '.[dev]'
pytest -q
python evals/run_scenarios.py
python run.py
```

## Maturity

L2 candidate. L3 is not claimed until larger held-out architecture suites, published artifacts, and independent reproducibility are available.

See `docs/ARCHITECTURE.md`, `docs/SAFETY.md`, `docs/EVALUATION.md`, and `docs/EXTENDING.md`.
