# Human-operated feedback drafts

Full source review at 9c2f70eeb39eb9320d9c08202e0ecb660df1ef84: three independent general lenses, separate SME and coordinator grounding. Native C++/BMC/Redis/D-Bus tests were not run. Report: https://github.com/yxieca/sonic-review-reports/pull/26. Existing inherited follow-ups remain tracked; check current head/replies and review gates before use. Actual PR targets master;202608 applicability is separate. Nothing is submitted automatically.

## Comment

Source review is favorable for the six-file Redfish test change against the explicit Redfish41 comparison. Previous assertion/finalizer issues are fixed. Nonblocking readiness/command-cleanup/retained-slot robustness suggestions remain, with normal next-param/module restarts limiting cross-test impact. The description now states Redfish41 must merge first and identifies required four-field MessageIds; Redfish41 remains open and the current Changes Requested review is not cleared. No installed-SUT or202608 branch validation is claimed. Existing feedback should not be duplicated.

Full source review at 9c2f70eeb39eb9320d9c08202e0ecb660df1ef84: three independent general lenses, separate SME and coordinator grounding. Native C++/BMC/Redis/D-Bus tests were not run. Report: https://github.com/yxieca/sonic-review-reports/pull/26. Existing inherited follow-ups remain tracked; check current head/replies and review gates before use. Actual PR targets master;202608 applicability is separate. Nothing is submitted automatically.

## Approve with comment

Source inspection supports the test coverage and current fixes, with the retained nonblocking robustness notes. This draft must not be submitted while the explicit Redfish41-first gate and current external Changes Requested review remain unresolved. Verify dependency state, installed image and current target revision before any later approval decision. Original202608 destination was not found; no release applicability/test receipt is implied. This text does not cast approval or clear another review.

Full source review at 9c2f70eeb39eb9320d9c08202e0ecb660df1ef84: three independent general lenses, separate SME and coordinator grounding. Native C++/BMC/Redis/D-Bus tests were not run. Report: https://github.com/yxieca/sonic-review-reports/pull/26. Existing inherited follow-ups remain tracked; check current head/replies and review gates before use. Actual PR targets master;202608 applicability is separate. Nothing is submitted automatically.


## 2026-11-25 — Reader freshness / conversation note

The author reports local readiness, command publication/cleanup, power-event filtering, conditional Retry-After diagnostics, helper consolidation and nonempty leak-collection checks, pending a run with Redfish41 before the next push. These address existing N1/N2/N3 suggestions; they are not verified source fixes because the target head remains unchanged. The author explicitly preserves the all-row liquid-cooling selection consistent with the inspected Redfish41 adapter. Existing N5 retained-slot mitigation still needs current-source reconciliation after publication; no automatic disposition change. The Redfish41-first dependency and external Changes Requested review remain separate gates. No new code finding, target feedback or test execution. [Discussion](https://github.com/sonic-net/sonic-mgmt/pull/29199#issuecomment-7154788259).
