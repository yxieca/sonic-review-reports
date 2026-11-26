<!-- target-approval-receipt-6069532769 -->

**Target approval already submitted — Waiting CI.** [Verified approval](https://github.com/sonic-net/sonic-linkmgrd/pull/362#pullrequestreview-6069532769) at `19e0b9c2c0082c1022c8f179f4dbb7499259e953`. Source approval is verified at the covered revision; remaining Azure CI is not yet green. Optional notes are not approval conditions. No target merge was performed. Historical reader drafts below must not be resubmitted as duplicate feedback.

# Current reader drafts: sonic-linkmgrd #362

## Comment
The source build/runtime design and production format-string correction are acceptable within the reviewed scope; no introduced blocker was established.

N1 correction verified. tools/bazel/swsscommon.bzl::_linkmgrd_swsscommon_impl now describes the actual public-header/shared-link split without the stale version label. Do not repost the old Common-version request. Only that comment and unused/redundant Python imports changed; no checker guard or runtime/test behavior changed.

Nonblocking evidence auditability — preserve the BEP/report association. tools/bazel/validate.py::build records test-events.jsonl’s SHA; test_reports/collect use and recheck its label/result/XML mapping, but .github/workflows/bazel.yml’s upload allowlist omits the file. In-job checking is valid; later artifact-only readers cannot replay that mapping/digest. Please retain a compact hashed receipt containing target, attempt, cache/execution/result/summary status, relative XML name and XML hash, or inspect and retain curated public-safe BEP. Do not blindly upload environment-bearing files. This can follow separately.

Optional test guards — extend tools/bazel/evidence_test.py and validate.py::collect rejection controls for duplicate identities/summary attempts, not-run/disabled testcase attributes, empty reports, URI decoding, parameter-instance completeness and installed-hash mismatch. The current source/tests were selected and no case loss was demonstrated; this is an enhancement, not a blocking floor issue.

Optional logging regression — src/common/SwssLogBackend.cpp::send now correctly uses Logger::write(priority,"%s",message). Existing logger fixtures do not protect literal-percent messages through that backend; add a small isolated format-capture case to preserve the fix. No Redis/service/new framework is required.

Reviewed HEAD:19e0b9c2c0082c1022c8f179f4dbb7499259e953, BASE926040f8a26c1affca07831a1b613be7291372bb. Original full three-general plus separate-SME review at5a4563b carried for unchanged bytes; new independent general/SME comment/import delta checks and coordinator grounding. No reviewer C++/Bazel/native/package/Redis/network/DUT execution or payload probe. Current hosted native results are external: two of three test targets executed, source-contract result cached. Source approval is not deployment/ABI certification. Report: https://github.com/yxieca/sonic-review-reports/pull/65. Check current revision, CI and replies before submission.

## Approve
Source approval with optional/nonblocking follow-ups that can be handled separately. This does not claim daemon startup, live networking/Redis or final image qualification.

N1 correction verified. tools/bazel/swsscommon.bzl::_linkmgrd_swsscommon_impl now describes the actual public-header/shared-link split without the stale version label. Do not repost the old Common-version request. Only that comment and unused/redundant Python imports changed; no checker guard or runtime/test behavior changed.

Nonblocking evidence auditability — preserve the BEP/report association. tools/bazel/validate.py::build records test-events.jsonl’s SHA; test_reports/collect use and recheck its label/result/XML mapping, but .github/workflows/bazel.yml’s upload allowlist omits the file. In-job checking is valid; later artifact-only readers cannot replay that mapping/digest. Please retain a compact hashed receipt containing target, attempt, cache/execution/result/summary status, relative XML name and XML hash, or inspect and retain curated public-safe BEP. Do not blindly upload environment-bearing files. This can follow separately.

Optional test guards — extend tools/bazel/evidence_test.py and validate.py::collect rejection controls for duplicate identities/summary attempts, not-run/disabled testcase attributes, empty reports, URI decoding, parameter-instance completeness and installed-hash mismatch. The current source/tests were selected and no case loss was demonstrated; this is an enhancement, not a blocking floor issue.

Optional logging regression — src/common/SwssLogBackend.cpp::send now correctly uses Logger::write(priority,"%s",message). Existing logger fixtures do not protect literal-percent messages through that backend; add a small isolated format-capture case to preserve the fix. No Redis/service/new framework is required.

Reviewed HEAD:19e0b9c2c0082c1022c8f179f4dbb7499259e953, BASE926040f8a26c1affca07831a1b613be7291372bb. Original full three-general plus separate-SME review at5a4563b carried for unchanged bytes; new independent general/SME comment/import delta checks and coordinator grounding. No reviewer C++/Bazel/native/package/Redis/network/DUT execution or payload probe. Current hosted native results are external: two of three test targets executed, source-contract result cached. Source approval is not deployment/ABI certification. Report: https://github.com/yxieca/sonic-review-reports/pull/65. Check current revision, CI and replies before submission.
