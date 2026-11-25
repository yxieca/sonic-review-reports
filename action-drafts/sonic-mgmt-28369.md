# Current reader drafts — integration follow-up2026-11-25

REVISE; R1P2. Existing approval preserved, old approval drafts superseded. These drafts are human-operated only and no target action is authorized by report publication. Avoid duplicate feedback.

## Questions without verdict

AI-assisted review report: https://github.com/yxieca/sonic-review-reports/pull/15

Reviewed target head: f445237b36b18c0db54d4cd669399f3dbcb4281d; integration cutoff: 42205428fbe07ed1d12ea4e8b0eb654b78891726, including module recovery72b557630cbd5ae737c8135ec09b12a56ca32fa4.

R1 (P2): `_restore_config` is shared by per-case cleanup and the later module recovery. Adding raw `config reload -y` there makes a raw-reload failure raise before the module's following checked `config_reload` is attempted, even after the saved file was restored. That module failure propagates as a teardown error; the concern is loss of the checked recovery attempt, not a claim of silently green module teardown. Successful paths also gain per-case and extra module reloads.

Could recovery remain file-only in this helper with the existing one module-scoped checked reload, or could you explain how the checked recovery is reached after raw reload failure? The existing external discussion raises this same concern; do not duplicate it without a useful reason. The earlier approval receipt is preserved and predates this integration follow-up.

Source-only independent integration review; no exact merged-tree physical validation, tests or image-specific CLI behavior reproduced. Check latest target/upstream context before submission.

## Request changes

AI-assisted review report: https://github.com/yxieca/sonic-review-reports/pull/15

Reviewed target head: f445237b36b18c0db54d4cd669399f3dbcb4281d; integration cutoff: 42205428fbe07ed1d12ea4e8b0eb654b78891726, including module recovery72b557630cbd5ae737c8135ec09b12a56ca32fa4.

Changes requested for the inspected integration context. R1 (P2): `_restore_config` is shared by per-case cleanup and the later module recovery. Adding raw `config reload -y` there makes a raw-reload failure raise before the module's following checked `config_reload` is attempted, even after the saved file was restored. That module failure propagates as a teardown error; the concern is loss of the checked recovery attempt, not a claim of silently green module teardown. Successful paths also gain per-case and extra module reloads.

Please retain file-only restoration and the existing one module-scoped checked reload, or explain the intended lifecycle. The existing external discussion raises this same concern; do not duplicate it without a useful reason. The earlier approval receipt is preserved and predates this integration follow-up.

Source-only independent integration review; no exact merged-tree physical validation, tests or image-specific CLI behavior reproduced. Check latest target/upstream context before submission.
