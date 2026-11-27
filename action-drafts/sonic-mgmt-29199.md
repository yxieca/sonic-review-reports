> Current Q1 external review cleared; own R1/R2 remain correction-required. No source approval or target submission.

# Self-contained reader drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/26

Reviewed target head: `8fd84017fc27f07c22e99346a2b794ba76dface2`. Existing issue dispositions, coverage limits and target-feedback receipts remain unchanged. This presentation update submits no target feedback.



## Questions without verdict

Questions for correction or explanation; no formal verdict.

**R1 — global audit silence can block owned-subscription cleanup (P2).** `tests/redfish/test_redfish_audit_log.py::AuditLog.mark` (119–131) waits without a deadline for counts to agree, and the subscription finalizer (464–467) calls it before DELETE. Ongoing audit activity can prevent assertions and deletion of the test-owned subscription. Bound cursor acquisition and attempt owned-resource cleanup even if marking fails; quiet-device convergence remains valid and no newly observed hang/outage is claimed.

**R2 — initial DEBUG can cause a false no-read failure (P2).** The log_level fixture (212–236) snapshots/restores but does not establish INFO; the test (361–392) asserts no read before changing level. A supported initial DEBUG configuration correctly records that GET and fails the negative assertion. Set/wait for INFO first, exercise DEBUG→INFO and restore original state. Previous readiness/publication/event-filter/analyzer corrections remain credited. Zero-subscriber isolation and conditional command lifecycle remain nonblocking; merged prerequisite and existing external review are separate gates.

Source: https://github.com/sonic-net/sonic-mgmt/blob/8fd84017fc27f07c22e99346a2b794ba76dface2/tests/redfish/test_redfish_audit_log.py#L119-L131

Reviewed target head: `8fd84017fc27f07c22e99346a2b794ba76dface2`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/26.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Comment without verdict

Comment without a formal verdict.

**R1 — global audit silence can block owned-subscription cleanup (P2).** `tests/redfish/test_redfish_audit_log.py::AuditLog.mark` (119–131) waits without a deadline for counts to agree, and the subscription finalizer (464–467) calls it before DELETE. Ongoing audit activity can prevent assertions and deletion of the test-owned subscription. Bound cursor acquisition and attempt owned-resource cleanup even if marking fails; quiet-device convergence remains valid and no newly observed hang/outage is claimed.

**R2 — initial DEBUG can cause a false no-read failure (P2).** The log_level fixture (212–236) snapshots/restores but does not establish INFO; the test (361–392) asserts no read before changing level. A supported initial DEBUG configuration correctly records that GET and fails the negative assertion. Set/wait for INFO first, exercise DEBUG→INFO and restore original state. Previous readiness/publication/event-filter/analyzer corrections remain credited. Zero-subscriber isolation and conditional command lifecycle remain nonblocking; merged prerequisite and existing external review are separate gates.

Source: https://github.com/sonic-net/sonic-mgmt/blob/8fd84017fc27f07c22e99346a2b794ba76dface2/tests/redfish/test_redfish_audit_log.py#L119-L131

Reviewed target head: `8fd84017fc27f07c22e99346a2b794ba76dface2`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/26.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Request changes with comment

Request-changes reader draft for the retained findings below.

**R1 — global audit silence can block owned-subscription cleanup (P2).** `tests/redfish/test_redfish_audit_log.py::AuditLog.mark` (119–131) waits without a deadline for counts to agree, and the subscription finalizer (464–467) calls it before DELETE. Ongoing audit activity can prevent assertions and deletion of the test-owned subscription. Bound cursor acquisition and attempt owned-resource cleanup even if marking fails; quiet-device convergence remains valid and no newly observed hang/outage is claimed.

**R2 — initial DEBUG can cause a false no-read failure (P2).** The log_level fixture (212–236) snapshots/restores but does not establish INFO; the test (361–392) asserts no read before changing level. A supported initial DEBUG configuration correctly records that GET and fails the negative assertion. Set/wait for INFO first, exercise DEBUG→INFO and restore original state. Previous readiness/publication/event-filter/analyzer corrections remain credited. Zero-subscriber isolation and conditional command lifecycle remain nonblocking; merged prerequisite and existing external review are separate gates.

Source: https://github.com/sonic-net/sonic-mgmt/blob/8fd84017fc27f07c22e99346a2b794ba76dface2/tests/redfish/test_redfish_audit_log.py#L119-L131

Reviewed target head: `8fd84017fc27f07c22e99346a2b794ba76dface2`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/26.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Prior draft history

The prior wording is preserved in the preceding report commit. This update expands author-facing explanations only; it does not change findings, severity, source coverage, target verdict or submission state.


**Q1 external-review gate cleared:** [current-head approval6084615107](https://github.com/sonic-net/sonic-mgmt/pull/29199#pullrequestreview-6084615107) explicitly clears the earlier merge-order/external-review objection. Redfish41 is merged; Redfish50 remains a nonblocking follow-up whose final API/record shape should remain aligned with the audit tests. The dated Changes Requested6034554222 record is preserved as historical, not current controlling Q1 state.

**Our distinct R1/R2 remain unchanged and correction-required.** This receipt is not our source approval, a CI-ready claim, target feedback or merge. No independent source panel was rerun solely to reconcile another reviewer's status. Reviewed HEAD `8fd84017fc27f07c22e99346a2b794ba76dface2`; report https://github.com/yxieca/sonic-review-reports/pull/26.