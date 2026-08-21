# Contributing

Contributions should preserve the Gold Standard goals: distinct agent responsibilities, structured state, evidence provenance, fail-closed safety behavior, reproducible scenarios, tests, and documentation.

Before opening a PR, run:

```bash
ruff check .
pytest -q
python evals/run_scenarios.py
python run.py
```

New infrastructure decisions should include behavioral tests for normal, failure, and escalation paths. Do not add autonomous production mutation without an explicit authorization boundary and human approval model.
