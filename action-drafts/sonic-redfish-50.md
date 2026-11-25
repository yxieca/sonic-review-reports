# Human-operated feedback drafts

## Questions

Could you fix the newly identified R2/R3? R1 was withdrawn: authoritative Git blob has the correct NUL expectation; the apparent mismatch was retrieval-related. R2: recordCompleted takes/resets the suppressed-read count and places it in detail, then overwrites detail with buildDetail before emitting; could the count be merged after route detail? R3: HTTP/1 handleContentLengthError sends an early401 for a logged-out body above4096 but below the global limit before handle/router, bypassing both new audit hooks; could that boundary be audited without copying raw target/header data? Separately, pinned HTTP/2 DEBUG still logs raw header values before auth. That sink is inherited, but the new CONFIG_DB DEBUG path enables it, so safe audit JSON does not make all DEBUG logs credential-safe. Please remove/constrain it before making that guarantee. Failed-account proposed UserName remains an explicit privacy-policy clarification, not an authorization-bypass claim.

Full source review at 8e26302ff30e0ee986add3bb2dae0a0ce28d394b: three independent general lenses, separate SME and coordinator grounding. No native C++ test, credentials, HTTP/syslog/Redis/D-Bus/service or BMC runtime operation was performed. Report: https://github.com/yxieca/sonic-review-reports/pull/31. Source conclusions and reported samples do not certify deployed behavior. Check current revision/replies/CI before use; nothing submits automatically.

## Request changes

Please correct R2/R3 before relying on the new audit verification/accounting: preserve suppressed-read counts through final detail construction; and cover the early HTTP/1 content-length401 exit with one redacted denied record. Add hook-level serialized suppression and early-refusal regressions, not only limiter or ordinary-auth mocks. The existing HTTP/2 raw-header DEBUG logger also requires removal/redaction or decoupling from safe read-audit enablement before advertising credential-safe DEBUG. Source controls were static/effect-closed; no actual credentials or network requests were tested. Keep the nonblocking failed-account input policy and sampling/upgrade completeness notes distinct from new runtime vulnerabilities.

Full source review at 8e26302ff30e0ee986add3bb2dae0a0ce28d394b: three independent general lenses, separate SME and coordinator grounding. No native C++ test, credentials, HTTP/syslog/Redis/D-Bus/service or BMC runtime operation was performed. Report: https://github.com/yxieca/sonic-review-reports/pull/31. Source conclusions and reported samples do not certify deployed behavior. Check current revision/replies/CI before use; nothing submits automatically.


### 2026-11-25 13:30 UTC — Author-reported combined-image test results

The target description now reports 142 passed, 0 failed, 0 errors and 0 skipped on a combined Redfish41/50 image identified by short revision 9d65f76 and build 351066, including seven audit-log cases. The current reviewed target head is unchanged. The reported generic audit cases do not specifically establish corrected suppressed-read accounting R2 or the early HTTP/1 oversized unauthenticated refusal R3. Those source-grounded concerns remain open; R1 remains withdrawn. The description acknowledges 500 rather than 503 bridge-down responses, leaving Retry-After unexercised. Results are author-reported, not independently run or exact-head-bound; the “202008 msft branch” heading does not verify requested 202608 applicability. No verdict change or duplicate target feedback.

[Observed target description](https://github.com/sonic-net/sonic-redfish/pull/50) at `8e26302ff30e0ee986add3bb2dae0a0ce28d394b`.
