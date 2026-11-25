# Reader drafts: sonic-build-infra #7

Report: https://github.com/yxieca/sonic-review-reports/pull/58

## Questions

Could you reconcile R1 before landing? The documented default APT update still selects rules_distroless .20, absent from the newly selected canonical registry and BCR. Its generated root is separate from the normal .26 root. Please preserve or deliberately migrate the resolver/default and lock-input provenance together.

Nonblocking R2/R3: could you clarify the restricted mtree grammar and reject or normalize missing final LF and ambiguous bare hierarchical names? Metadata and archive interpretation can differ for those forms, but no supported production caller emitting them was established. These guardrails can be addressed separately; default TAR callers are not claimed broken.

Full review and severity history: https://github.com/yxieca/sonic-review-reports/pull/58. No real DEB assembly or archive payload probe was executed by this review.

## Request changes

Please resolve R1 before landing: the endpoint migration leaves the documented default APT updater requesting a resolver version unavailable in its selected registries. Reconcile compatible publication or deliberately migrate the generated-root default and recorded lock-input contract.

R2/R3 are nonblocking input-contract hardening, not acceptance conditions: clarify/enforce the flat mtree grammar and normalization to prevent metadata/archive disagreement for unsupported or malformed forms. N1/N2 and parent ordering also remain optional. Preserve the streaming improvement.

Review: https://github.com/yxieca/sonic-review-reports/pull/58. This feedback reflects the submitting reviewer's judgment; no executed package-corruption result is claimed.
