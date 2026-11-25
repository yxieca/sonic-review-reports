# Human-operated feedback drafts

Full current-source review at fc8c24f01c4c3c3706957103226d0a7cd5ac3b73: three independent general lenses, separate SME and coordinator grounding. No GPIO/leak injection/native/HW/Redis/service operation was executed. Report: https://github.com/yxieca/sonic-review-reports/pull/29. Current branchmaster; original main request preserved. Explicit selected/merged sources do not prove installed image versions. Check current head/replies and dependencies; no automatic action.

## Questions

Could the verifier check consumer compatibility before any shared marker write? R1: main runs per-sensor default/CRITICAL injection cycles and CLI mutation before calling check_state_db, so --verify-db can reach the unsupported-consumer skip only after earlier injections. A final clear cannot undo a mitigation already dispatched. Please move the preflight ahead of all shared cycles, or require an explicitly private unwatched directory/compatible consumer. Current coherent health/leak sampling and real-hardware precedence are source-supported. Existing review/dependency concerns should be reconciled in their original discussion; merged943/650 protection is behind the candidate gitlinks, not established as installed. The fault-after-confirmed-leak gate question remains a policy qualification, not a physical-outcome assertion.

Full current-source review at fc8c24f01c4c3c3706957103226d0a7cd5ac3b73: three independent general lenses, separate SME and coordinator grounding. No GPIO/leak injection/native/HW/Redis/service operation was executed. Report: https://github.com/yxieca/sonic-review-reports/pull/29. Current branchmaster; original main request preserved. Explicit selected/merged sources do not prove installed image versions. Check current head/replies and dependencies; no automatic action.

## Request changes

Please fix R1 before treating the runtime verifier as safely refusing incompatible consumers: enforce the required test-origin producer/consumer preflight before any shared-marker injection phase, not only inside the later DB check; preserve private unwatched-dir use and physical-leak precedence. Add a whole-main negative call-order control. Current README no-injection assurance is broader than the caller enforces. Existing coherent-sample safety fix is verified, and existing daemon/kernel selection/review gates remain separate. Do not assume a merged dependency is built into this image or copy GPIO/mitigation policy without its source contract.

Full current-source review at fc8c24f01c4c3c3706957103226d0a7cd5ac3b73: three independent general lenses, separate SME and coordinator grounding. No GPIO/leak injection/native/HW/Redis/service operation was executed. Report: https://github.com/yxieca/sonic-review-reports/pull/29. Current branchmaster; original main request preserved. Explicit selected/merged sources do not prove installed image versions. Check current head/replies and dependencies; no automatic action.
