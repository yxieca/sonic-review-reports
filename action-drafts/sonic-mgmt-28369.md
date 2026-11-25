# Self-contained reader drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/15

Reviewed target head: `f445237b36b18c0db54d4cd669399f3dbcb4281d`. Existing issue dispositions, coverage limits and target-feedback receipts remain unchanged. This presentation update submits no target feedback.



## Questions without verdict

Questions for correction or explanation; no formal verdict.

**R1 — raw shared-helper reload can skip module checked recovery (P2 integration cutoff).** `tests/gnmi_benchmark/helpers.py::_restore_config` at the reviewed target adds config reload -y after file restoration. At integration cutoff42205428fbe07ed1d12ea4e8b0eb654b78891726, the module finalizer in test_gnmi_benchmark.py (67–130) calls that helper before checked config_reload. A raw-reload error exits before the checked database/service/interface/BGP recovery is attempted even if the saved file was restored; it propagates as teardown error, not silently green module teardown. Keep file-only restoration and the one module-owned checked reload, or explain recovery ownership. Successful paths also add per-case/extra module reloads. This is later upstream integration scope, not a retrospectively proven original-head failure or physical result. Existing external assessment raises the same issue; no duplicate feedback or edit of the historic approval is requested.

Source: https://github.com/sonic-net/sonic-mgmt/blob/f445237b36b18c0db54d4cd669399f3dbcb4281d/tests/gnmi_benchmark/helpers.py#L144-L152
Integration caller: https://github.com/sonic-net/sonic-mgmt/blob/42205428fbe07ed1d12ea4e8b0eb654b78891726/tests/gnmi_benchmark/test_gnmi_benchmark.py#L67-L130

Reviewed target head: `f445237b36b18c0db54d4cd669399f3dbcb4281d`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/15.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Request changes

Request-changes reader draft for the retained findings below.

**R1 — raw shared-helper reload can skip module checked recovery (P2 integration cutoff).** `tests/gnmi_benchmark/helpers.py::_restore_config` at the reviewed target adds config reload -y after file restoration. At integration cutoff42205428fbe07ed1d12ea4e8b0eb654b78891726, the module finalizer in test_gnmi_benchmark.py (67–130) calls that helper before checked config_reload. A raw-reload error exits before the checked database/service/interface/BGP recovery is attempted even if the saved file was restored; it propagates as teardown error, not silently green module teardown. Keep file-only restoration and the one module-owned checked reload, or explain recovery ownership. Successful paths also add per-case/extra module reloads. This is later upstream integration scope, not a retrospectively proven original-head failure or physical result. Existing external assessment raises the same issue; no duplicate feedback or edit of the historic approval is requested.

Source: https://github.com/sonic-net/sonic-mgmt/blob/f445237b36b18c0db54d4cd669399f3dbcb4281d/tests/gnmi_benchmark/helpers.py#L144-L152
Integration caller: https://github.com/sonic-net/sonic-mgmt/blob/42205428fbe07ed1d12ea4e8b0eb654b78891726/tests/gnmi_benchmark/test_gnmi_benchmark.py#L67-L130

Reviewed target head: `f445237b36b18c0db54d4cd669399f3dbcb4281d`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/15.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Prior draft history

The prior wording is preserved in the preceding report commit. This update expands author-facing explanations only; it does not change findings, severity, source coverage, target verdict or submission state.
