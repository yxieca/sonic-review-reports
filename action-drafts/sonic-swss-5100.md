> **Feedback already submitted:** https://github.com/sonic-net/sonic-swss/pull/5100#issuecomment-7175239897. The original revision-bound drafts below are retained as history; do not repost identical feedback.

# Reader drafts: sonic-swss #5100

Report: https://github.com/yxieca/sonic-review-reports/pull/56
Reviewed HEAD: `ebb7de7807ecf97dc17c79f2aeeea3512087da9a`. No automatic target feedback.

## Questions without verdict

Could R1 be addressed in the hardware removed-TC teardown path? With TCs3+4 monitored and TC3 stormed, an accepted PORT_QOS_MAP SET changes pfcwd_sw_enable to4; a subsequent PFC_WD SET then skips TC3 in the current-mask storm guard. Successful old-mapping cleanup closes counters and erases queue identity without interrupting history, and reinitialization visits TC4 only. Could each successfully disabled tracked queue be marked interrupted before its saved alias/TC mapping is erased, including removed TCs, with a regression and disable-failure/unchanged-mask/DELETE controls? Later TC3 registration interrupts the old record, but too late to recover the actual teardown timestamp. This is new-history correctness, not a demonstrated forwarding outage. Nonblocking N1: document last-event state/optional prior fields/reset lifetimes. Nonblocking N2: make the duration unit test deterministic rather than requiring a roughly300ms scheduling allowance.

Reviewed HEAD: ebb7de7807ecf97dc17c79f2aeeea3512087da9a. Full independent three-general-plus-separate-SME source review and coordinator grounding; no tests, compiler, native/live Redis/SAI/DUT or hardware validation executed. Report: https://github.com/yxieca/sonic-review-reports/pull/56. Verify current revision and discussion before submission. The earlier initialized-TC warm-history correction is credited; this concerns a different teardown boundary.

## Request changes with comment

Please correct R1 before accepting the new history feature: interrupt each successfully disabled tracked hardware queue before erasing its saved alias/TC mapping, including TCs absent from the current watchdog mask. A valid mask SET3,4→4 followed by watchdog SET can otherwise retire stormed TC3 while leaving its history without restored/interrupted; initialization visits only TC4. Later TC3 registration closes the row late, not at the actual retirement boundary. Preserve open tracking when disable fails and add removed-TC reconfiguration plus unchanged-mask/DELETE/failure controls. This is a P2 diagnostic-history defect, not an observed forwarding failure. Nonblocking N1: document schema and last-event/reset semantics. Nonblocking N2: remove the duration unit test real-clock scheduling deadline.

Reviewed HEAD: ebb7de7807ecf97dc17c79f2aeeea3512087da9a. Full independent three-general-plus-separate-SME source review and coordinator grounding; no tests, compiler, native/live Redis/SAI/DUT or hardware validation executed. Report: https://github.com/yxieca/sonic-review-reports/pull/56. Verify current revision and discussion before submission. The earlier initialized-TC warm-history correction is credited; this concerns a different teardown boundary.
