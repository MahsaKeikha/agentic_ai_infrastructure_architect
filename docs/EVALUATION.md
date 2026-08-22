# Evaluation and Benchmark Method

F40 evaluates decision-support behavior, not universal infrastructure quality.

## Required metrics

- expected-status accuracy across deterministic scenarios;
- approval-gate accuracy;
- blocker detection for topology, capacity, reliability, cost, security, rollback, conflicts, and unresolved questions;
- trace completeness;
- provenance/evidence presence;
- reproducibility across Python 3.10, 3.11, and 3.12.

## Suites

`evals/run_scenarios.py` contains the primary normal and failure suite. `evals/run_heldout.py` contains a separate eight-scenario acceptance suite spanning healthy architecture, capacity shortfall, budget overrun, untested recovery, missing security review, approval withholding, conflicting inputs, and unresolved disaster-recovery questions.

CI requires a 100% expected-decision pass rate for both suites. Python 3.12 additionally uploads `artifacts/heldout_results.json` as a workflow artifact so the evaluation result can be inspected independently of console output.

## Interpretation

A passing suite means the checked reference behaviors are reproducible. It does not establish universal safety, provider-specific correctness, optimal cost, or fitness for unattended deployment. New infrastructure domains should add held-out fixtures before making stronger claims.
