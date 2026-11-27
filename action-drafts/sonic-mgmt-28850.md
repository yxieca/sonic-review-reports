# Revision-pinned reader drafts: sonic-mgmt #28850

Reviewed head: `463c9f28b087b61892182b59616c999a620300f2`

Existing target discussions cover retained concerns; do not duplicate feedback. These editable texts are self-contained, not submitted reviews. Runtime evidence limits are included inline.

## Comment as questions

https://github.com/sonic-net/sonic-mgmt/pull/28850#issuecomment-new

> Following the existing discussions, could you correct or explain these remaining source conditions? This comment casts no review verdict.
>
> Reviewed target head `463c9f28b087b61892182b59616c999a620300f2`. The current update is a bounded independent general-plus-separate-SME source cross-check with unchanged-scope original panel coverage carried forward, not a newly executed full panel or hardware qualification. No tests were executed for this follow-up. Existing discussions are referenced rather than repeated as newly discovered findings.
>
> **Failed cleanup reported as successful teardown (R1, P2):** In [test_liquid_cooling_leakage.py::leak_test_injection](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/platform_tests/api/test_liquid_cooling_leakage.py#L91-L105) and [test_thermal_leak_sensor.py::leak_test_injection](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/platform_tests/api/test_thermal_leak_sensor.py#L147-L160), failed `clear_test_leaks()` only logs a warning. If an injection remains, teardown can finish normally and following tests can consume the leftover state; the real-leak gate does not reject test-origin leaks. Please verify removal, reuse per-sensor withdrawal if useful, and fail teardown when cleanup remains unconfirmed. The [author's logging explanation](https://github.com/sonic-net/sonic-mgmt/pull/28850#discussion_r4636417239) is acknowledged; this references the existing cleanup discussion rather than a new duplicate finding.
>
> **Probe/reinjection episode boundary (R2, conditional P2):** [LeakTestApiInjector.supports_sensor_state](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/common/helpers/bmc_liquid_leakage_control_test_helper.py#L201-L216) waits for a non-leaking row only after the [brief capability injections](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/common/helpers/platform_api/leak_sensor_test.py#L77-L121). The old No row can satisfy that wait before probe publication. If publication precedes the [event marker](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/platform_tests/daemon/test_thermalctld.py#L326-L352) and reinjection precedes a clear poll, the daemon can retain the same episode and omit the fresh onset expected by the test. Please establish observed-injection → withdrawal → confirmed recovery ordering, or explain a supported equivalent boundary/containment. The [next-poll explanation](https://github.com/sonic-net/sonic-mgmt/pull/28850#discussion_r4636417611) is credited; deferral is not established solely by a narrow-window assertion.
>
> **Vendor escalation missing host recovery (R3, P2):** In [test_thermalctld_leak_severity_aggregation](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/platform_tests/daemon/test_thermalctld.py#L531-L571), the timeout case begins with expected MINOR and later reaches MAJOR, but the recovery guard still checks the initial expected severity. With a vendor physical-reading mocker and MAJOR `power_off`/`graceful_shutdown`, this skips host recovery; normal vendor deinit only restores sensors. Please include escalation/reached MAJOR in vendor recovery while keeping non-mitigating API-test injections excluded. This is conditional source evidence, not an observed hardware outage, and references the [existing escalation thread](https://github.com/sonic-net/sonic-mgmt/pull/28850#discussion_r4644242759).
>
> **Nonblocking:** [Case19](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/docs/testplan/bmc/sonic-bmc/BMC-platform-API-daemon-test-plan.md#L638-L650) should describe the real-leak skip rather than a HOST_STATE assertion that the test no longer performs. [Fixed-severity compatibility](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/platform_tests/api/test_thermal_leak_sensor.py#L162-L205) remains a question: if supported platforms can reject a parameter on every sensor, should that unavailable parameter skip rather than fail `tested>0`? No supported fixed-only platform is established here; neither note is an additional blocker.
>
> Evidence and retained history: https://github.com/yxieca/sonic-review-reports/pull/1.

## Request changes

https://github.com/sonic-net/sonic-mgmt/pull/28850/files

> Changes are recommended for the cleanup and conditional vendor restoration issues below. The episode concern needs a reliable boundary or supported accepted containment; optional notes are separate.
>
> Reviewed target head `463c9f28b087b61892182b59616c999a620300f2`. The current update is a bounded independent general-plus-separate-SME source cross-check with unchanged-scope original panel coverage carried forward, not a newly executed full panel or hardware qualification. No tests were executed for this follow-up. Existing discussions are referenced rather than repeated as newly discovered findings.
>
> **Failed cleanup reported as successful teardown (R1, P2):** In [test_liquid_cooling_leakage.py::leak_test_injection](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/platform_tests/api/test_liquid_cooling_leakage.py#L91-L105) and [test_thermal_leak_sensor.py::leak_test_injection](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/platform_tests/api/test_thermal_leak_sensor.py#L147-L160), failed `clear_test_leaks()` only logs a warning. If an injection remains, teardown can finish normally and following tests can consume the leftover state; the real-leak gate does not reject test-origin leaks. Please verify removal, reuse per-sensor withdrawal if useful, and fail teardown when cleanup remains unconfirmed. The [author's logging explanation](https://github.com/sonic-net/sonic-mgmt/pull/28850#discussion_r4636417239) is acknowledged; this references the existing cleanup discussion rather than a new duplicate finding.
>
> **Probe/reinjection episode boundary (R2, conditional P2):** [LeakTestApiInjector.supports_sensor_state](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/common/helpers/bmc_liquid_leakage_control_test_helper.py#L201-L216) waits for a non-leaking row only after the [brief capability injections](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/common/helpers/platform_api/leak_sensor_test.py#L77-L121). The old No row can satisfy that wait before probe publication. If publication precedes the [event marker](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/platform_tests/daemon/test_thermalctld.py#L326-L352) and reinjection precedes a clear poll, the daemon can retain the same episode and omit the fresh onset expected by the test. Please establish observed-injection → withdrawal → confirmed recovery ordering, or explain a supported equivalent boundary/containment. The [next-poll explanation](https://github.com/sonic-net/sonic-mgmt/pull/28850#discussion_r4636417611) is credited; deferral is not established solely by a narrow-window assertion.
>
> **Vendor escalation missing host recovery (R3, P2):** In [test_thermalctld_leak_severity_aggregation](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/platform_tests/daemon/test_thermalctld.py#L531-L571), the timeout case begins with expected MINOR and later reaches MAJOR, but the recovery guard still checks the initial expected severity. With a vendor physical-reading mocker and MAJOR `power_off`/`graceful_shutdown`, this skips host recovery; normal vendor deinit only restores sensors. Please include escalation/reached MAJOR in vendor recovery while keeping non-mitigating API-test injections excluded. This is conditional source evidence, not an observed hardware outage, and references the [existing escalation thread](https://github.com/sonic-net/sonic-mgmt/pull/28850#discussion_r4644242759).
>
> **Nonblocking:** [Case19](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/docs/testplan/bmc/sonic-bmc/BMC-platform-API-daemon-test-plan.md#L638-L650) should describe the real-leak skip rather than a HOST_STATE assertion that the test no longer performs. [Fixed-severity compatibility](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/platform_tests/api/test_thermal_leak_sensor.py#L162-L205) remains a question: if supported platforms can reject a parameter on every sensor, should that unavailable parameter skip rather than fail `tested>0`? No supported fixed-only platform is established here; neither note is an additional blocker.
>
> Evidence and retained history: https://github.com/yxieca/sonic-review-reports/pull/1.

## Plain comment without verdict

https://github.com/sonic-net/sonic-mgmt/pull/28850#issuecomment-new

> Current source follow-up: the conditions below remain unchanged. This comment provides consolidated evidence without an approval or Changes Requested verdict.
>
> Reviewed target head `463c9f28b087b61892182b59616c999a620300f2`. The current update is a bounded independent general-plus-separate-SME source cross-check with unchanged-scope original panel coverage carried forward, not a newly executed full panel or hardware qualification. No tests were executed for this follow-up. Existing discussions are referenced rather than repeated as newly discovered findings.
>
> **Failed cleanup reported as successful teardown (R1, P2):** In [test_liquid_cooling_leakage.py::leak_test_injection](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/platform_tests/api/test_liquid_cooling_leakage.py#L91-L105) and [test_thermal_leak_sensor.py::leak_test_injection](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/platform_tests/api/test_thermal_leak_sensor.py#L147-L160), failed `clear_test_leaks()` only logs a warning. If an injection remains, teardown can finish normally and following tests can consume the leftover state; the real-leak gate does not reject test-origin leaks. Please verify removal, reuse per-sensor withdrawal if useful, and fail teardown when cleanup remains unconfirmed. The [author's logging explanation](https://github.com/sonic-net/sonic-mgmt/pull/28850#discussion_r4636417239) is acknowledged; this references the existing cleanup discussion rather than a new duplicate finding.
>
> **Probe/reinjection episode boundary (R2, conditional P2):** [LeakTestApiInjector.supports_sensor_state](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/common/helpers/bmc_liquid_leakage_control_test_helper.py#L201-L216) waits for a non-leaking row only after the [brief capability injections](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/common/helpers/platform_api/leak_sensor_test.py#L77-L121). The old No row can satisfy that wait before probe publication. If publication precedes the [event marker](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/platform_tests/daemon/test_thermalctld.py#L326-L352) and reinjection precedes a clear poll, the daemon can retain the same episode and omit the fresh onset expected by the test. Please establish observed-injection → withdrawal → confirmed recovery ordering, or explain a supported equivalent boundary/containment. The [next-poll explanation](https://github.com/sonic-net/sonic-mgmt/pull/28850#discussion_r4636417611) is credited; deferral is not established solely by a narrow-window assertion.
>
> **Vendor escalation missing host recovery (R3, P2):** In [test_thermalctld_leak_severity_aggregation](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/platform_tests/daemon/test_thermalctld.py#L531-L571), the timeout case begins with expected MINOR and later reaches MAJOR, but the recovery guard still checks the initial expected severity. With a vendor physical-reading mocker and MAJOR `power_off`/`graceful_shutdown`, this skips host recovery; normal vendor deinit only restores sensors. Please include escalation/reached MAJOR in vendor recovery while keeping non-mitigating API-test injections excluded. This is conditional source evidence, not an observed hardware outage, and references the [existing escalation thread](https://github.com/sonic-net/sonic-mgmt/pull/28850#discussion_r4644242759).
>
> **Nonblocking:** [Case19](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/docs/testplan/bmc/sonic-bmc/BMC-platform-API-daemon-test-plan.md#L638-L650) should describe the real-leak skip rather than a HOST_STATE assertion that the test no longer performs. [Fixed-severity compatibility](https://github.com/sonic-net/sonic-mgmt/blob/463c9f28b087b61892182b59616c999a620300f2/tests/platform_tests/api/test_thermal_leak_sensor.py#L162-L205) remains a question: if supported platforms can reject a parameter on every sensor, should that unavailable parameter skip rather than fail `tested>0`? No supported fixed-only platform is established here; neither note is an additional blocker.
>
> Evidence and retained history: https://github.com/yxieca/sonic-review-reports/pull/1.

---

## Preserved prior draft texts — historical, superseded for submission

# Current human-operated drafts: sonic-mgmt #28850

Target head: `551639a26205168f539a1deb66262442cc7aa426`
Report: https://github.com/yxieca/sonic-review-reports/pull/1

Prepared after bounded coordinator-only source assessment on 2026-11-24. R1/R3 retained P2; R2 conditional P2, no accepted deferral. No fresh full panel or test execution. Earlier decision remains held; renewed revision-bound confirmation is needed for assistant submission. Do not claim the new material was already human-reviewed. No approval draft.

## Current Request changes

https://github.com/sonic-net/sonic-mgmt/pull/28850/files

> Regarding target head 551639a26205168f539a1deb66262442cc7aa426:
>
> I reviewed the findings in https://github.com/yxieca/sonic-review-reports/pull/1 against the target change. Before landing, please resolve or explain R1 (unconfirmed test-leak cleanup finishing normally) and R3 (vendor MINOR-to-MAJOR escalation missing power recovery). R2's probe-episode synchronization needs either a reliable boundary or an explicit, supported deferral/containment decision.
>
> These points are already discussed in the linked target threads; I am referencing those discussions rather than raising them as newly discovered issues. Please use the report IDs when explaining a correction or disagreement. The report includes the exact reviewed revision, scope and evidence limits.
>
> AI-assisted review report: https://github.com/yxieca/sonic-review-reports/pull/1. This submission reflects my own review and decision.
>
> Revision-bound evidence: target head 551639a26205168f539a1deb66262442cc7aa426. The 2026-11-24 follow-up is bounded coordinator-only source review, not a fresh full panel; earlier inert results are reused, not new hardware or test-suite validation. Existing R1/R2/R3 discussions are referenced; no new target feedback has been submitted.

## Current Comment as questions

https://github.com/sonic-net/sonic-mgmt/pull/28850#issuecomment-new

> Regarding target head 551639a26205168f539a1deb66262442cc7aa426:
>
> Following the existing discussions, could you clarify the remaining points in https://github.com/yxieca/sonic-review-reports/pull/1?
>
> - R1: what establishes unsuccessful teardown or verified cleanup if bulk withdrawal returns false? The warning-only decision is acknowledged.
> - R2: what ensures reinjection starts a new daemon episode if the recovery predicate observes the old No row before publication? Could this be safely deferred with an explicit containment?
> - R3: should the vendor recovery guard include the MINOR-to-MAJOR escalation case when MAJOR can remove power?
>
> I am asking for correction or explanation, not asserting a physical outage. The report distinguishes new-path gaps, the direct recovery regression, and source/inert versus hardware evidence.
>
> AI-assisted review report: https://github.com/yxieca/sonic-review-reports/pull/1. This comment is not an approval or a Changes Requested verdict.
>
> Revision-bound evidence: target head 551639a26205168f539a1deb66262442cc7aa426. The 2026-11-24 follow-up is bounded coordinator-only source review, not a fresh full panel; earlier inert results are reused, not new hardware or test-suite validation. Existing R1/R2/R3 discussions are referenced; no new target feedback has been submitted.

## Current Comment without a formal verdict

https://github.com/sonic-net/sonic-mgmt/pull/28850#issuecomment-new

> I reviewed the findings in https://github.com/yxieca/sonic-review-reports/pull/1 against target head 551639a26205168f539a1deb66262442cc7aa426. Before landing, please resolve or explain R1 (unconfirmed test-leak cleanup finishing normally) and R3 (vendor MINOR-to-MAJOR escalation missing power recovery). R2's probe-episode synchronization needs either a reliable boundary or an explicit, supported deferral/containment decision.
>
> These points are already discussed in the linked target threads; I am referencing those discussions rather than raising them as newly discovered issues. The warning-only cleanup decision and the author's probe-window explanation are acknowledged; the report records the remaining disagreement and its source/inert evidence limits. Please use the report IDs when explaining a correction or disagreement. No physical outage or new hardware validation is claimed.
>
> AI-assisted review report: https://github.com/yxieca/sonic-review-reports/pull/1. This comment is not an approval or a Changes Requested verdict.
>
> Revision-bound evidence: target head 551639a26205168f539a1deb66262442cc7aa426. The 2026-11-24 follow-up is bounded coordinator-only source review, not a fresh full panel; earlier inert results are reused, not new hardware or test-suite validation. Existing R1/R2/R3 discussions are referenced; no new target feedback has been submitted.

---

## Superseded old-SHA drafts — preserved history, not current submission text

# Human-operated feedback drafts: sonic-mgmt #28850

**STALE — current target head `551639a26205168f539a1deb66262442cc7aa426` differs from reviewed head `834b687c739eb0b5e72ad49770afc8a9a9cd6a30`.** The saved findings and drafts are historical, not current-head clearance. Source review of the changed scope is pending; do not submit these drafts as current feedback. The earlier plain-comment signal remains held and cannot authorize feedback at the new target revision.

Report: https://github.com/yxieca/sonic-review-reports/pull/1  
Target: https://github.com/sonic-net/sonic-mgmt/pull/28850  
Reviewed head: `834b687c739eb0b5e72ad49770afc8a9a9cd6a30`

These are draft text, not submitted reviews. Confirm the head, read existing discussion and revise to reflect your own judgment. Existing R1/R2/R3 discussions already cover these concerns; reference them rather than duplicating them. The signed-in person submitting is responsible for the verdict. No draft impersonates Ying or claims human approval not yet given.

## 1. Request-changes review draft

[Open target Files changed](https://github.com/sonic-net/sonic-mgmt/pull/28850/files), select **Review changes → Request changes**, and paste/edit:

> I reviewed the findings in https://github.com/yxieca/sonic-review-reports/pull/1 against the target change. Before landing, please resolve or explain R1 (unconfirmed test-leak cleanup finishing normally) and R3 (vendor MINOR-to-MAJOR escalation missing power recovery). R2's probe-episode synchronization needs either a reliable boundary or an explicit, supported deferral/containment decision.
>
> These points are already discussed in the linked target threads; I am referencing those discussions rather than raising them as newly discovered issues. Please use the report IDs when explaining a correction or disagreement. The report includes the exact reviewed revision, scope and evidence limits.
>
> AI-assisted review report: https://github.com/yxieca/sonic-review-reports/pull/1. This submission reflects my own review and decision.

## 2. Comment-as-questions draft

[Open target conversation](https://github.com/sonic-net/sonic-mgmt/pull/28850#issuecomment-new) and paste/edit:

> Following the existing discussions, could you clarify the remaining points in https://github.com/yxieca/sonic-review-reports/pull/1?
>
> - R1: what establishes unsuccessful teardown or verified cleanup if bulk withdrawal returns false? The warning-only decision is acknowledged.
> - R2: what ensures reinjection starts a new daemon episode if the recovery predicate observes the old No row before publication? Could this be safely deferred with an explicit containment?
> - R3: should the vendor recovery guard include the MINOR-to-MAJOR escalation case when MAJOR can remove power?
>
> I am asking for correction or explanation, not asserting a physical outage. The report distinguishes new-path gaps, the direct recovery regression, and source/inert versus hardware evidence.
>
> AI-assisted review report: https://github.com/yxieca/sonic-review-reports/pull/1. This comment is not an approval or a Changes Requested verdict.

## 3. Plain-comment feedback draft — prepared 2026-11-24

[Open the comment draft](https://yxieca.github.io/sonic-review-reports/sonic-mgmt-28850.html#comment). This is a plain comment with no formal verdict. It did not exist when the earlier comment decision was made; review this prepared text before renewing that decision.

> I reviewed the findings in https://github.com/yxieca/sonic-review-reports/pull/1 against target head 834b687c739eb0b5e72ad49770afc8a9a9cd6a30. Before landing, please resolve or explain R1 (unconfirmed test-leak cleanup finishing normally) and R3 (vendor MINOR-to-MAJOR escalation missing power recovery). R2's probe-episode synchronization needs either a reliable boundary or an explicit, supported deferral/containment decision.
>
> These points are already discussed in the linked target threads; I am referencing those discussions rather than raising them as newly discovered issues. The warning-only cleanup decision and the author's probe-window explanation are acknowledged; the report records the remaining disagreement and its source/inert evidence limits. Please use the report IDs when explaining a correction or disagreement. No physical outage or new hardware validation is claimed.
>
> AI-assisted review report: https://github.com/yxieca/sonic-review-reports/pull/1. This comment is not an approval or a Changes Requested verdict.
>
> AI-assisted review, reviewed by Ying Xie (@yxieca).

## If blockers are later resolved

Reconcile evidence and update issue dispositions first. Then replace the two action drafts with **comment without approval** and **approve with comment**. Keep any remaining nits explicitly optional, preserve this report backlink, and retain the previous draft/disposition history through normal commits. Never offer an approval link merely because CI is green.
