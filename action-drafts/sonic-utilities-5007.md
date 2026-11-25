# Current-head feedback hold — 2026-11-24

Report: https://github.com/yxieca/sonic-review-reports/pull/18
Target: https://github.com/sonic-net/sonic-utilities/pull/5007
Observed current head: `9d777d3ef609e3bd5d9abb8040e12fe6e7f49c8f`
Historical full-review head: `8fb199d6da3e909fea0cf2261ef4afd23f8e373a`

R1/N1/N2 source corrections are verified in a bounded delta check. Q1 has a downstream follow-up acknowledgment, not deployed validation. Required current-head independent changed-scope coverage is pending. No current actionable question/request-changes/approval draft is prepared. Historical drafts below must not be submitted as current feedback; they refer to corrected code and are preserved only for history.

---

## Preserved historical drafts (superseded; not current feedback)

# Human-operated feedback drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/18
Reviewed SHA: `8fb199d6da3e909fea0cf2261ef4afd23f8e373a`
Coverage: completed three independent general passes, separate SME and coordinator grounding.

## Questions

For reviewed SHA 8fb199d6da3e909fea0cf2261ef4afd23f8e373a, could you clarify/fix the declared-but-unavailable CPO handling in the existing availability-isolation thread (https://github.com/sonic-net/sonic-utilities/pull/5007#discussion_r4679062681)? The resolver runs before the per-target loop, so a healthy later endpoint is not processed.

Full batch review report: https://github.com/yxieca/sonic-review-reports/pull/18. Three independent general passes and the separate SME are completed and grounded. No hardware or firmware validation was executed. This is a question without approval or a formal verdict; check current head and replies and avoid duplicating already answered feedback.

## Request changes

At reviewed SHA 8fb199d6da3e909fea0cf2261ef4afd23f8e373a, the full batch source review in https://github.com/yxieca/sonic-review-reports/pull/18 identifies R1: the all-target resolver can abort before healthy declared endpoints are processed. Please address the existing availability-isolation thread (https://github.com/sonic-net/sonic-utilities/pull/5007#discussion_r4679062681), preserving invalid-index rejection and adding the missing-CPO/healthy-target case. This references existing feedback rather than adding a duplicate finding.

Three independent general passes and separate SME are complete; no hardware or firmware validation was executed for this assessment. Check the current head, author replies and report before submitting. This draft does not assert anyone else's approval.
