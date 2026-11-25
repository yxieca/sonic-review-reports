# Human-operated feedback drafts: sonic-platform-daemons #944

Report: https://github.com/yxieca/sonic-review-reports/pull/55
Reviewed head: `fe17f2eb76d6574ef6bcdb4bb3f1a5a20f1b4036`

## Questions without verdict

Could configuration removal revoke an existing port actor's control path without requiring a TRANSCEIVER_INFO event? At this revision, deleting CONFIG_DB MUX_CABLE for an initialized port leaves cached `self.cable`/driver state active; a queued or later toggle still reaches the vendor API. Python rechecks membership at dispatch. Could request/telemetry admission revalidate configuration, or receive ordered actor invalidation, with a regression deleting MUX_CABLE while leaving TRANSCEIVER_INFO unchanged? See R3 in the linked report. The existing TLS and runtime-replay concerns are already raised in the earlier review; please address those in their existing discussion rather than duplicating feedback.

Reviewed source: `fe17f2eb76d6574ef6bcdb4bb3f1a5a20f1b4036`. Source-only review; no tests/builds, native imports or hardware/service validation performed. Report: https://github.com/yxieca/sonic-review-reports/pull/55. R1/R2 already have existing target feedback; this draft does not request duplicate comments. Check current head and author replies before submitting with your own account.

## Request changes with comment

Please ensure configuration removal revokes an existing mux actor's hardware-control path before accepting this implementation. After MUX_CABLE is deleted without a transceiver event, cached classification still admits a later toggle and telemetry. Revalidate membership at actionable dispatch/telemetry or deliver ordered configuration invalidation; add a regression requiring no driver/RPC call after removal. This is R3 in the report. R1/R2 (TLS establishment/readiness and runtime command replay) are already raised in the existing review and should be resolved there; no duplicate repost is requested. The syslog backpressure note is nonblocking.

Reviewed source: `fe17f2eb76d6574ef6bcdb4bb3f1a5a20f1b4036`. Source-only review; no tests/builds, native imports or hardware/service validation performed. Report: https://github.com/yxieca/sonic-review-reports/pull/55. R1/R2 already have existing target feedback; this draft does not request duplicate comments. Check current head and author replies before submitting with your own account.
