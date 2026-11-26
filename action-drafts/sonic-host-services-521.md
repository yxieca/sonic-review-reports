# Archived source review — target MERGED

<!-- terminal-archive-report77-20261126 -->
Target: https://github.com/sonic-net/sonic-host-services/pull/521 · Report: https://github.com/yxieca/sonic-review-reports/pull/77

The target merged at `2026-11-26T22:03:51Z` with [merge commit `fe679db2d7c8ea4b1d8a83289de8313589ea690b`](https://github.com/sonic-net/sonic-host-services/commit/fe679db2d7c8ea4b1d8a83289de8313589ea690b). Reviewed/terminal head: `c818b032d08fce97d8679074b159185c52747f1f`. [Source approval with nonblocking notes](https://github.com/sonic-net/sonic-host-services/pull/521#pullrequestreview-6080961264) was submitted before the merge. This monitor did not merge or submit feedback to the target. Temporary action pages are retired; prior drafts and waiting-state prose below are historical, not current submission instructions.

## Terminal finding outcomes

| ID | Outcome |
|---|---|
| N1 | Nonblocking validation-description scope correction remains a recorded recommendation; merge does not prove the documentation was corrected. |
| N2 | Nonblocking partial-diagnostics robustness recommendation retained; merge does not prove the collector was changed. |

The completed three-general-plus-separate-SME source coverage, dissent, source limits and discussion remain intact. No fresh source review, build, native test, install or hardware probe was performed for archival.


## Historical reader drafts — not actionable

# Human-operated target drafts

Target: https://github.com/sonic-net/sonic-host-services/pull/521
Reviewed HEAD: `c818b032d08fce97d8679074b159185c52747f1f`
Report: https://github.com/yxieca/sonic-review-reports/pull/77

## Comment without approval

The inspected producer preserves the setup-owned Python installation, data/unit payloads, controlled service enablement/no-start behavior, Rust release/debug handoff and the existing hostcfgd test assertions while improving test isolation. No blocking introduced source issue was established in the reviewed scope.

**Nonblocking: describe the native Cargo and published Bazel dependency selections separately.** [README.bazel.md](https://github.com/sonic-net/sonic-host-services/blob/c818b032d08fce97d8679074b159185c52747f1f/README.bazel.md#L18-L23) says the daemon selects sysinfo 0.40.3 “to match Cargo.lock”, but the unchanged [application lock](https://github.com/sonic-net/sonic-host-services/blob/c818b032d08fce97d8679074b159185c52747f1f/Cargo.lock#L671-L675) resolves sysinfo **0.40.4**. Cargo also resolves regex **1.13.2**, while the selected published Bazel graph supplies **0.40.3 / 1.13.1**; procfs **0.18.0** is shared. The PR body already acknowledges these differences. The guide also lists the data package as 1.0.0, while `data/debian/changelog` declares `1.0-1`. Please update the durable guide to give the actual data version and both dependency selections accurately, avoiding an implication of dependency or binary equivalence. This documentation error does not establish a runtime regression: the relevant source/API comparison found no demonstrated supported failure, and no native execution or artifact equivalence probe was performed by this review.

The note is nonblocking. Source acceptance is separate from containing-image adoption, native behavior and target submission. Reviewer builds, imports, tests, service/DB operations, installation and hardware probes were not performed. Reviewed HEAD: `c818b032d08fce97d8679074b159185c52747f1f`. Full report: https://github.com/yxieca/sonic-review-reports/pull/77

## Approve with nonblocking comment

The inspected producer preserves the setup-owned Python installation, data/unit payloads, controlled service enablement/no-start behavior, Rust release/debug handoff and the existing hostcfgd test assertions while improving test isolation. No blocking introduced source issue was established in the reviewed scope.

**Nonblocking: describe the native Cargo and published Bazel dependency selections separately.** [README.bazel.md](https://github.com/sonic-net/sonic-host-services/blob/c818b032d08fce97d8679074b159185c52747f1f/README.bazel.md#L18-L23) says the daemon selects sysinfo 0.40.3 “to match Cargo.lock”, but the unchanged [application lock](https://github.com/sonic-net/sonic-host-services/blob/c818b032d08fce97d8679074b159185c52747f1f/Cargo.lock#L671-L675) resolves sysinfo **0.40.4**. Cargo also resolves regex **1.13.2**, while the selected published Bazel graph supplies **0.40.3 / 1.13.1**; procfs **0.18.0** is shared. The PR body already acknowledges these differences. The guide also lists the data package as 1.0.0, while `data/debian/changelog` declares `1.0-1`. Please update the durable guide to give the actual data version and both dependency selections accurately, avoiding an implication of dependency or binary equivalence. This documentation error does not establish a runtime regression: the relevant source/API comparison found no demonstrated supported failure, and no native execution or artifact equivalence probe was performed by this review.

The note is nonblocking. Source acceptance is separate from containing-image adoption, native behavior and target submission. Reviewer builds, imports, tests, service/DB operations, installation and hardware probes were not performed. Reviewed HEAD: `c818b032d08fce97d8679074b159185c52747f1f`. Full report: https://github.com/yxieca/sonic-review-reports/pull/77
