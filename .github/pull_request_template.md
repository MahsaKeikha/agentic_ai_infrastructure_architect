## Summary

Describe the infrastructure behavior or documentation change.

## Validation

- [ ] `ruff check .`
- [ ] `pytest -q`
- [ ] `python evals/run_scenarios.py`
- [ ] `python evals/run_heldout.py`
- [ ] `python examples/minimal.py`
- [ ] `python examples/complete.py`
- [ ] `python run.py`

## Safety and governance

- [ ] Human approval behavior is unchanged or explicitly tested.
- [ ] Failed architecture, capacity, reliability, cost, security, rollback, conflict, and unresolved-question gates still fail closed.
- [ ] New assumptions, evidence, conflicts, and risks are represented explicitly.

## Documentation

- [ ] README/docs match actual behavior.
- [ ] CHANGELOG updated for user-visible changes.
