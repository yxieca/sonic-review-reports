# Current human-operated feedback drafts

Target: https://github.com/sonic-net/sonic-sairedis/pull/2233
Reviewed HEAD: `aeac40152501f811f3db1e603644eeef923d6483`
Report: https://github.com/yxieca/sonic-review-reports/pull/75

## Comment without a verdict

The follow-up at `aeac40152501f811f3db1e603644eeef923d6483` resolves the previously raised non-ASAN fortification policy at source, including metadata C and Python compilation, while preserving the ASAN exception. The original suggestion and author response remain in their existing discussion; this is not a request to repeat that feedback.

**Nonblocking: finish the existing documentation correction.** The new [service-free list](https://github.com/sonic-net/sonic-sairedis/blob/aeac40152501f811f3db1e603644eeef923d6483/docs/bazel.md#L110-L133) now includes eleven targets, but other sections of `docs/bazel.md` and `runtime_packages.md` still describe older Common/Infra/SAI selections, source-count and launcher behavior. Please align the remaining prose with `MODULE.bazel`, the current 365-source/373-owner-pair contract and declared-runtime launcher, or mark historical examples explicitly. This is the retained N1 accuracy note, not a new runtime defect.

**Nonblocking: recognize split macro options in the hardening audit.** [check_fortify.py](https://github.com/sonic-net/sonic-sairedis/blob/aeac40152501f811f3db1e603644eeef923d6483/bazel/ci/check_fortify.py#L30-L49) filters joined `-D_FORTIFY_SOURCE...` and `-U_FORTIFY_SOURCE` arguments. A later legal split pair such as `-U`, `_FORTIFY_SOURCE` is ignored, allowing the checker to accept an earlier level-3 suffix even though the final macro operation undefines it. Please normalize joined and split `-D`/`-U` arguments before checking order and add argument-array cases. The current component rules use joined options; this guard weakness does **not** mean the present source correction fails. Verification was an inert metadata-list comparison, not a compiler or checker execution.

Both notes are nonblocking. Canonical merge CI currently fails a reviewed-Make-input digest guard after target-branch VPP changes; reconcile that integration separately rather than treating exact-head fork success as a canonical pass. The target remains draft. No reviewer compiler, tests, ASAN, SAI/DUT or native payload probe was run. Reviewed HEAD: `aeac40152501f811f3db1e603644eeef923d6483`. Full report: https://github.com/yxieca/sonic-review-reports/pull/75.

## Source-favorable approval draft, manual and freshness-gated

The follow-up at `aeac40152501f811f3db1e603644eeef923d6483` resolves the previously raised non-ASAN fortification policy at source, including metadata C and Python compilation, while preserving the ASAN exception. The original suggestion and author response remain in their existing discussion; this is not a request to repeat that feedback.

**Nonblocking: finish the existing documentation correction.** The new [service-free list](https://github.com/sonic-net/sonic-sairedis/blob/aeac40152501f811f3db1e603644eeef923d6483/docs/bazel.md#L110-L133) now includes eleven targets, but other sections of `docs/bazel.md` and `runtime_packages.md` still describe older Common/Infra/SAI selections, source-count and launcher behavior. Please align the remaining prose with `MODULE.bazel`, the current 365-source/373-owner-pair contract and declared-runtime launcher, or mark historical examples explicitly. This is the retained N1 accuracy note, not a new runtime defect.

**Nonblocking: recognize split macro options in the hardening audit.** [check_fortify.py](https://github.com/sonic-net/sonic-sairedis/blob/aeac40152501f811f3db1e603644eeef923d6483/bazel/ci/check_fortify.py#L30-L49) filters joined `-D_FORTIFY_SOURCE...` and `-U_FORTIFY_SOURCE` arguments. A later legal split pair such as `-U`, `_FORTIFY_SOURCE` is ignored, allowing the checker to accept an earlier level-3 suffix even though the final macro operation undefines it. Please normalize joined and split `-D`/`-U` arguments before checking order and add argument-array cases. The current component rules use joined options; this guard weakness does **not** mean the present source correction fails. Verification was an inert metadata-list comparison, not a compiler or checker execution.

Both notes are nonblocking. Canonical merge CI currently fails a reviewed-Make-input digest guard after target-branch VPP changes; reconcile that integration separately rather than treating exact-head fork success as a canonical pass. The target remains draft. No reviewer compiler, tests, ASAN, SAI/DUT or native payload probe was run. Reviewed HEAD: `aeac40152501f811f3db1e603644eeef923d6483`. Full report: https://github.com/yxieca/sonic-review-reports/pull/75.

Source-favorable draft only: review current non-draft status and CI/integration gates before choosing any formal approval; this page does not submit or release those gates.

## Prior target feedback

The historical R1 suggestion was already submitted as issuecomment7202764228; do not repeat it. The original feedback remains in the report history.
