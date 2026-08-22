# Memory Policy

F40 does not persist user or organization data across runs. Each run is stateless outside its returned result. If an adapter adds persistence, it must define retention, staleness, access control, deletion, and provenance before being considered compatible with the L3 reference behavior.
