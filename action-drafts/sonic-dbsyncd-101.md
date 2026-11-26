# Current reader drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/61
N3/Q1 blocking; N1/N2 deferred. Existing target threads already cover the requests; avoid duplicate posts. Prior approval drafts remain in history only.

## Questions

Could you address the existing dependency-description and fixture-source requests before landing? README.bazel.md names Distroless .25, while the owner and fixture MODULE.bazel select .26 (N3). Please make the documented version match actual selection. The test-only fixture git_override still uses a personal buildimage fork (Q1); please switch to the canonical repository origin and verify equivalent pinned source rather than assuming endpoint changes preserve archive/source identity.

Existing discussions: https://github.com/sonic-net/sonic-dbsyncd/pull/101#discussion_r4694416620 and https://github.com/sonic-net/sonic-dbsyncd/pull/101#discussion_r4694519381 . These are before-approval traceability/ownership requirements, not allegations of current production failure. N1 wheel Maintainer metadata and N2 timeout cleanup are deferred follow-ups. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/61. Reviewed head: 8a7eb9f3da4ea3e350c35dcc25635ee4c0b0a413. No native tests executed by this review.

## Request changes

Please address the existing dependency-description and fixture-source requests before landing? README.bazel.md names Distroless .25, while the owner and fixture MODULE.bazel select .26 (N3). Please make the documented version match actual selection. The test-only fixture git_override still uses a personal buildimage fork (Q1); please switch to the canonical repository origin and verify equivalent pinned source rather than assuming endpoint changes preserve archive/source identity.

Existing discussions: https://github.com/sonic-net/sonic-dbsyncd/pull/101#discussion_r4694416620 and https://github.com/sonic-net/sonic-dbsyncd/pull/101#discussion_r4694519381 . These are before-approval traceability/ownership requirements, not allegations of current production failure. N1 wheel Maintainer metadata and N2 timeout cleanup are deferred follow-ups. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/61. Reviewed head: 8a7eb9f3da4ea3e350c35dcc25635ee4c0b0a413. No native tests executed by this review.
