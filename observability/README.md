# Observability Contract

Every agent appends one ordered trace record and one provenance-bearing evidence record. Escalations identify source, reason, and severity. Consumers should treat the returned `trace`, `evidence`, `open_risks`, and `escalations` fields as the minimum audit trail for each run. Production adapters may export the same contract to logs or tracing systems but must not silently drop approval or blocker events.
