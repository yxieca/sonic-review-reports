# Self-contained reader drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/14

Reviewed target head: `9a4ae5ec6499fd408bcb26de50a1f63e283122ea`. Existing issue dispositions, coverage limits and target-feedback receipts remain unchanged. This presentation update submits no target feedback.



## Comment without approval

Comment without a formal verdict.

**Q1 — tiny VLAN prefix support (nonblocking).** In `tests/bgp/test_bgp_dual_asn.py` speaker address selection (176–177,184–185), parent /30 or /31 yields child /31 or /32; excluding both endpoints leaves an empty randint range. Should the helper use prefix-aware usable-address rules or reject insufficient subnets clearly? Standard inspected topologies use larger prefixes, so no failure on those supported inputs is claimed. The endpoint correction remains source-favorable. This question was already posted; do not duplicate it.

Source: https://github.com/sonic-net/sonic-mgmt/blob/9a4ae5ec6499fd408bcb26de50a1f63e283122ea/tests/bgp/test_bgp_dual_asn.py#L176-L185

Reviewed target head: `9a4ae5ec6499fd408bcb26de50a1f63e283122ea`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/14.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Approve with comment

Source-favorable approval reader draft; nonblocking questions below do not become approval conditions.

**Q1 — tiny VLAN prefix support (nonblocking).** In `tests/bgp/test_bgp_dual_asn.py` speaker address selection (176–177,184–185), parent /30 or /31 yields child /31 or /32; excluding both endpoints leaves an empty randint range. Should the helper use prefix-aware usable-address rules or reject insufficient subnets clearly? Standard inspected topologies use larger prefixes, so no failure on those supported inputs is claimed. The endpoint correction remains source-favorable. This question was already posted; do not duplicate it.

Source: https://github.com/sonic-net/sonic-mgmt/blob/9a4ae5ec6499fd408bcb26de50a1f63e283122ea/tests/bgp/test_bgp_dual_asn.py#L176-L185

Reviewed target head: `9a4ae5ec6499fd408bcb26de50a1f63e283122ea`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/14.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Prior draft history

The prior wording is preserved in the preceding report commit. This update expands author-facing explanations only; it does not change findings, severity, source coverage, target verdict or submission state.
