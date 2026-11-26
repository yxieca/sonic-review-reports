# Current reader drafts: build-infra #7

Report: https://github.com/yxieca/sonic-review-reports/pull/58

## Comment

Default APT update fix verified in source. apt/lock.py now selects published rules_distroless0.9.4.sonic.26 through main→resolve→resolve_partition’s separate generated MODULE, retaining canonical SONiC+BCR defaults. apt/apt.lock.json records matching resolver/input digest; all2,719package records,99collections and source definitions remain unchanged. The new AMD64 fixture invokes update/check without registry/resolver/pre-resolved-lock overrides and logs a successful single-package export. This closes the earlier R1 default-route mismatch; no new delta blocker was found. The previous change-request text is superseded, not repeated here.

Optional input-contract follow-ups remain nonblocking: deb/mtree.py::summarize_mtree counts an unterminated final record that libarchive3.7.4 can omit, and accepts bare flat names that the backend can interpret hierarchically. If those spellings are supported, reject or normalize them once so summary/conffiles and emitted payload agree; this update changes no such producer and does not revive them as approval conditions. Prior documentation/host-process XML notes are also optional.

Reviewed current HEAD:5bc1832245d8e6885adf7e44bef90d5ef81b2e16, BASE20725f7f7545909c09073ab7030928b0883a1bb7. Prior full panel at57f537b9 retained for unchanged bytes; new independent general and separate-SME delta source checks plus coordinator grounding. No reviewer APT/Bazel/native/build/DEB/payload execution. Current hosted single-package updater fixture succeeded externally; full production/empty-cache refresh remains author-reported. Report: https://github.com/yxieca/sonic-review-reports/pull/58. Check current revision, replies and effective review state before submission.

## Approve

Source review supports approval of this update.

Default APT update fix verified in source. apt/lock.py now selects published rules_distroless0.9.4.sonic.26 through main→resolve→resolve_partition’s separate generated MODULE, retaining canonical SONiC+BCR defaults. apt/apt.lock.json records matching resolver/input digest; all2,719package records,99collections and source definitions remain unchanged. The new AMD64 fixture invokes update/check without registry/resolver/pre-resolved-lock overrides and logs a successful single-package export. This closes the earlier R1 default-route mismatch; no new delta blocker was found. The previous change-request text is superseded, not repeated here.

Optional input-contract follow-ups remain nonblocking: deb/mtree.py::summarize_mtree counts an unterminated final record that libarchive3.7.4 can omit, and accepts bare flat names that the backend can interpret hierarchically. If those spellings are supported, reject or normalize them once so summary/conffiles and emitted payload agree; this update changes no such producer and does not revive them as approval conditions. Prior documentation/host-process XML notes are also optional.

Reviewed current HEAD:5bc1832245d8e6885adf7e44bef90d5ef81b2e16, BASE20725f7f7545909c09073ab7030928b0883a1bb7. Prior full panel at57f537b9 retained for unchanged bytes; new independent general and separate-SME delta source checks plus coordinator grounding. No reviewer APT/Bazel/native/build/DEB/payload execution. Current hosted single-package updater fixture succeeded externally; full production/empty-cache refresh remains author-reported. Report: https://github.com/yxieca/sonic-review-reports/pull/58. Check current revision, replies and effective review state before submission.
