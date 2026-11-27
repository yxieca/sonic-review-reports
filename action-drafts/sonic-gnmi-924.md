# Current decision/freshness hold — gNMI #924

Target: https://github.com/sonic-net/sonic-gnmi/pull/924
Current target HEAD: `f89a76c78373c94a3c840dc530e4d2f4d9e0a345`.

**Source follow-up queued; current feedback drafts are inert.** The target advanced after the completed d6bf4251 source review. The new exact changed scope has not yet been independently reviewed. The request is input to review, not a verified new blocking defect or a completed source assessment. Existing full source coverage and R1-resolved/N1-nonblocking dispositions are preserved below as the prior snapshot; current decision readiness is held until this newly raised source-origin scope is grounded.

No target approval, comment, review dismissal, CI retry or native validation is performed by this metadata hold. Do not use or repeat historical drafts while the follow-up is queued.

## Historical editable text — do not submit

# Current source follow-up drafts

## Comment
**Test-only correction source-reviewed:** `gnmi_server/server_test.go::runTestSubscribe` now completes the initial POLL Subscribe through Sync before calling Poll on the same stream. Non-POLL subscriptions use a per-subtest cancel/close/join sequence, and the expected-error check handles nil safely. This supports stream-read ordering and client-side lifetime isolation; it is not proof of server-side goroutine completion or elimination of every shared-mock race.

**Nonblocking N1 remains:** `sonic_data_client/mixed_db_client.go` still interpolates the TMPDIR-derived filename into `PyCodeForYang` without lossless Python-string quoting. Valid quote/backslash directory names can change syntax or the interpreted filename. Pass the filename as data or encode a lossless literal. The existing questions7205039251 already raised this note; do not duplicate them. Trusted environment input is not a reproduced remote-execution vulnerability.

The native-source origin reconciliation and retired checksum R1 remain carried unchanged from the prior covered head. Current review `d6bf42518cd70243f7495d9977db8fcac60b949b`; report https://github.com/yxieca/sonic-review-reports/pull/78. No native imports, compiler/build/tests, services, network/device/package operations or target action were performed. Check external review/CI/freshness before any formal verdict.

## Manual source-favorable approval draft
**Test-only correction source-reviewed:** `gnmi_server/server_test.go::runTestSubscribe` now completes the initial POLL Subscribe through Sync before calling Poll on the same stream. Non-POLL subscriptions use a per-subtest cancel/close/join sequence, and the expected-error check handles nil safely. This supports stream-read ordering and client-side lifetime isolation; it is not proof of server-side goroutine completion or elimination of every shared-mock race.

**Nonblocking N1 remains:** `sonic_data_client/mixed_db_client.go` still interpolates the TMPDIR-derived filename into `PyCodeForYang` without lossless Python-string quoting. Valid quote/backslash directory names can change syntax or the interpreted filename. Pass the filename as data or encode a lossless literal. The existing questions7205039251 already raised this note; do not duplicate them. Trusted environment input is not a reproduced remote-execution vulnerability.

The native-source origin reconciliation and retired checksum R1 remain carried unchanged from the prior covered head. Current review `d6bf42518cd70243f7495d9977db8fcac60b949b`; report https://github.com/yxieca/sonic-review-reports/pull/78. No native imports, compiler/build/tests, services, network/device/package operations or target action were performed. Check external review/CI/freshness before any formal verdict.

Source-favorable manual draft only; this page does not submit or clear external/CI/integration gates.