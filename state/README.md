# State Layer

The executable shared state is implemented in `orchestration/state.py`. This directory documents the state-layer boundary for adapters and future persistence integrations. F40 keeps each run isolated and returns all decision-relevant state needed for audit and reproduction.
