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