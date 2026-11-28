# Self-contained reader drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/52

Reviewed target head: `bf03c7306bf774dfa747182a9788e64512207dbd`. Existing issue dispositions, coverage limits and target-feedback receipts remain unchanged. This presentation update submits no target feedback.



## Questions without verdict

Questions for correction or explanation; no formal verdict.

**G1 — shared-client worker import is rejected by the dependency checker (P2).** `tests/common/pygnmi_client.py:27` imports `tests.pygnmi_subscription`. The actual repository policy permits common/common2/same-feature imports and named root exceptions, but not this feature-root module from the shared client. The retained exact-head CI and policy inspection reject this import, preventing dependency-check admission. Preserve the lightweight fresh-spawn entry by choosing an approved shared location or a narrowly justified policy accommodation. Do not blindly move it under `tests.common`: its initializer eagerly imports reboot/config_reload/port_toggle and Ansible dependencies, defeating the lightweight entry. Check both dependency-policy admission and fresh-spawn behavior after correction. The already-raised partial initial-POLL snapshot issue is nonblocking for the current no-retry caller; do not duplicate it.

Source: https://github.com/sonic-net/sonic-mgmt/blob/bf03c7306bf774dfa747182a9788e64512207dbd/tests/common/pygnmi_client.py#L27

Reviewed target head: `bf03c7306bf774dfa747182a9788e64512207dbd`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/52.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Request changes with comment

Request-changes reader draft for the retained findings below.

**G1 — shared-client worker import is rejected by the dependency checker (P2).** `tests/common/pygnmi_client.py:27` imports `tests.pygnmi_subscription`. The actual repository policy permits common/common2/same-feature imports and named root exceptions, but not this feature-root module from the shared client. The retained exact-head CI and policy inspection reject this import, preventing dependency-check admission. Preserve the lightweight fresh-spawn entry by choosing an approved shared location or a narrowly justified policy accommodation. Do not blindly move it under `tests.common`: its initializer eagerly imports reboot/config_reload/port_toggle and Ansible dependencies, defeating the lightweight entry. Check both dependency-policy admission and fresh-spawn behavior after correction. The already-raised partial initial-POLL snapshot issue is nonblocking for the current no-retry caller; do not duplicate it.

Source: https://github.com/sonic-net/sonic-mgmt/blob/bf03c7306bf774dfa747182a9788e64512207dbd/tests/common/pygnmi_client.py#L27

Reviewed target head: `bf03c7306bf774dfa747182a9788e64512207dbd`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/52.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Prior draft history

The prior wording is preserved in the preceding report commit. This update expands author-facing explanations only; it does not change findings, severity, source coverage, target verdict or submission state.
