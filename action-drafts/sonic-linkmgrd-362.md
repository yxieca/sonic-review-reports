# Reader drafts: sonic-linkmgrd #362

Report: REPORT_PR_URL

## Comment

The source build/runtime design and production format-string correction are acceptable within the reviewed scope; no introduced blocker was established.

Nonblocking documentation — correct the Common version in tools/bazel/swsscommon.bzl::_linkmgrd_swsscommon_impl. The comment says0.0.9, while MODULE.bazel selects0.0.8-qualified source; the actual provider split is correct. Remove the stale version or identify the chosen revision. README’s39production-source count is correct and should not be changed.

Nonblocking evidence auditability — preserve the BEP/report association. tools/bazel/validate.py::build records test-events.jsonl’s SHA; test_reports/collect use and recheck its label/result/XML mapping, but .github/workflows/bazel.yml’s upload allowlist omits the file. In-job checking is valid; later artifact-only readers cannot replay that mapping/digest. Please retain a compact hashed receipt containing target, attempt, cache/execution/result/summary status, relative XML name and XML hash, or inspect and retain curated public-safe BEP. Do not blindly upload environment-bearing files. This can follow separately.

Optional test guards — extend tools/bazel/evidence_test.py and validate.py::collect rejection controls for duplicate identities/summary attempts, not-run/disabled testcase attributes, empty reports, URI decoding, parameter-instance completeness and installed-hash mismatch. The current source/tests were selected and no case loss was demonstrated; this is an enhancement, not a blocking floor issue.

Optional logging regression — src/common/SwssLogBackend.cpp::send now correctly uses Logger::write(priority,"%s",message). Existing logger fixtures do not protect literal-percent messages through that backend; add a small isolated format-capture case to preserve the fix. No Redis/service/new framework is required.

Reviewed HEAD:5a4563b1ccd21bfbc915f4e165f778e49ea269a7, BASE926040f8a26c1affca07831a1b613be7291372bb. Full three-independent-general plus separate-SME source review and coordinator grounding. No reviewer C++/Bazel/native/package/Redis/network/DUT execution or payload probe. Current hosted native results are external: two of three test targets executed, source-contract result cached. Source approval is not deployment/ABI certification. Report: REPORT_PR_URL. Check current revision, CI and replies before submission.

## Approve

Source approval with optional/nonblocking follow-ups that can be handled separately. This does not claim daemon startup, live networking/Redis or final image qualification.

Nonblocking documentation — correct the Common version in tools/bazel/swsscommon.bzl::_linkmgrd_swsscommon_impl. The comment says0.0.9, while MODULE.bazel selects0.0.8-qualified source; the actual provider split is correct. Remove the stale version or identify the chosen revision. README’s39production-source count is correct and should not be changed.

Nonblocking evidence auditability — preserve the BEP/report association. tools/bazel/validate.py::build records test-events.jsonl’s SHA; test_reports/collect use and recheck its label/result/XML mapping, but .github/workflows/bazel.yml’s upload allowlist omits the file. In-job checking is valid; later artifact-only readers cannot replay that mapping/digest. Please retain a compact hashed receipt containing target, attempt, cache/execution/result/summary status, relative XML name and XML hash, or inspect and retain curated public-safe BEP. Do not blindly upload environment-bearing files. This can follow separately.

Optional test guards — extend tools/bazel/evidence_test.py and validate.py::collect rejection controls for duplicate identities/summary attempts, not-run/disabled testcase attributes, empty reports, URI decoding, parameter-instance completeness and installed-hash mismatch. The current source/tests were selected and no case loss was demonstrated; this is an enhancement, not a blocking floor issue.

Optional logging regression — src/common/SwssLogBackend.cpp::send now correctly uses Logger::write(priority,"%s",message). Existing logger fixtures do not protect literal-percent messages through that backend; add a small isolated format-capture case to preserve the fix. No Redis/service/new framework is required.

Reviewed HEAD:5a4563b1ccd21bfbc915f4e165f778e49ea269a7, BASE926040f8a26c1affca07831a1b613be7291372bb. Full three-independent-general plus separate-SME source review and coordinator grounding. No reviewer C++/Bazel/native/package/Redis/network/DUT execution or payload probe. Current hosted native results are external: two of three test targets executed, source-contract result cached. Source approval is not deployment/ABI certification. Report: REPORT_PR_URL. Check current revision, CI and replies before submission.
