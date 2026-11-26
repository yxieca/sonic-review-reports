# Current feedback drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/63

N1 is blocking; previous approval drafts are superseded and preserved in history.

## Questions

Could you correct the canonical registry description before approval (N1)? README.bazel.md says “canonical securely1g registry”, but .bazelrc selects sonic-net/sonic-bazel-registry/main. The reader-facing source ownership/reference must match the configured canonical source. This is a documentation requirement, not a runtime wrong-registry claim.

Documentation: https://github.com/sonic-net/sonic-dhcpmon/blob/65b99647b87eb0955009310c531d0fadcb840c60/README.bazel.md#L1-L8
Configuration: https://github.com/sonic-net/sonic-dhcpmon/blob/65b99647b87eb0955009310c531d0fadcb840c60/.bazelrc#L1-L7

N2/N3 checker/unaligned-input regression suggestions and Q1 provider-verification scope remain nonblocking. Full source review and history: https://github.com/yxieca/sonic-review-reports/pull/63. Reviewed head: 65b99647b87eb0955009310c531d0fadcb840c60. No native builds or runtime tests were executed by this review.

## Request changes

Please correct the canonical registry description before landing (N1, blocking). README.bazel.md says “canonical securely1g registry”, but .bazelrc selects sonic-net/sonic-bazel-registry/main. The reader-facing source ownership/reference must match the configured canonical source. This is a documentation requirement, not a runtime wrong-registry claim.

Documentation: https://github.com/sonic-net/sonic-dhcpmon/blob/65b99647b87eb0955009310c531d0fadcb840c60/README.bazel.md#L1-L8
Configuration: https://github.com/sonic-net/sonic-dhcpmon/blob/65b99647b87eb0955009310c531d0fadcb840c60/.bazelrc#L1-L7

N2/N3 checker/unaligned-input regression suggestions and Q1 provider-verification scope remain nonblocking. Full source review and history: https://github.com/yxieca/sonic-review-reports/pull/63. Reviewed head: 65b99647b87eb0955009310c531d0fadcb840c60. No native builds or runtime tests were executed by this review.
