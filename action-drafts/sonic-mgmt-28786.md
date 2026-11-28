# Self-contained reader drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/49

Reviewed target head: `e1c21fc39dc94d71d5a30425ac8bd559081bfd9a`. Existing issue dispositions, coverage limits and target-feedback receipts remain unchanged. This presentation update submits no target feedback.



## Questions without verdict

Questions for correction or explanation; no formal verdict.

**R1 — restore interfaces after partial Scenario B failure (P2).** In `tests/platform_tests/api/test_sfp.py::test_reset` (999–1022,1035–1074), shutdown is followed by startup only on the normal path. A client HTTP/JSON reset failure, second CPO-member shutdown failure, or cleanup exception can leave changed interfaces down until later module recovery. Register restoration before mutation, preserve the original failure and attempt every changed member even if another cleanup fails. A vendor False/None result alone is not claimed to skip startup; module recovery limits the consequence to per-test isolation, not permanent stranding.

**R2 — quiesce every logical sibling of the physical reset unit (P2).** `get_intf_name` (862–869) returns the first interface, while the physical reverse mapping is one-to-many. On breakout, one sibling can remain up during the shared physical reset, so Scenario B can pass without its intended all-down precondition. Use the full logical-member set with explicit connection/skip scope and test multiple siblings. No hardware recovery failure is claimed.

**R3 — preserve originally admin-down members (P2).** Connected/non-skipped selection does not guarantee admin-up, but Scenario B always starts selected interfaces after reset. A successful test can enable an intentionally down interface and affect later tests before module recovery. Snapshot and restore original per-member state, or explicitly restrict eligible interfaces; cover initially-down success separately from exceptional cleanup.

Source: https://github.com/sonic-net/sonic-mgmt/blob/e1c21fc39dc94d71d5a30425ac8bd559081bfd9a/tests/platform_tests/api/test_sfp.py#L999-L1074

Reviewed target head: `e1c21fc39dc94d71d5a30425ac8bd559081bfd9a`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/49.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Request changes with comment

Request-changes reader draft for the retained findings below.

**R1 — restore interfaces after partial Scenario B failure (P2).** In `tests/platform_tests/api/test_sfp.py::test_reset` (999–1022,1035–1074), shutdown is followed by startup only on the normal path. A client HTTP/JSON reset failure, second CPO-member shutdown failure, or cleanup exception can leave changed interfaces down until later module recovery. Register restoration before mutation, preserve the original failure and attempt every changed member even if another cleanup fails. A vendor False/None result alone is not claimed to skip startup; module recovery limits the consequence to per-test isolation, not permanent stranding.

**R2 — quiesce every logical sibling of the physical reset unit (P2).** `get_intf_name` (862–869) returns the first interface, while the physical reverse mapping is one-to-many. On breakout, one sibling can remain up during the shared physical reset, so Scenario B can pass without its intended all-down precondition. Use the full logical-member set with explicit connection/skip scope and test multiple siblings. No hardware recovery failure is claimed.

**R3 — preserve originally admin-down members (P2).** Connected/non-skipped selection does not guarantee admin-up, but Scenario B always starts selected interfaces after reset. A successful test can enable an intentionally down interface and affect later tests before module recovery. Snapshot and restore original per-member state, or explicitly restrict eligible interfaces; cover initially-down success separately from exceptional cleanup.

Source: https://github.com/sonic-net/sonic-mgmt/blob/e1c21fc39dc94d71d5a30425ac8bd559081bfd9a/tests/platform_tests/api/test_sfp.py#L999-L1074

Reviewed target head: `e1c21fc39dc94d71d5a30425ac8bd559081bfd9a`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/49.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Prior draft history

The prior wording is preserved in the preceding report commit. This update expands author-facing explanations only; it does not change findings, severity, source coverage, target verdict or submission state.
