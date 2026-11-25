> **Feedback already submitted — historical drafts.** Verified target CHANGES_REQUESTED review at `57f537b9ec9cedc797a19ffade867b3b285a3a9f`: https://github.com/sonic-net/sonic-build-infra/pull/7#pullrequestreview-6065748013. R1 remains the only P2 blocker; author explanation or fix is next. R2/R3 remain optional P3 input-contract hardening. Identical feedback has already been submitted; saved drafts below are historical and must not be reposted.

## Verified submitted feedback — retained receipt, do not repost

Please address the default APT updater's registry/version mismatch before landing.

**Must fix — default APT update cannot resolve its selected resolver (R1).**
`apt/lock.py` still defaults `RESOLVER_VERSION` to `0.9.4.sonic.20`. Its `resolve()` path creates a separate root MODULE, and this PR changes that root's default registry to the canonical SONiC registry followed by BCR. The documented command in `apt/README.md`:

`"$BOOTSTRAP_PYTHON" apt/lock.py update --bazel /path/to/bazel-8.5.1`

provides no version or registry override. At the reviewed registry snapshot, SONiC publishes `.26`, not `.20`, and BCR also lacks `.20`; the former registry does contain `.20`. Consequently this default maintenance command fails during dependency resolution before producing an updated lock. The normal root's `.26` and successful locked-build CI do not cover this separately generated updater root.

Please either publish the compatible `.20` recipe in the selected registry or deliberately migrate the updater default and lock-input provenance to an available resolver. Changing the constant alone needs care because `_inputs` records the resolver version/digest. Add a default-route regression without overrides masking the mismatch.

Source: https://github.com/sonic-net/sonic-build-infra/blob/57f537b9ec9cedc797a19ffade867b3b285a3a9f/apt/lock.py#L548-L593

**Optional follow-ups — not approval conditions:**
- Missing final newline (R2): `deb/mtree.py::summarize_mtree()` includes the final record via Python `splitlines()`, but the selected libarchive 3.7.4 mtree reader drops an unterminated final record. Reject or normalize it so checksums/control metadata cannot describe a file omitted from the archive.
- Ambiguous bare names (R3): a directory `a` followed by bare file `f` is summarized as root `f`, while libarchive's hierarchical interpretation emits `a/f`. Clarify/enforce explicit flat `./...` names or canonicalize once for both readers.

These mtree examples were accepted by the Python parser, but no supported production caller emitting them was established. They remain nonblocking input-contract hardening. Archive behavior was inspected in source, not reproduced by building a DEB. Preserve the streaming improvement and default TAR compatibility.

Supporting review and detailed evidence: https://github.com/yxieca/sonic-review-reports/pull/58
Reviewed target head: `57f537b9ec9cedc797a19ffade867b3b285a3a9f`.

## Earlier prepared drafts — historical

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
