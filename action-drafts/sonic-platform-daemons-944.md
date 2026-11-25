# Self-contained reader drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/55

Reviewed target head: `fe17f2eb76d6574ef6bcdb4bb3f1a5a20f1b4036`. Existing issue dispositions, coverage limits and target-feedback receipts remain unchanged. This presentation update submits no target feedback.



## Questions without verdict

Questions for correction or explanation; no formal verdict.

**R3 — configuration removal does not revoke cached actor control (P2).** `sonic-ycabled-rs/src/actor/mod.rs::handle_request` (368–388) dispatches from cached self.cable; refresh occurs on TRANSCEIVER_INFO SET (410–452), not MUX_CABLE deletion. Initialize an active-standby mux port, then delete CONFIG_DB MUX_CABLE without a transceiver/presence event: queued or later HW_MUX_CABLE_TABLE toggles still reach the vendor API through standby helpers, and periodic telemetry remains admitted. Python dispatch rechecks membership and skips the missing row. Revalidate mux membership at actionable request/telemetry dispatch or deliver ordered invalidation, and cover removal without TRANSCEIVER_INFO change with no-driver/RPC controls. This is the configuration-removal boundary, not a claim all reconfiguration is wrong. Existing TLS/readiness and runtime replay R1/R2 are already raised in the earlier review; resolve them there without duplicate feedback.

Source: https://github.com/sonic-net/sonic-platform-daemons/blob/fe17f2eb76d6574ef6bcdb4bb3f1a5a20f1b4036/sonic-ycabled-rs/src/actor/mod.rs#L368-L388

Reviewed target head: `fe17f2eb76d6574ef6bcdb4bb3f1a5a20f1b4036`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/55.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Request changes with comment

Request-changes reader draft for the retained findings below.

**R3 — configuration removal does not revoke cached actor control (P2).** `sonic-ycabled-rs/src/actor/mod.rs::handle_request` (368–388) dispatches from cached self.cable; refresh occurs on TRANSCEIVER_INFO SET (410–452), not MUX_CABLE deletion. Initialize an active-standby mux port, then delete CONFIG_DB MUX_CABLE without a transceiver/presence event: queued or later HW_MUX_CABLE_TABLE toggles still reach the vendor API through standby helpers, and periodic telemetry remains admitted. Python dispatch rechecks membership and skips the missing row. Revalidate mux membership at actionable request/telemetry dispatch or deliver ordered invalidation, and cover removal without TRANSCEIVER_INFO change with no-driver/RPC controls. This is the configuration-removal boundary, not a claim all reconfiguration is wrong. Existing TLS/readiness and runtime replay R1/R2 are already raised in the earlier review; resolve them there without duplicate feedback.

Source: https://github.com/sonic-net/sonic-platform-daemons/blob/fe17f2eb76d6574ef6bcdb4bb3f1a5a20f1b4036/sonic-ycabled-rs/src/actor/mod.rs#L368-L388

Reviewed target head: `fe17f2eb76d6574ef6bcdb4bb3f1a5a20f1b4036`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/55.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Prior draft history

The prior wording is preserved in the preceding report commit. This update expands author-facing explanations only; it does not change findings, severity, source coverage, target verdict or submission state.
