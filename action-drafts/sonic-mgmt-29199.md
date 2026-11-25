# Human-operated current-head feedback drafts

Reviewed revision 9b0fc773bb0e084f6a761775e95b32e95b1d3c83. Report: https://github.com/yxieca/sonic-review-reports/pull/26. Three independent general source lenses, separate SME and coordinator grounding; closed inert Python controls only, no native/DUT/Redis/service/hardware validation. Earlier source fixes are credited; current dependency/review gates remain. Check current source/replies before submitting. Nothing is submitted automatically.

## Questions

Could the new audit tests address R1/R2? R1: AuditLog.mark() requires global audit silence with no deadline and runs before the owned subscription DELETE in finally. Could cursor acquisition be bounded and cleanup attempted even if it fails? R2: test_read_recorded_only_at_debug rejects read records before establishing a non-DEBUG baseline; an initially DEBUG-configured BMC correctly logs that GET. Could the fixture set INFO before the first negative assertion and restore the original level afterward? Separately, the advertised no-subscriber test accepts an existing nonzero count; could it require zero or clearly skip without deleting unrelated subscriptions? Prior readiness/command/event improvements are credited; existing feedback should not be duplicated.

Reviewed revision 9b0fc773bb0e084f6a761775e95b32e95b1d3c83. Report: https://github.com/yxieca/sonic-review-reports/pull/26. Three independent general source lenses, separate SME and coordinator grounding; closed inert Python controls only, no native/DUT/Redis/service/hardware validation. Earlier source fixes are credited; current dependency/review gates remain. Check current source/replies before submitting. Nothing is submitted automatically.

## Request changes

Please fix new audit-test R1/R2 before acceptance: bound AuditLog.mark() and ensure cursor failure cannot block deletion of the test-owned subscription; establish INFO before the first no-read assertion, then test DEBUG/INFO transitions while restoring the original configuration. These are new test lifecycle/false-failure cases, not CodeQL secret/finally allegations. The no-subscriber precondition is a nonblocking coverage improvement; preserve existing subscriptions. Previous daemon readiness, command publication, registry power filtering and Retry-After warnings are credited. Existing Redfish41-first and external review gates remain separate; no live device or503header execution is claimed.

Reviewed revision 9b0fc773bb0e084f6a761775e95b32e95b1d3c83. Report: https://github.com/yxieca/sonic-review-reports/pull/26. Three independent general source lenses, separate SME and coordinator grounding; closed inert Python controls only, no native/DUT/Redis/service/hardware validation. Earlier source fixes are credited; current dependency/review gates remain. Check current source/replies before submitting. Nothing is submitted automatically.
