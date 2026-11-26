> **STALE — not for submission.** Needs Report Update: target advanced to `af0fa70af966032f46d90f0173411142e5d0e25a`. The author reports corrections to the remap oracle, counter windows, TTL origin and label repetition. Those claims are not yet source-verified; prior findings/coverage are historical and drafts are stale.

## Historical drafts

# Self-contained reader drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/33

Reviewed target head: `a8b9d1a0191ad78a0f030ae1849cd496c826668d`. Existing issue dispositions, coverage limits and target-feedback receipts remain unchanged. This presentation update submits no target feedback.



## Comment without approval

Comment without a formal verdict.

**E3-04 — make the remap observation distinguish mappings (nonblocking design correction).** `docs/testplan/scaleup/scaleup_esun_testplan.md:410` sends100 packets per CoS and expects100 per queue under both maps. Every bijective mapping, including an ignored remap, yields the same aggregate histogram. Repeat E3-01's per-CoS queue-counter deltas under each map or use unequal per-CoS counts, with explicit phase counter windows. Intended additional per-CoS attribution may resolve this; state it explicitly. This concerns prospective observables, not failure of an implemented ESUN feature.

**Other nonblocking clarifications:** at333–366,407–410,448–449 specify fresh subrun deltas and distinct required queues so prior traffic is not mistaken for current results. At435, captured input-TTL15 traffic is already TTL14: explain whether the original hop is included or restart with a fresh TTL15 frame. At425, fixed lower-byte/variable-upper-byte labels provide256 distinct values, so10000 sparse packets require explicitly permitted/weighted repetition rather than uniqueness. Preserve prospective scope; arithmetic/source evidence is not runtime ESUN qualification.

Source: https://github.com/sonic-net/sonic-mgmt/blob/a8b9d1a0191ad78a0f030ae1849cd496c826668d/docs/testplan/scaleup/scaleup_esun_testplan.md#L410

Reviewed target head: `a8b9d1a0191ad78a0f030ae1849cd496c826668d`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/33.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Questions without verdict

Questions for correction or explanation; no formal verdict.

**E3-04 — make the remap observation distinguish mappings (nonblocking design correction).** `docs/testplan/scaleup/scaleup_esun_testplan.md:410` sends100 packets per CoS and expects100 per queue under both maps. Every bijective mapping, including an ignored remap, yields the same aggregate histogram. Repeat E3-01's per-CoS queue-counter deltas under each map or use unequal per-CoS counts, with explicit phase counter windows. Intended additional per-CoS attribution may resolve this; state it explicitly. This concerns prospective observables, not failure of an implemented ESUN feature.

**Other nonblocking clarifications:** at333–366,407–410,448–449 specify fresh subrun deltas and distinct required queues so prior traffic is not mistaken for current results. At435, captured input-TTL15 traffic is already TTL14: explain whether the original hop is included or restart with a fresh TTL15 frame. At425, fixed lower-byte/variable-upper-byte labels provide256 distinct values, so10000 sparse packets require explicitly permitted/weighted repetition rather than uniqueness. Preserve prospective scope; arithmetic/source evidence is not runtime ESUN qualification.

Source: https://github.com/sonic-net/sonic-mgmt/blob/a8b9d1a0191ad78a0f030ae1849cd496c826668d/docs/testplan/scaleup/scaleup_esun_testplan.md#L410

Reviewed target head: `a8b9d1a0191ad78a0f030ae1849cd496c826668d`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/33.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Prior draft history

The prior wording is preserved in the preceding report commit. This update expands author-facing explanations only; it does not change findings, severity, source coverage, target verdict or submission state.
