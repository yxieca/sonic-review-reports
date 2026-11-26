<!-- source-evidence-hold-0830-571496d20d6de6aef24884ae69cb54003c3b7998 -->

**Historical drafts — not actionable at the current head.**

**Needs Report Update — current revision not yet qualified.** Target advanced from the covered revision `8e26302ff30e0ee986add3bb2dae0a0ce28d394b` to `571496d20d6de6aef24884ae69cb54003c3b7998`. Changed source and its reached dependency contracts require independent reconciliation. Prior completed full-panel and bounded follow-up evidence remain preserved; historical findings are not current-head qualification. The author reports the earlier concerns are fixed; those corrections require source verification, not acceptance by assertion. Our earlier Changes Requested review remains a historical/current review receipt, not permission to submit another action. The coverage gap is not a confirmed code defect. Do not submit historical feedback drafts.

# Self-contained reader drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/31

Reviewed target head: `8e26302ff30e0ee986add3bb2dae0a0ce28d394b`. Existing issue dispositions, coverage limits and target-feedback receipts remain unchanged. This presentation update submits no target feedback.



## Questions without verdict

Questions for correction or explanation; no formal verdict.

**R2 — admitted read discards suppressed-read accounting (P2).** `redfish-audit/bmcweb/redfish_audit_hook.hpp::recordCompleted` (548–627) takes/resets the rate limiter count into record.detail, then overwrites it with buildDetail for ordinary reads. After exceeding50 DEBUG reads/second, the later admitted Systems GET loses detail.suppressed; suppressed reads never reached Sink, so its sequence cannot reconstruct them. Merge the count after final route-detail construction and cover hook-to-serialized output, not just the limiter. This is source-derived new accounting loss, not executed syslog evidence.

**R3 — early HTTP/1 oversized logged-out401 bypasses audit (P2).** The pinned HTTP/1 handleContentLengthError (http/http_connection.hpp:543–660) returns401 for logged-out content length>4096 below the global limit, outside the100-continue branch, before later handle/router audit hooks added by patches/0012-Record-an-audit-trail-of-Redfish-requests.patch. The denied response has no audit record/suppression accounting. Instrument that early boundary with parsed method and a constant unauthenticated marker, retaining raw-target/header redaction; cover exactly-one-record behavior. This is audit omission, not authentication bypass or permission to log rejected content.

**Q1 — inherited credential-log claim boundary:** the pinned HTTP/2 header callback (http/http2_connection.hpp:457–467) logs raw header values before authentication. New CONFIG_DB read-audit DEBUG also raises general bmcweb DEBUG. Remove/redact the ordinary sink or decouple enablement before claiming universally credential-safe DEBUG; safe audit JSON alone does not sanitize other logging. This is inherited sink/new enablement qualification, not a newly proven exploit. Failed-account UserName policy and sampling/upgrade completeness remain nonblocking. R1 remains withdrawn as a source-retrieval artifact; do not revive it. Author-reported combined-image tests do not specifically establish R2/R3 repair.

Source: https://github.com/sonic-net/sonic-redfish/blob/8e26302ff30e0ee986add3bb2dae0a0ce28d394b/redfish-audit/bmcweb/redfish_audit_hook.hpp#L548-L627
Pinned HTTP/1: https://github.com/openbmc/bmcweb/blob/6926d43047446a1f08d4b157d48a30221ae8f87e/http/http_connection.hpp#L543-L660
Pinned HTTP/2: https://github.com/openbmc/bmcweb/blob/6926d43047446a1f08d4b157d48a30221ae8f87e/http/http2_connection.hpp#L457-L467

Reviewed target head: `8e26302ff30e0ee986add3bb2dae0a0ce28d394b`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/31.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Request changes with comment

Request-changes reader draft for the retained findings below.

**R2 — admitted read discards suppressed-read accounting (P2).** `redfish-audit/bmcweb/redfish_audit_hook.hpp::recordCompleted` (548–627) takes/resets the rate limiter count into record.detail, then overwrites it with buildDetail for ordinary reads. After exceeding50 DEBUG reads/second, the later admitted Systems GET loses detail.suppressed; suppressed reads never reached Sink, so its sequence cannot reconstruct them. Merge the count after final route-detail construction and cover hook-to-serialized output, not just the limiter. This is source-derived new accounting loss, not executed syslog evidence.

**R3 — early HTTP/1 oversized logged-out401 bypasses audit (P2).** The pinned HTTP/1 handleContentLengthError (http/http_connection.hpp:543–660) returns401 for logged-out content length>4096 below the global limit, outside the100-continue branch, before later handle/router audit hooks added by patches/0012-Record-an-audit-trail-of-Redfish-requests.patch. The denied response has no audit record/suppression accounting. Instrument that early boundary with parsed method and a constant unauthenticated marker, retaining raw-target/header redaction; cover exactly-one-record behavior. This is audit omission, not authentication bypass or permission to log rejected content.

**Q1 — inherited credential-log claim boundary:** the pinned HTTP/2 header callback (http/http2_connection.hpp:457–467) logs raw header values before authentication. New CONFIG_DB read-audit DEBUG also raises general bmcweb DEBUG. Remove/redact the ordinary sink or decouple enablement before claiming universally credential-safe DEBUG; safe audit JSON alone does not sanitize other logging. This is inherited sink/new enablement qualification, not a newly proven exploit. Failed-account UserName policy and sampling/upgrade completeness remain nonblocking. R1 remains withdrawn as a source-retrieval artifact; do not revive it. Author-reported combined-image tests do not specifically establish R2/R3 repair.

Source: https://github.com/sonic-net/sonic-redfish/blob/8e26302ff30e0ee986add3bb2dae0a0ce28d394b/redfish-audit/bmcweb/redfish_audit_hook.hpp#L548-L627
Pinned HTTP/1: https://github.com/openbmc/bmcweb/blob/6926d43047446a1f08d4b157d48a30221ae8f87e/http/http_connection.hpp#L543-L660
Pinned HTTP/2: https://github.com/openbmc/bmcweb/blob/6926d43047446a1f08d4b157d48a30221ae8f87e/http/http2_connection.hpp#L457-L467

Reviewed target head: `8e26302ff30e0ee986add3bb2dae0a0ce28d394b`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/31.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Prior draft history

The prior wording is preserved in the preceding report commit. This update expands author-facing explanations only; it does not change findings, severity, source coverage, target verdict or submission state.
