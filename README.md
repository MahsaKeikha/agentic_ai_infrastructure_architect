# F40 Agentic AI Infrastructure Architect

**Maturity: L3 Gold Standard**  
**Version: 1.0.0**

A reference multi-agent architecture for AI infrastructure design, capacity planning, resilience, cost governance, and deployment-readiness decision support.

## Why multi-agent

Infrastructure decisions combine different failure modes. F40 separates architecture coverage, capacity, reliability, cost, and final readiness so each concern can challenge the others and leave auditable evidence instead of collapsing everything into one opaque score.

## Agent workflow

1. Platform Architecture Agent validates required capabilities and topology coverage.
2. Capacity Agent checks provisioned capacity against expected peak demand.
3. Reliability Agent checks redundancy, backups, and tested recovery.
4. Cost Governance Agent checks budget variance and cost constraints.
5. Deployment Readiness Agent synthesizes upstream evidence and applies security, rollback, conflict, unresolved-question, and human-approval gates.

The orchestrator records assumptions, conflicts, unresolved questions, provenance evidence, open risks, escalations, execution trace, and approval state. Human approval cannot override failed technical or governance gates.

## Quick start

```bash
python -m pip install -e '.[dev]'
pytest -q
python evals/run_scenarios.py
python evals/run_heldout.py
python examples/minimal.py
python examples/complete.py
python run.py
```

The core reference workflow runs offline. CI executes the same acceptance path on Python 3.10, 3.11, and 3.12 and publishes the held-out results artifact.

## L3 evidence

- substantive five-agent implementation;
- explicit agents -> skills -> tools separation;
- shared traceable state and provenance;
- fail-closed approval and escalation logic;
- unit, integration, red-team, failure, approval, and end-to-end tests;
- normal, failure, and held-out architecture scenarios;
- deterministic offline reproducibility;
- three-version green CI required for promotion;
- held-out evaluation artifact publication;
- complete architecture, safety, evaluation, extension, citation, contribution, and security documentation.

See `docs/L3_AUDIT.md` for the promotion record and `docs/EVALUATION.md` for benchmark interpretation.

## Limitations

F40 is a reference implementation, not an autonomous production deployment engine. Organization-specific infrastructure, threat models, regulatory requirements, cloud-provider semantics, pricing, and SRE policies require separate validation. L3 describes the quality of the reference implementation, not universal fitness for every production environment.

## Parent library

Agentic AI Library: https://github.com/MahsaKeikha/agentic_ai_library
