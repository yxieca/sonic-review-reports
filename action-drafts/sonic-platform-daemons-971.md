# Archived source review — target MERGED

<!-- terminal-archive-report76-20261126 -->
Target: https://github.com/sonic-net/sonic-platform-daemons/pull/971 · Report: https://github.com/yxieca/sonic-review-reports/pull/76

The target merged at `2026-11-26T21:15:31Z` with [merge commit `0ca41544c73a1f1775f5a707e8e9e4f224064c01`](https://github.com/sonic-net/sonic-platform-daemons/commit/0ca41544c73a1f1775f5a707e8e9e4f224064c01). Reviewed/terminal head: `ee544e7495a0f1a97c6e46e31193b8d5af53c0fa`. [Source approval with nonblocking notes](https://github.com/sonic-net/sonic-platform-daemons/pull/971#pullrequestreview-6080533114) was submitted before the merge. This monitor did not merge or submit feedback to the target. Temporary action pages are retired; prior drafts and waiting-state prose below are historical, not current submission instructions.

## Terminal finding outcomes

| ID | Outcome |
|---|---|
| N1 | Nonblocking validation-description scope correction remains a recorded recommendation; merge does not prove the documentation was corrected. |
| N2 | Nonblocking partial-diagnostics robustness recommendation retained; merge does not prove the collector was changed. |

The completed three-general-plus-separate-SME source coverage, dissent, source limits and discussion remain intact. No fresh source review, build, native test, install or hardware probe was performed for archival.


## Historical reader drafts — not actionable

# Human-operated target drafts

Target: https://github.com/sonic-net/sonic-platform-daemons/pull/971
Reviewed HEAD: `ee544e7495a0f1a97c6e46e31193b8d5af53c0fa`
Report: https://github.com/yxieca/sonic-review-reports/pull/76

## Comment without approval

The reviewed source preserves the existing setup.py-owned distribution contracts, explicit generated-protobuf inputs, per-wheel installation/metadata checks, and the two ycabled assertions while adding channel cleanup. No blocking introduced source issue was established in the declared scope.

**Nonblocking: describe the exact validation scope.** The new [README's original-Azure-suite description](https://github.com/sonic-net/sonic-platform-daemons/blob/ee544e7495a0f1a97c6e46e31193b8d5af53c0fa/README.bazel.md#L33) should explicitly exclude ycabled's privileged black-box suite: [the new unit runner](https://github.com/sonic-net/sonic-platform-daemons/blob/ee544e7495a0f1a97c6e46e31193b8d5af53c0fa/tests/bazel/unit_runner.py#L18-L34) does not set `BB_ENABLE=1`, while the unchanged [Azure invocation](https://github.com/sonic-net/sonic-platform-daemons/blob/ee544e7495a0f1a97c6e46e31193b8d5af53c0fa/azure-pipelines.yml#L179-L189) does. [The existing collection hook](https://github.com/sonic-net/sonic-platform-daemons/blob/ee544e7495a0f1a97c6e46e31193b8d5af53c0fa/sonic-ycabled/blackbox/conftest.py#L19-L47) therefore excludes those black-box tests before collection, so they are not represented as skipped JUnit cases. Keeping that privileged suite outside this ordinary Bazel application is reasonable; please label the unit/source-suite receipts accordingly. Also, the [installed-interface probe](https://github.com/sonic-net/sonic-platform-daemons/blob/ee544e7495a0f1a97c6e46e31193b8d5af53c0fa/tests/bazel/installed_runtime_test.py#L153-L196) checks chassisd's `shutdown_allowed` publication for default/unimplemented and explicitly protected `ModuleBase` providers, not thermalctld thermal-policy/action execution. Please narrow the PR's installed-thermal-shutdown wording to the contract actually exercised. This is a documentation/evidence-scope correction, not a new daemon or shutdown defect.

**Nonblocking: retain available evidence when collection itself fails.** [The always-run evidence step](https://github.com/sonic-net/sonic-platform-daemons/blob/ee544e7495a0f1a97c6e46e31193b8d5af53c0fa/.github/workflows/bazel.yml#L73-L86) calls [collect_evidence.py::main](https://github.com/sonic-net/sonic-platform-daemons/blob/ee544e7495a0f1a97c6e46e31193b8d5af53c0fa/tests/bazel/collect_evidence.py#L38-L99). Its early `info`/`cquery` calls and artifact `read_bytes()` are not caught; a build that failed before producing a wheel/TAR can make collection exit before copying later test logs or writing `provenance.json`. Missing or malformed receipt archives can do the same. Please collect independent artifact/test sections under bounded exception handling, append errors, write a partial provenance record in a finalization path, and then return failure. The original failed build remains failed; this suggestion is about preserving diagnostics, not a demonstrated false-green workflow.

Both notes are nonblocking. Reviewer builds, tests, native imports, installation and hardware/runtime probes were not performed. Reviewed HEAD: `ee544e7495a0f1a97c6e46e31193b8d5af53c0fa`. Full report: https://github.com/yxieca/sonic-review-reports/pull/76

## Approve with nonblocking comments

The reviewed source preserves the existing setup.py-owned distribution contracts, explicit generated-protobuf inputs, per-wheel installation/metadata checks, and the two ycabled assertions while adding channel cleanup. No blocking introduced source issue was established in the declared scope.

**Nonblocking: describe the exact validation scope.** The new [README's original-Azure-suite description](https://github.com/sonic-net/sonic-platform-daemons/blob/ee544e7495a0f1a97c6e46e31193b8d5af53c0fa/README.bazel.md#L33) should explicitly exclude ycabled's privileged black-box suite: [the new unit runner](https://github.com/sonic-net/sonic-platform-daemons/blob/ee544e7495a0f1a97c6e46e31193b8d5af53c0fa/tests/bazel/unit_runner.py#L18-L34) does not set `BB_ENABLE=1`, while the unchanged [Azure invocation](https://github.com/sonic-net/sonic-platform-daemons/blob/ee544e7495a0f1a97c6e46e31193b8d5af53c0fa/azure-pipelines.yml#L179-L189) does. [The existing collection hook](https://github.com/sonic-net/sonic-platform-daemons/blob/ee544e7495a0f1a97c6e46e31193b8d5af53c0fa/sonic-ycabled/blackbox/conftest.py#L19-L47) therefore excludes those black-box tests before collection, so they are not represented as skipped JUnit cases. Keeping that privileged suite outside this ordinary Bazel application is reasonable; please label the unit/source-suite receipts accordingly. Also, the [installed-interface probe](https://github.com/sonic-net/sonic-platform-daemons/blob/ee544e7495a0f1a97c6e46e31193b8d5af53c0fa/tests/bazel/installed_runtime_test.py#L153-L196) checks chassisd's `shutdown_allowed` publication for default/unimplemented and explicitly protected `ModuleBase` providers, not thermalctld thermal-policy/action execution. Please narrow the PR's installed-thermal-shutdown wording to the contract actually exercised. This is a documentation/evidence-scope correction, not a new daemon or shutdown defect.

**Nonblocking: retain available evidence when collection itself fails.** [The always-run evidence step](https://github.com/sonic-net/sonic-platform-daemons/blob/ee544e7495a0f1a97c6e46e31193b8d5af53c0fa/.github/workflows/bazel.yml#L73-L86) calls [collect_evidence.py::main](https://github.com/sonic-net/sonic-platform-daemons/blob/ee544e7495a0f1a97c6e46e31193b8d5af53c0fa/tests/bazel/collect_evidence.py#L38-L99). Its early `info`/`cquery` calls and artifact `read_bytes()` are not caught; a build that failed before producing a wheel/TAR can make collection exit before copying later test logs or writing `provenance.json`. Missing or malformed receipt archives can do the same. Please collect independent artifact/test sections under bounded exception handling, append errors, write a partial provenance record in a finalization path, and then return failure. The original failed build remains failed; this suggestion is about preserving diagnostics, not a demonstrated false-green workflow.

Both notes are nonblocking. Reviewer builds, tests, native imports, installation and hardware/runtime probes were not performed. Reviewed HEAD: `ee544e7495a0f1a97c6e46e31193b8d5af53c0fa`. Full report: https://github.com/yxieca/sonic-review-reports/pull/76
