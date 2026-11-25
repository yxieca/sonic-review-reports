# Self-contained reader drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/47

Reviewed target head: `aeb2f1ca6f02a5315f44a56ebb72d0c101a8bf8a`. Existing issue dispositions, coverage limits and target-feedback receipts remain unchanged. This presentation update submits no target feedback.



## Questions without verdict

Questions for correction or explanation; no formal verdict.

**R2 — failed backup read must not delete existing pmon configuration (P2).** `tests/transceiver/common/state_management.py:167–173` sees an existing `pmon_daemon_control.json` but returns `(None,error)` when reading it fails. `tests/transceiver/system/event_handling/test_low_power_mode.py:198–203` passes that value to `restore_pmon_daemon_control`; `state_management.py:241–260` interprets None as originally absent and removes the existing file. A transient/read-permission failure can therefore delete configuration before setup mutated it, with no captured backup to reconstruct it. Distinguish unavailable backup from genuine absence and do not perform destructive restoration after pre-mutation backup failure; preserve valid absent-file cleanup and controller-resident backups. This is distinct from the fixed reboot-cleared backup issue. Existing mandatory-argument, lane/timing and rotation/window concerns remain in their existing threads, not new duplicate feedback.

Source: https://github.com/sonic-net/sonic-mgmt/blob/aeb2f1ca6f02a5315f44a56ebb72d0c101a8bf8a/tests/transceiver/common/state_management.py#L167-L173

Reviewed target head: `aeb2f1ca6f02a5315f44a56ebb72d0c101a8bf8a`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/47.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Request changes with comment

Request-changes reader draft for the retained findings below.

**R2 — failed backup read must not delete existing pmon configuration (P2).** `tests/transceiver/common/state_management.py:167–173` sees an existing `pmon_daemon_control.json` but returns `(None,error)` when reading it fails. `tests/transceiver/system/event_handling/test_low_power_mode.py:198–203` passes that value to `restore_pmon_daemon_control`; `state_management.py:241–260` interprets None as originally absent and removes the existing file. A transient/read-permission failure can therefore delete configuration before setup mutated it, with no captured backup to reconstruct it. Distinguish unavailable backup from genuine absence and do not perform destructive restoration after pre-mutation backup failure; preserve valid absent-file cleanup and controller-resident backups. This is distinct from the fixed reboot-cleared backup issue. Existing mandatory-argument, lane/timing and rotation/window concerns remain in their existing threads, not new duplicate feedback.

Source: https://github.com/sonic-net/sonic-mgmt/blob/aeb2f1ca6f02a5315f44a56ebb72d0c101a8bf8a/tests/transceiver/common/state_management.py#L167-L173

Reviewed target head: `aeb2f1ca6f02a5315f44a56ebb72d0c101a8bf8a`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/47.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Prior draft history

The prior wording is preserved in the preceding report commit. This update expands author-facing explanations only; it does not change findings, severity, source coverage, target verdict or submission state.
