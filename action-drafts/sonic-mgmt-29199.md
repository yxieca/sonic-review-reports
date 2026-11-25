# Human-operated current-head feedback drafts

Reviewed revision 9b0fc773bb0e084f6a761775e95b32e95b1d3c83. Report: https://github.com/yxieca/sonic-review-reports/pull/26. Three independent general source lenses, separate SME and coordinator grounding; closed inert Python controls only, no native/DUT/Redis/service/hardware validation. Earlier source fixes are credited; current dependency/review gates remain. Check current source/replies before submitting. Nothing is submitted automatically.

## Questions

Could the new audit tests address R1/R2? R1: AuditLog.mark() requires global audit silence with no deadline and runs before the owned subscription DELETE in finally. Could cursor acquisition be bounded and cleanup attempted even if it fails? R2: test_read_recorded_only_at_debug rejects read records before establishing a non-DEBUG baseline; an initially DEBUG-configured BMC correctly logs that GET. Could the fixture set INFO before the first negative assertion and restore the original level afterward? Separately, the advertised no-subscriber test accepts an existing nonzero count; could it require zero or clearly skip without deleting unrelated subscriptions? Prior readiness/command/event improvements are credited; existing feedback should not be duplicated.

Reviewed revision 9b0fc773bb0e084f6a761775e95b32e95b1d3c83. Report: https://github.com/yxieca/sonic-review-reports/pull/26. Three independent general source lenses, separate SME and coordinator grounding; closed inert Python controls only, no native/DUT/Redis/service/hardware validation. Earlier source fixes are credited; current dependency/review gates remain. Check current source/replies before submitting. Nothing is submitted automatically.

## Request changes

Please fix new audit-test R1/R2 before acceptance: bound AuditLog.mark() and ensure cursor failure cannot block deletion of the test-owned subscription; establish INFO before the first no-read assertion, then test DEBUG/INFO transitions while restoring the original configuration. These are new test lifecycle/false-failure cases, not CodeQL secret/finally allegations. The no-subscriber precondition is a nonblocking coverage improvement; preserve existing subscriptions. Previous daemon readiness, command publication, registry power filtering and Retry-After warnings are credited. Existing Redfish41-first and external review gates remain separate; no live device or503header execution is claimed.

Reviewed revision 9b0fc773bb0e084f6a761775e95b32e95b1d3c83. Report: https://github.com/yxieca/sonic-review-reports/pull/26. Three independent general source lenses, separate SME and coordinator grounding; closed inert Python controls only, no native/DUT/Redis/service/hardware validation. Earlier source fixes are credited; current dependency/review gates remain. Check current source/replies before submitting. Nothing is submitted automatically.


## Comment

The current-head source review identifies two new audit-test correctness issues. R1: AuditLog.mark() waits for global audit silence without a deadline, and the owned-subscription finalizer calls it before DELETE; bound cursor acquisition and guarantee owned-subscription cleanup even when marking fails. R2: test_read_recorded_only_at_debug asserts no read record before establishing INFO, so a supported initial DEBUG configuration correctly logs the GET and fails the test; establish INFO before that assertion and restore the original level afterward. Nonblocking N6: require a zero-subscriber precondition or clearly skip without deleting unrelated subscriptions. Earlier daemon readiness, ordinary command publication/completion, registry power filtering and explicit Retry-After warnings are credited. These are source-grounded test concerns, not confirmed CodeQL secret/finally defects or live device failures.

Reviewed revision `9b0fc773bb0e084f6a761775e95b32e95b1d3c83`. Full report: https://github.com/yxieca/sonic-review-reports/pull/26. Three independent general source lenses, separate SME and coordinator grounding; only closed inert Python controls executed, no native/DUT/Redis/service/hardware validation. No formal verdict is submitted with this comment; existing review/release gates remain separate.

— AI-assisted review, reviewed and approved by the human reviewer.
