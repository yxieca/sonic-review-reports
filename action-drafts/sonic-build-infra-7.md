# Reader drafts: sonic-build-infra #7

Report: https://github.com/yxieca/sonic-review-reports/pull/58

## Questions

Could R1–R3 be addressed or explained before accepting the new interfaces? R1: the documented default APT updater still selects rules_distroless0.9.4.sonic.20, but the new canonical registry publishes only.26 and BCR lacks.20; its separate generated root does not inherit the normal root’s.26. Please align publication/default/lock-input provenance rather than changing the constant alone. R2: Python includes an unterminated final mtree record, while selected libarchive3.7.4 drops it, leaving checksums/control metadata for an absent file. R3: bare directory a then bare file f passes the flat Python map as root f, while libarchive emits a/f. Could the manifest be validated/canonicalized once so summary, conffiles and emitted payload agree, with no-LF and bare/full-path package controls? Default TAR callers are not claimed broken. Q1 nonblocking: could parent-first order be enforced or normalized? N1/N2 nonblocking: narrow pin-preservation wording and retain the new host-process test XML.

Reviewed HEAD:57f537b9ec9cedc797a19ffade867b3b285a3a9f. Full three-independent-general plus separate-SME source review and coordinator grounding. Only source/metadata and closed in-memory Python controls were executed; no Bazel/APT/compiler/native tests, real DEB creation or archive payload probe. Existing current-head hosted CI is external evidence. Report: https://github.com/yxieca/sonic-review-reports/pull/58. Check current source and replies before submitting; target feedback remains unsubmitted.

## Request changes

Please correct R1–R3 (P2) before accepting this revision: (R1) make the separate default APT update resolver.20 available at the canonical registry, or deliberately migrate its default and recorded lock-input contract together; (R2) reject/normalize missing final LF so the last mtree file cannot be checksummed but omitted by BSDtar; (R3) reject or canonicalize ambiguous bare mtree names so Python destinations/conffiles match the emitted archive. Keep the streaming payload/backpressure mechanism and default TAR compatibility. Add complete mtree membership/md5sums controls for LF/no-LF and bare/full-path inputs; these concerns are source-derived, not locally executed DEB failures. Parent-order clarification and pin-wording/host-test XML retention are nonblocking.

Reviewed HEAD:57f537b9ec9cedc797a19ffade867b3b285a3a9f. Full three-independent-general plus separate-SME source review and coordinator grounding. Only source/metadata and closed in-memory Python controls were executed; no Bazel/APT/compiler/native tests, real DEB creation or archive payload probe. Existing current-head hosted CI is external evidence. Report: https://github.com/yxieca/sonic-review-reports/pull/58. Check current source and replies before submitting; target feedback remains unsubmitted.
