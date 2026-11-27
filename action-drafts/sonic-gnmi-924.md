# Current decision/freshness hold — gNMI #924

Target: https://github.com/sonic-net/sonic-gnmi/pull/924
Current target HEAD: `b75f80523deb71f7c4810596a92dfb19e0e4182a`.

**Current source follow-up in progress; current feedback drafts are inert.** A new human review asks for reconciliation of the native subscription check's selected Common/Management source origins, pins and hashes. The request is input to review, not a verified new blocking defect or a completed source assessment. Existing full source coverage and R1-resolved/N1-nonblocking dispositions are preserved below as the prior snapshot; current decision readiness is held until this newly raised source-origin scope is grounded.

No target approval, comment, review dismissal, CI retry or native validation is performed by this metadata hold. Do not use or repeat historical drafts while the follow-up is queued.

## Historical editable text — do not submit

# Current decision/freshness hold — gNMI #924

Target: https://github.com/sonic-net/sonic-gnmi/pull/924
Current target HEAD: `be95e865091d7757b335b101919723d265712aed`.

**Source follow-up queued; current feedback drafts are inert.** A new human review asks for reconciliation of the native subscription check's selected Common/Management source origins, pins and hashes. The request is input to review, not a verified new blocking defect or a completed source assessment. Existing full source coverage and R1-resolved/N1-nonblocking dispositions are preserved below as the prior snapshot; current decision readiness is held until this newly raised source-origin scope is grounded.

No target approval, comment, review dismissal, CI retry or native validation is performed by this metadata hold. Do not use or repeat historical drafts while the follow-up is queued.

## Historical editable text — do not submit

# Current feedback

## Comment
**Nonblocking N1 remains:** `sonic_data_client/mixed_db_client.go` still interpolates the TMPDIR-derived `config_db.json.tmp` filename into `PyCodeForYang` using an unescaped double-quoted Python literal. A legitimate quote/backslash directory name can change syntax or the interpreted filename. Pass the filename as data or serialize a lossless literal. The existing [questions](https://github.com/sonic-net/sonic-gnmi/pull/924#issuecomment-7205039251) already raised this note; do not duplicate them. Trusted process environment is not a reproduced remote-execution vulnerability. No native interpreter/Go/test execution was performed.

Reviewed HEAD `be95e865091d7757b335b101919723d265712aed`; target is now non-draft. R1 checksum correction remains resolved. Full report: https://github.com/yxieca/sonic-review-reports/pull/78. Source acceptance, CI/integration readiness and formal approval remain separate.

## Approval draft
**Nonblocking N1 remains:** `sonic_data_client/mixed_db_client.go` still interpolates the TMPDIR-derived `config_db.json.tmp` filename into `PyCodeForYang` using an unescaped double-quoted Python literal. A legitimate quote/backslash directory name can change syntax or the interpreted filename. Pass the filename as data or serialize a lossless literal. The existing [questions](https://github.com/sonic-net/sonic-gnmi/pull/924#issuecomment-7205039251) already raised this note; do not duplicate them. Trusted process environment is not a reproduced remote-execution vulnerability. No native interpreter/Go/test execution was performed.

Reviewed HEAD `be95e865091d7757b335b101919723d265712aed`; target is now non-draft. R1 checksum correction remains resolved. Full report: https://github.com/yxieca/sonic-review-reports/pull/78. Source acceptance, CI/integration readiness and formal approval remain separate.

Source-favorable manual draft; recheck current head and remaining checks before choosing a formal verdict.