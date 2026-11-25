# Self-contained reader drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/45

Reviewed target head: `eafb857f06ae3445b7abfacef4f7b657d452320f`. Existing issue dispositions, coverage limits and target-feedback receipts remain unchanged. This presentation update submits no target feedback.



## Questions without verdict

Questions for correction or explanation; no formal verdict.

**R1 — unavailable-container prerequisite must precede managed TLS provisioning (P2, existing thread).** `tests/gnmi/test_gnmi_poll.py:17` replaces the old setup fixture with gnmi_tls. The old tests/gnmi/conftest.py prerequisite skipped an absent gnmi container before mutation; `_gnmi_tls_flow` in tests/common/fixtures/grpc_fixtures.py performs checkpoint/certificate/config work before `_restart_gnoi_server` raises for absence. On topology-any unsupported DUTs this changes skip into mutated setup/error. Add a selected-DUT availability prerequisite guaranteed before provisioning, without running legacy and managed setup together. This is test setup/reporting correctness, not false POLL packet success or a newly observed device incident. Resolve the existing availability discussion rather than post duplicate feedback: https://github.com/sonic-net/sonic-mgmt/pull/28601#discussion_r4518760414. Previous native-client architecture and fixed description concerns stay superseded.

Source: https://github.com/sonic-net/sonic-mgmt/blob/eafb857f06ae3445b7abfacef4f7b657d452320f/tests/gnmi/test_gnmi_poll.py#L17
Reviewed target head: `eafb857f06ae3445b7abfacef4f7b657d452320f`. Retained source evidence and coverage limits reused; this audit ran no candidate code/native tests/build/device/service validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/45.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Request changes with comment

Request-changes reader draft for the retained findings below.

**R1 — unavailable-container prerequisite must precede managed TLS provisioning (P2, existing thread).** `tests/gnmi/test_gnmi_poll.py:17` replaces the old setup fixture with gnmi_tls. The old tests/gnmi/conftest.py prerequisite skipped an absent gnmi container before mutation; `_gnmi_tls_flow` in tests/common/fixtures/grpc_fixtures.py performs checkpoint/certificate/config work before `_restart_gnoi_server` raises for absence. On topology-any unsupported DUTs this changes skip into mutated setup/error. Add a selected-DUT availability prerequisite guaranteed before provisioning, without running legacy and managed setup together. This is test setup/reporting correctness, not false POLL packet success or a newly observed device incident. Resolve the existing availability discussion rather than post duplicate feedback: https://github.com/sonic-net/sonic-mgmt/pull/28601#discussion_r4518760414. Previous native-client architecture and fixed description concerns stay superseded.

Source: https://github.com/sonic-net/sonic-mgmt/blob/eafb857f06ae3445b7abfacef4f7b657d452320f/tests/gnmi/test_gnmi_poll.py#L17
Reviewed target head: `eafb857f06ae3445b7abfacef4f7b657d452320f`. Retained source evidence and coverage limits reused; this audit ran no candidate code/native tests/build/device/service validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/45.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Prior draft history

The prior wording is preserved in the preceding report commit. This update expands author-facing explanations only; it does not change findings, severity, source coverage, target verdict or submission state.
