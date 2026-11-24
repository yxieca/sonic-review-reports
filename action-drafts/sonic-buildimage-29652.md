# Editable target feedback drafts

Report PR: https://github.com/yxieca/sonic-review-reports/pull/7
Target: https://github.com/sonic-net/sonic-buildimage/pull/29652
Reviewed head: `506526151f1bd020a508112ad2af463996198a3a`

## comment

```text
AI-assisted review report: https://github.com/yxieca/sonic-review-reports/pull/7

Source acceptable; no new demonstrated code blocker. Historical review: target MERGED at 2026-11-21T06:17:51Z; no additional target verdict is applicable.

— what changed since the saved442ba370 review
- `ENABLE_BMC_ZTP ?= n` selects the shipped admin-mode; aspeed package inclusion separately uses `ENABLE_ZTP ?= y`, now allowing environment as well as command-line override.
- Installer emits the aspeed-specific JSON template inline, with admin-mode false unless explicitly y and feat-inband false. No unit-disable step remains; shared `ztp_is_enabled` is restored to the existing CLI-status check.
- `config-setup::seed_ztp_cfg` runs before the first CLI use, copies absent state or adds missing keys while preserving existing operator settings.
- Supported opt-in is now explicitly `ztp enable` followed by `ztp run -y`, which deliberately renames startup config before discovery. Unit enablement survives reboot. Current exact sonic-ztp gitlink is `0ac9b0b6adc3c949c7a2b1fa3b794f6002552544`, not the old036c8eaa source.
- Unnecessary cached-RFS flag entry is removed; the waiver correctly describes final-installer consumption. Baseline matches current slave.mk blobc16ef406.

Reviewed target revision: 506526151f1bd020a508112ad2af463996198a3a. Retained source review and bounded validation were reused, not rerun. No independent hardware qualification is claimed.

The target is already terminal; this is a historical draft for report inspection, not a new approval request.

Any submission reflects the reader’s own review and judgment; this comment is not an approval.
```

## approve

```text
AI-assisted review report: https://github.com/yxieca/sonic-review-reports/pull/7

Source acceptable; no new demonstrated code blocker. Historical review: target MERGED at 2026-11-21T06:17:51Z; no additional target verdict is applicable.

— what changed since the saved442ba370 review
- `ENABLE_BMC_ZTP ?= n` selects the shipped admin-mode; aspeed package inclusion separately uses `ENABLE_ZTP ?= y`, now allowing environment as well as command-line override.
- Installer emits the aspeed-specific JSON template inline, with admin-mode false unless explicitly y and feat-inband false. No unit-disable step remains; shared `ztp_is_enabled` is restored to the existing CLI-status check.
- `config-setup::seed_ztp_cfg` runs before the first CLI use, copies absent state or adds missing keys while preserving existing operator settings.
- Supported opt-in is now explicitly `ztp enable` followed by `ztp run -y`, which deliberately renames startup config before discovery. Unit enablement survives reboot. Current exact sonic-ztp gitlink is `0ac9b0b6adc3c949c7a2b1fa3b794f6002552544`, not the old036c8eaa source.
- Unnecessary cached-RFS flag entry is removed; the waiver correctly describes final-installer consumption. Baseline matches current slave.mk blobc16ef406.

Reviewed target revision: 506526151f1bd020a508112ad2af463996198a3a. Retained source review and bounded validation were reused, not rerun. No independent hardware qualification is claimed.

The target is already terminal; this is a historical draft for report inspection, not a new approval request.

Any approval must reflect the submitting reviewer’s own judgment and permissions; this saved draft is not a claim that anyone has approved it.
```
