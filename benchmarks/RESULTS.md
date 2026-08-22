# F40 Held-out Benchmark Results

**Version:** 1.0.0  
**Commit:** `bb8cd07331efedbbc5b349c968e9547714dc3b53`  
**GitHub Actions run:** `32539376371`  
**Artifact:** `f40-heldout-results`  
**Artifact digest:** `sha256:59e92d99389e4ef16f156e073225231c86040e2a188f11c9a109f63d7a3193a7`

## Result

- Scenario count: 8
- Passed: 8
- Pass rate: 1.0

## Scenarios

| Scenario | Expected | Actual | Result |
|---|---|---|---|
| healthy_multi_zone | approved | approved | PASS |
| capacity_shortfall | review_required | review_required | PASS |
| budget_overrun | review_required | review_required | PASS |
| untested_restore | review_required | review_required | PASS |
| missing_security_review | review_required | review_required | PASS |
| unapproved_but_ready | awaiting_human_approval | awaiting_human_approval | PASS |
| conflicting_budget_input | review_required | review_required | PASS |
| unresolved_dr_question | review_required | review_required | PASS |

These results validate the documented reference behaviors for this deterministic held-out suite. They do not imply universal correctness for every cloud, infrastructure topology, threat model, or production environment.
