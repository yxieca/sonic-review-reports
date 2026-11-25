# Self-contained reader drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/35

Reviewed target head: `90125a5622a28de95d79c22d240fa1b887d33a8d`. Existing issue dispositions, coverage limits and target-feedback receipts remain unchanged. This presentation update submits no target feedback.



## Questions without verdict

Questions for correction or explanation; no formal verdict.

**P2 — establish per-rank entitlement before raw cross-queue fairness.** `tests/snappi_tests/rocev2/test_rocev2_qp_fairness_dcqcn.py:81–107,128–141,195–200` accepts at least four ports, cycles senders over Q3/Q4, and compares raw rates to one 30% spread bound without checking weights/entitlement. With five ports, four senders split 2:2 and weights20:10, correct weighted within-queue sharing gives33.33/16.67/33.33/16.67, a50% raw spread incorrectly rejected. Verify/select equal per-rank entitlement or retain within-queue fairness and normalize cross-queue expectations by weights and sender counts; do not merely increase tolerance. Exact four-port selection alone still needs the2:1 weight premise. This is a prerequisite/oracle mismatch, not an independently observed RoCE hardware failure. Optional live-positive-sample and zero/missing CNP-denominator questions remain unexecuted qualifications, not extra blockers.

Source: https://github.com/sonic-net/sonic-mgmt/blob/90125a5622a28de95d79c22d240fa1b887d33a8d/tests/snappi_tests/rocev2/test_rocev2_qp_fairness_dcqcn.py#L81-L107

Reviewed target head: `90125a5622a28de95d79c22d240fa1b887d33a8d`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/35.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Request changes with comment

Request-changes reader draft for the retained findings below.

**P2 — establish per-rank entitlement before raw cross-queue fairness.** `tests/snappi_tests/rocev2/test_rocev2_qp_fairness_dcqcn.py:81–107,128–141,195–200` accepts at least four ports, cycles senders over Q3/Q4, and compares raw rates to one 30% spread bound without checking weights/entitlement. With five ports, four senders split 2:2 and weights20:10, correct weighted within-queue sharing gives33.33/16.67/33.33/16.67, a50% raw spread incorrectly rejected. Verify/select equal per-rank entitlement or retain within-queue fairness and normalize cross-queue expectations by weights and sender counts; do not merely increase tolerance. Exact four-port selection alone still needs the2:1 weight premise. This is a prerequisite/oracle mismatch, not an independently observed RoCE hardware failure. Optional live-positive-sample and zero/missing CNP-denominator questions remain unexecuted qualifications, not extra blockers.

Source: https://github.com/sonic-net/sonic-mgmt/blob/90125a5622a28de95d79c22d240fa1b887d33a8d/tests/snappi_tests/rocev2/test_rocev2_qp_fairness_dcqcn.py#L81-L107

Reviewed target head: `90125a5622a28de95d79c22d240fa1b887d33a8d`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/35.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Prior draft history

The prior wording is preserved in the preceding report commit. This update expands author-facing explanations only; it does not change findings, severity, source coverage, target verdict or submission state.
