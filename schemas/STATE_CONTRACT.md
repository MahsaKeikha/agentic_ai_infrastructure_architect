# State Contract

The public result contract contains `system_id`, `system_name`, `version`, `analyses`, `status`, `approval`, `assumptions`, `conflicts`, `unresolved_questions`, `open_risks`, `escalations`, `evidence`, and `trace`.

`status` is one of `approved`, `awaiting_human_approval`, or `review_required`. Evidence records identify their source and provenance. Conflicts and unresolved questions are never silently discarded and prevent approval until resolved.
