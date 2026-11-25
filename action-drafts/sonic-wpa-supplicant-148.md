# Reader drafts: sonic-wpa-supplicant148

Report: REPORT_PR_URL

## Comment

The MACSEC reply-length correction looks sound: wpa_scnprintf accumulates stored non-NUL bytes, preserves the buffer bound, and matches the control transports’ exact-length contract. The regression links the production formatter/helper and checks every capacity0–199 around the197-byte reply. Nonblocking N1: please add ./test-macsec_status to the tests/Makefile run-tests recipe; it is currently built through ALL but not run by that aggregate target, although the PR workflow runs it explicitly. Optional multi-association fixtures could further exercise repeated loop termination.

Reviewed HEAD:5c45e5df3363d59a45c5d43333d8f1af254e58e0. Full three-independent-general plus separate-SME source review and coordinator grounding. No compiler/native C tests, MACsec/DUT/SAI, build or runtime qualification executed by this review. Existing hosted unit-test success is external evidence. Check current CI and replies before submission. Report: REPORT_PR_URL.

## Approve

Source review supports this MACSEC reply-length correction; no introduced blocker was found. The stored-byte accumulation, NUL handling and association-loop stopping match actual control callers, and the production-linked boundary regression is appropriate. Nonblocking N1 can follow separately: invoke ./test-macsec_status from run-tests so the local aggregate executes it as well as building it. Check any still-pending CI before landing; approval here does not claim physical MACsec qualification.

Reviewed HEAD:5c45e5df3363d59a45c5d43333d8f1af254e58e0. Full three-independent-general plus separate-SME source review and coordinator grounding. No compiler/native C tests, MACsec/DUT/SAI, build or runtime qualification executed by this review. Existing hosted unit-test success is external evidence. Check current CI and replies before submission. Report: REPORT_PR_URL.
