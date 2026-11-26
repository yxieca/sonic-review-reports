# Human-operated target drafts

Target: https://github.com/sonic-net/sonic-host-services/pull/521
Reviewed HEAD: `c818b032d08fce97d8679074b159185c52747f1f`
Report: REPORT_PR_URL

## Comment without approval

The inspected producer preserves the setup-owned Python installation, data/unit payloads, controlled service enablement/no-start behavior, Rust release/debug handoff and the existing hostcfgd test assertions while improving test isolation. No blocking introduced source issue was established in the reviewed scope.

**Nonblocking: describe the native Cargo and published Bazel dependency selections separately.** [README.bazel.md](https://github.com/sonic-net/sonic-host-services/blob/c818b032d08fce97d8679074b159185c52747f1f/README.bazel.md#L18-L23) says the daemon selects sysinfo 0.40.3 “to match Cargo.lock”, but the unchanged [application lock](https://github.com/sonic-net/sonic-host-services/blob/c818b032d08fce97d8679074b159185c52747f1f/Cargo.lock#L671-L675) resolves sysinfo **0.40.4**. Cargo also resolves regex **1.13.2**, while the selected published Bazel graph supplies **0.40.3 / 1.13.1**; procfs **0.18.0** is shared. The PR body already acknowledges these differences. The guide also lists the data package as 1.0.0, while `data/debian/changelog` declares `1.0-1`. Please update the durable guide to give the actual data version and both dependency selections accurately, avoiding an implication of dependency or binary equivalence. This documentation error does not establish a runtime regression: the relevant source/API comparison found no demonstrated supported failure, and no native execution or artifact equivalence probe was performed by this review.

The note is nonblocking. Source acceptance is separate from containing-image adoption, native behavior and target submission. Reviewer builds, imports, tests, service/DB operations, installation and hardware probes were not performed. Reviewed HEAD: `c818b032d08fce97d8679074b159185c52747f1f`. Full report: REPORT_PR_URL

## Approve with nonblocking comment

The inspected producer preserves the setup-owned Python installation, data/unit payloads, controlled service enablement/no-start behavior, Rust release/debug handoff and the existing hostcfgd test assertions while improving test isolation. No blocking introduced source issue was established in the reviewed scope.

**Nonblocking: describe the native Cargo and published Bazel dependency selections separately.** [README.bazel.md](https://github.com/sonic-net/sonic-host-services/blob/c818b032d08fce97d8679074b159185c52747f1f/README.bazel.md#L18-L23) says the daemon selects sysinfo 0.40.3 “to match Cargo.lock”, but the unchanged [application lock](https://github.com/sonic-net/sonic-host-services/blob/c818b032d08fce97d8679074b159185c52747f1f/Cargo.lock#L671-L675) resolves sysinfo **0.40.4**. Cargo also resolves regex **1.13.2**, while the selected published Bazel graph supplies **0.40.3 / 1.13.1**; procfs **0.18.0** is shared. The PR body already acknowledges these differences. The guide also lists the data package as 1.0.0, while `data/debian/changelog` declares `1.0-1`. Please update the durable guide to give the actual data version and both dependency selections accurately, avoiding an implication of dependency or binary equivalence. This documentation error does not establish a runtime regression: the relevant source/API comparison found no demonstrated supported failure, and no native execution or artifact equivalence probe was performed by this review.

The note is nonblocking. Source acceptance is separate from containing-image adoption, native behavior and target submission. Reviewer builds, imports, tests, service/DB operations, installation and hardware probes were not performed. Reviewed HEAD: `c818b032d08fce97d8679074b159185c52747f1f`. Full report: REPORT_PR_URL
