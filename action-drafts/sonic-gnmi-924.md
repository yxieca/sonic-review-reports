# Current source follow-up feedback

## Comment
**Native-source origin request reconciled at `b75f80523deb71f7c4810596a92dfb19e0e4182a`.** `tools/ci/native_subscription.py` downloads sonic-net Common and Management sources at immutable revisions d8d59ad0/7259c3a1 and checks the declared SHA256 before reuse/extraction. Bazel overrides point SDK/runtime/SWIG/codegen builds at those checkouts; private native Go preparation explicitly replaces Management Common with the same local checkout before tidy/vendor. This addresses source-origin consistency within that independent race-test graph, not universal equality with the ordinary registry/Make graph.

R1 obsolete checksum remains fixed. Nonblocking N1 remains: `mixed_db_client.go` substitutes TMPDIR-derived filename into `PyCodeForYang` without lossless literal escaping. Valid quotes/backslashes can change syntax or filename; pass filename as data. The author's private-directory and per-instance openImage rationale matches the inspected callers but does not fix N1. Existing questions7205039251 are preserved, not repeated.

This source review ran no compiler, imports, tests, archives/packages, Redis/gNMI/TLS services, network or DUT operations. Independent native race checks deliberately return on first Recv error before full origin/subscription execution; successful race evidence must not be generalized to full native subscription/write, ABI or deployment qualification. Full report: https://github.com/yxieca/sonic-review-reports/pull/78.

## Approval draft
**Native-source origin request reconciled at `b75f80523deb71f7c4810596a92dfb19e0e4182a`.** `tools/ci/native_subscription.py` downloads sonic-net Common and Management sources at immutable revisions d8d59ad0/7259c3a1 and checks the declared SHA256 before reuse/extraction. Bazel overrides point SDK/runtime/SWIG/codegen builds at those checkouts; private native Go preparation explicitly replaces Management Common with the same local checkout before tidy/vendor. This addresses source-origin consistency within that independent race-test graph, not universal equality with the ordinary registry/Make graph.

R1 obsolete checksum remains fixed. Nonblocking N1 remains: `mixed_db_client.go` substitutes TMPDIR-derived filename into `PyCodeForYang` without lossless literal escaping. Valid quotes/backslashes can change syntax or filename; pass filename as data. The author's private-directory and per-instance openImage rationale matches the inspected callers but does not fix N1. Existing questions7205039251 are preserved, not repeated.

This source review ran no compiler, imports, tests, archives/packages, Redis/gNMI/TLS services, network or DUT operations. Independent native race checks deliberately return on first Recv error before full origin/subscription execution; successful race evidence must not be generalized to full native subscription/write, ABI or deployment qualification. Full report: https://github.com/yxieca/sonic-review-reports/pull/78.

Manual source-favorable draft only; current external review/CI/integration gates and freshness remain separate.