# Current source follow-up drafts

## Comment
**Source follow-up:** `azure-pipelines.yml` changes only the integration job timeout from 60 to 75 minutes. The test commands, failure propagation, result publication, coverage conditions and thresholds are unchanged. This adds time to the existing job; it does not prove a successful integration run, resolve a test failure, relax assertions or establish runner capacity.

The previously completed source/native-origin and Subscribe/Poll corrections remain carried at unchanged source. R1 obsolete-checksum correction remains retired/resolved. Nonblocking N1 remains: `sonic_data_client/mixed_db_client.go` embeds the TMPDIR-derived filename in `PyCodeForYang` without lossless Python-literal quoting. A legitimate quote/backslash directory name can change syntax or the interpreted filename; pass the filename as data or serialize it losslessly. Existing questions7205039251 already raised this note; do not duplicate feedback.

Reviewed HEAD `f89a76c78373c94a3c840dc530e4d2f4d9e0a345`. Full report: https://github.com/yxieca/sonic-review-reports/pull/78. No native imports, compiler/build/tests, services, network or device/package probes were run by this review. Source acceptance, external review and current CI/integration readiness remain separate.

## Manual approval draft
**Source follow-up:** `azure-pipelines.yml` changes only the integration job timeout from 60 to 75 minutes. The test commands, failure propagation, result publication, coverage conditions and thresholds are unchanged. This adds time to the existing job; it does not prove a successful integration run, resolve a test failure, relax assertions or establish runner capacity.

The previously completed source/native-origin and Subscribe/Poll corrections remain carried at unchanged source. R1 obsolete-checksum correction remains retired/resolved. Nonblocking N1 remains: `sonic_data_client/mixed_db_client.go` embeds the TMPDIR-derived filename in `PyCodeForYang` without lossless Python-literal quoting. A legitimate quote/backslash directory name can change syntax or the interpreted filename; pass the filename as data or serialize it losslessly. Existing questions7205039251 already raised this note; do not duplicate feedback.

Reviewed HEAD `f89a76c78373c94a3c840dc530e4d2f4d9e0a345`. Full report: https://github.com/yxieca/sonic-review-reports/pull/78. No native imports, compiler/build/tests, services, network or device/package probes were run by this review. Source acceptance, external review and current CI/integration readiness remain separate.

Manual source-favorable draft only; check current source, external review and CI gates before any formal verdict. No automatic submission.