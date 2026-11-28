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
## Readiness observation — 2026-11-27 18:30 Pacific
At unchanged reviewed HEAD `f89a76c78373c94a3c840dc530e4d2f4d9e0a345`, [qualified approval coverage](https://github.com/sonic-net/sonic-gnmi/pull/924#issuecomment-7232265567) now records **196/196 changed files covered**, supported by the [current-head administrator approval](https://github.com/sonic-net/sonic-gnmi/pull/924#pullrequestreview-6095158125). The four formal required checks are successful; the observed Azure aggregate, integration and memory-leak checks are also successful. Target is OPEN, non-draft and mergeable; no effective Changes Requested or unresolved blocking review thread was observed.

**Ready to Merge describes the target's observed readiness only.** It neither authorizes nor performs a target merge, target feedback or premature report archival. Source conclusions and completed independent coverage are unchanged: R1 remains resolved; N1 remains a nonblocking follow-up already raised in the existing question. Approval and CI receipts are external evidence, not this reviewer's test execution or proof N1 was fixed. No additional reviewer decision or duplicate feedback is required by this readiness update.
