# Self-contained reader drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/44

Reviewed target head: `aaeafc9879ea14deb0ca747180c02382f736bc02`. Existing issue dispositions, coverage limits and target-feedback receipts remain unchanged. This presentation update submits no target feedback.



## Questions without verdict

Questions for correction or explanation; no formal verdict.

**B1 — restore BGP state in the namespaces installation changes (P2).** `tests/platform_tests/ssd/conftest.py:103–106,123–128` snapshots host-global running config and restores unqualified CONFIG_DB, while all-peer shutdown/startup iterates frontend ASIC namespaces. An asic0 peer originally down or lacking admin_status can become explicitly up without a saved namespace record to restore. Capture presence/value per namespace and neighbor for the actual mutation domain, or constrain support explicitly. Later module config recovery does not prevent unintended activation during the module; no permanent outage is claimed.

**B2 — restore disabled peers before validating old route totals (P2).** `conftest.py:121–128` starts all peers and waits for original route totals before re-disabling initially-down peers. A reachable formerly-disabled peer advertising at least five distinct additional routes can make successful installation fail readiness. Restore exact original state first, then verify convergence; final cleanup exists, so this is ordering/false setup failure rather than no cleanup.

**B3 — reject loss of previously available post-stress health data (P2).** `test_ssd_health.py:216–232` ignores missing after-load SMART/warning/temperature and detects disappearance only for media counters. A valid SATA baseline lacking vendor media counters can pass even when its after snapshot becomes entirely unreadable. Preserve baseline critical-field availability and fail disappearance, at least total unreadability, while tolerating fields unsupported from the start. Separate collection/parse failure from unsupported telemetry.

Source: https://github.com/sonic-net/sonic-mgmt/blob/aaeafc9879ea14deb0ca747180c02382f736bc02/tests/platform_tests/ssd/conftest.py#L103-L128

Reviewed target head: `aaeafc9879ea14deb0ca747180c02382f736bc02`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/44.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Request changes with comment

Request-changes reader draft for the retained findings below.

**B1 — restore BGP state in the namespaces installation changes (P2).** `tests/platform_tests/ssd/conftest.py:103–106,123–128` snapshots host-global running config and restores unqualified CONFIG_DB, while all-peer shutdown/startup iterates frontend ASIC namespaces. An asic0 peer originally down or lacking admin_status can become explicitly up without a saved namespace record to restore. Capture presence/value per namespace and neighbor for the actual mutation domain, or constrain support explicitly. Later module config recovery does not prevent unintended activation during the module; no permanent outage is claimed.

**B2 — restore disabled peers before validating old route totals (P2).** `conftest.py:121–128` starts all peers and waits for original route totals before re-disabling initially-down peers. A reachable formerly-disabled peer advertising at least five distinct additional routes can make successful installation fail readiness. Restore exact original state first, then verify convergence; final cleanup exists, so this is ordering/false setup failure rather than no cleanup.

**B3 — reject loss of previously available post-stress health data (P2).** `test_ssd_health.py:216–232` ignores missing after-load SMART/warning/temperature and detects disappearance only for media counters. A valid SATA baseline lacking vendor media counters can pass even when its after snapshot becomes entirely unreadable. Preserve baseline critical-field availability and fail disappearance, at least total unreadability, while tolerating fields unsupported from the start. Separate collection/parse failure from unsupported telemetry.

Source: https://github.com/sonic-net/sonic-mgmt/blob/aaeafc9879ea14deb0ca747180c02382f736bc02/tests/platform_tests/ssd/conftest.py#L103-L128

Reviewed target head: `aaeafc9879ea14deb0ca747180c02382f736bc02`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/44.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Prior draft history

The prior wording is preserved in the preceding report commit. This update expands author-facing explanations only; it does not change findings, severity, source coverage, target verdict or submission state.
