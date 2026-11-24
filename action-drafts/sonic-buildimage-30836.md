# Editable target feedback drafts

Report PR: REPORT_PR_PENDING
Target: https://github.com/sonic-net/sonic-buildimage/pull/30836
Reviewed head: `f2eda294feb033481e70462466cd5913f154b6cb`

## comment

```text
AI-assisted review report: REPORT_PR_PENDING

Source acceptable; no new demonstrated code blocker. Historical review: target MERGED at 2026-11-21T06:18:58Z; no additional target verdict is applicable.

The operator helper installs server certificate/key/CA at `/etc/sonic/credentials/{restapiserver.crt,restapiserver.key,restapica.crt}` and, with `--push-config`, writes those same paths to REDFISH|certs. CN-only generation becomes supported; both CSR and signing-extension producers already conditionally emit IP SANs and retain DNS SANs. Post-install requests use a SAN hostname with a separate transport destination rather than disabling TLS verification.

Reviewed target revision: f2eda294feb033481e70462466cd5913f154b6cb. Retained source review and bounded validation were reused, not rerun. No independent hardware qualification is claimed.

The target is already terminal; this is a historical draft for report inspection, not a new approval request.

N1: distinguish installed credential files from CONFIG_DB activation in the no-push message; this is inherited wording, not a new installation defect.

Any submission reflects the reader’s own review and judgment; this comment is not an approval.
```

## approve

```text
AI-assisted review report: REPORT_PR_PENDING

Source acceptable; no new demonstrated code blocker. Historical review: target MERGED at 2026-11-21T06:18:58Z; no additional target verdict is applicable.

The operator helper installs server certificate/key/CA at `/etc/sonic/credentials/{restapiserver.crt,restapiserver.key,restapica.crt}` and, with `--push-config`, writes those same paths to REDFISH|certs. CN-only generation becomes supported; both CSR and signing-extension producers already conditionally emit IP SANs and retain DNS SANs. Post-install requests use a SAN hostname with a separate transport destination rather than disabling TLS verification.

Reviewed target revision: f2eda294feb033481e70462466cd5913f154b6cb. Retained source review and bounded validation were reused, not rerun. No independent hardware qualification is claimed.

The target is already terminal; this is a historical draft for report inspection, not a new approval request.

N1: distinguish installed credential files from CONFIG_DB activation in the no-push message; this is inherited wording, not a new installation defect.

Any approval must reflect the submitting reviewer’s own judgment and permissions; this saved draft is not a claim that anyone has approved it.
```
