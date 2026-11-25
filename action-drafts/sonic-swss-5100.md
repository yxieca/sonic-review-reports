# Self-contained reader drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/56

Reviewed target head: `ebb7de7807ecf97dc17c79f2aeeea3512087da9a`. Existing issue dispositions, coverage limits and target-feedback receipts remain unchanged. This presentation update submits no target feedback.



## Questions without verdict

Questions for correction or explanation; no formal verdict.

**R1 — hardware retirement must terminate removed-TC history (P2).** In `orchagent/pfcwdhworch.cpp` reconfiguration/current-mask guard (468–490,1170–1210), a valid PORT_QOS_MAP SET changes pfcwd_sw_enable3,4→4 while TC3 is stormed; a subsequent valid PFC_WD SET skips TC3 in the guard. Successful old-mapping teardown (909–995) closes counters and erases its saved alias/TC mapping without interrupting history; initialization (1116–1150) visits TC4 only. The retired TC3 row retains storm_N_detected without restored/interrupted or the actual terminal timestamp. Later TC3 registration interrupts it late, so no inevitable future-storm merge or forwarding outage is claimed. After each successful tracked-queue disable, interrupt history using saved alias/TC before erasing the mapping, covering both teardown loops. Preserve open tracking on disable failure; retain warm-start interruption and add removed-TC SET, unchanged-mask, DELETE and RECOVERED-first controls. The earlier warm-history fix is credited, not reopened.

**N1/N2 — nonblocking:** document last-event/optional-prior/reset semantics in doc/swss-schema.md; make tests/mock_tests/pfcwd_history_ut.cpp's duration check deterministic instead of a real-clock roughly300ms scheduling allowance. No live/C++ execution was performed.

Source: https://github.com/sonic-net/sonic-swss/blob/ebb7de7807ecf97dc17c79f2aeeea3512087da9a/orchagent/pfcwdhworch.cpp#L909-L995

Reviewed target head: `ebb7de7807ecf97dc17c79f2aeeea3512087da9a`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/56.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Request changes with comment

Request-changes reader draft for the retained findings below.

**R1 — hardware retirement must terminate removed-TC history (P2).** In `orchagent/pfcwdhworch.cpp` reconfiguration/current-mask guard (468–490,1170–1210), a valid PORT_QOS_MAP SET changes pfcwd_sw_enable3,4→4 while TC3 is stormed; a subsequent valid PFC_WD SET skips TC3 in the guard. Successful old-mapping teardown (909–995) closes counters and erases its saved alias/TC mapping without interrupting history; initialization (1116–1150) visits TC4 only. The retired TC3 row retains storm_N_detected without restored/interrupted or the actual terminal timestamp. Later TC3 registration interrupts it late, so no inevitable future-storm merge or forwarding outage is claimed. After each successful tracked-queue disable, interrupt history using saved alias/TC before erasing the mapping, covering both teardown loops. Preserve open tracking on disable failure; retain warm-start interruption and add removed-TC SET, unchanged-mask, DELETE and RECOVERED-first controls. The earlier warm-history fix is credited, not reopened.

**N1/N2 — nonblocking:** document last-event/optional-prior/reset semantics in doc/swss-schema.md; make tests/mock_tests/pfcwd_history_ut.cpp's duration check deterministic instead of a real-clock roughly300ms scheduling allowance. No live/C++ execution was performed.

Source: https://github.com/sonic-net/sonic-swss/blob/ebb7de7807ecf97dc17c79f2aeeea3512087da9a/orchagent/pfcwdhworch.cpp#L909-L995

Reviewed target head: `ebb7de7807ecf97dc17c79f2aeeea3512087da9a`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/56.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Prior draft history

The prior wording is preserved in the preceding report commit. This update expands author-facing explanations only; it does not change findings, severity, source coverage, target verdict or submission state.
