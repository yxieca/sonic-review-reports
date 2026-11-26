<!-- current-source-hold-624bbde249936b1eba44b98f3f4f49595c896fe8 -->

**Historical drafts — not actionable at the current head.**

**Needs Report Update — current revision not yet qualified.** Target advanced to `624bbde249936b1eba44b98f3f4f49595c896fe8` after the completed source assessment at `5240b3d4505534b82848a7b9c9e073be25663e4a`. The author reports a correction to the existing ganged-interface discussion; this is a reported fix pending independent changed-scope verification, not confirmed resolution of R1 or Q1. Two earlier human approvals are now dismissed; their historical reasoning and test claims remain retained, not current-head acceptance. Original completed general/SME coverage and stable finding IDs remain historical, not current-revision clearance. Prior findings and completed full-review history remain preserved; the coverage gap is not a confirmed code defect. Historical feedback drafts must not be submitted.

# Self-contained reader drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/19

Reviewed target head: `5240b3d4505534b82848a7b9c9e073be25663e4a`. Existing issue dispositions, coverage limits and target-feedback receipts remain unchanged. This presentation update submits no target feedback.



## Questions without verdict

Questions for correction or explanation; no formal verdict.

**R1 — single-interface resolution can abort readable ganged DOM (P2, existing related thread).** `cpoutil/main.py::show_interface_dom` (1144–1215) calls resolve_interface for each physical member using one logical name. An active ganged index(1,2) intersecting static mappings(1,) and(2,) is accepted by physical-entry loading, but cpoutil/mapping.py:170–265 raises one-interface ambiguity before DOM reads. The base reads members directly; the exception escapes the loop and can suppress earlier accumulated output. Preserve per-member reading where bank sharing is ambiguous, or use an established member-specific mapping while retaining ordinary bank caching. This is accepted-input source control flow, not a shipped-SKU failure. The existing ganged-member discussion is related, not our reproduced physical measurement: https://github.com/sonic-net/sonic-utilities/pull/5074#discussion_r4679055165. Q1 distinct member/bank views remains conditional; different Python objects do not prove different hardware banks.

Source: https://github.com/sonic-net/sonic-utilities/blob/5240b3d4505534b82848a7b9c9e073be25663e4a/cpoutil/main.py#L1144-L1215
Reviewed target head: `5240b3d4505534b82848a7b9c9e073be25663e4a`. Retained source evidence and coverage limits reused; this audit ran no candidate code/native tests/build/device/service validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/19.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Request changes with comment

Request-changes reader draft for the retained findings below.

**R1 — single-interface resolution can abort readable ganged DOM (P2, existing related thread).** `cpoutil/main.py::show_interface_dom` (1144–1215) calls resolve_interface for each physical member using one logical name. An active ganged index(1,2) intersecting static mappings(1,) and(2,) is accepted by physical-entry loading, but cpoutil/mapping.py:170–265 raises one-interface ambiguity before DOM reads. The base reads members directly; the exception escapes the loop and can suppress earlier accumulated output. Preserve per-member reading where bank sharing is ambiguous, or use an established member-specific mapping while retaining ordinary bank caching. This is accepted-input source control flow, not a shipped-SKU failure. The existing ganged-member discussion is related, not our reproduced physical measurement: https://github.com/sonic-net/sonic-utilities/pull/5074#discussion_r4679055165. Q1 distinct member/bank views remains conditional; different Python objects do not prove different hardware banks.

Source: https://github.com/sonic-net/sonic-utilities/blob/5240b3d4505534b82848a7b9c9e073be25663e4a/cpoutil/main.py#L1144-L1215
Reviewed target head: `5240b3d4505534b82848a7b9c9e073be25663e4a`. Retained source evidence and coverage limits reused; this audit ran no candidate code/native tests/build/device/service validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/19.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Prior draft history

The prior wording is preserved in the preceding report commit. This update expands author-facing explanations only; it does not change findings, severity, source coverage, target verdict or submission state.
