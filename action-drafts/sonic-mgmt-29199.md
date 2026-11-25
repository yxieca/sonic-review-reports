# Reader drafts: sonic-mgmt #29199

Current reviewed HEAD: `8fd84017fc27f07c22e99346a2b794ba76dface2`. These drafts require current reader confirmation; historical decision text must not be replayed. No automatic submission.

## Questions without verdict

Could R1/R2 in the audit module be addressed? R1: AuditLog.mark() still waits for global silence without a deadline and runs before owned-subscription DELETE. Could cursor acquisition be bounded and cleanup attempted even when it fails? R2: the first no-read assertion runs before establishing INFO; an initially DEBUG configuration correctly audits the GET. Could INFO be established before that assertion while preserving original-level restoration? Nonblocking N6: could the no-subscriber case require zero or skip clearly without removing unrelated subscriptions? The prior readiness, command publication and event-filter fixes and latest analyzer clarifications are credited. Redfish41 has merged; the existing formal review remains separate.

Reviewed revision `8fd84017fc27f07c22e99346a2b794ba76dface2`. Report: https://github.com/yxieca/sonic-review-reports/pull/26. Retained full source panel on verified unchanged scope plus bounded independent correction crosscheck and coordinator grounding. No new native/live tests; historical evidence is not current-head execution. Check freshness and existing discussion before submission.

## Comment without verdict

The current bounded correction review credits the analyzer clarifications and earlier readiness/publication/event fixes. R1/R2 remain test-correctness concerns: bound AuditLog.mark() and ensure it cannot prevent owned-subscription deletion; establish INFO before the first negative read assertion, then test DEBUG→INFO and restore the original level. The zero-subscriber precondition is a nonblocking scenario improvement. Redfish41 has merged, satisfying the named ordering prerequisite only; existing external review and installed-image/release applicability remain separate. No new live validation is claimed.

Reviewed revision `8fd84017fc27f07c22e99346a2b794ba76dface2`. Report: https://github.com/yxieca/sonic-review-reports/pull/26. Retained full source panel on verified unchanged scope plus bounded independent correction crosscheck and coordinator grounding. No new native/live tests; historical evidence is not current-head execution. Check freshness and existing discussion before submission.

## Request changes with comment

Please address retained audit-test R1/R2 before source acceptance: bound AuditLog.mark() and always attempt deletion of the test-owned subscription when marking fails; establish/wait for INFO before the first no-read assertion, then verify DEBUG→INFO and restore the original configuration. These are lifecycle/false-failure defects, not historical CodeQL secret/finally allegations. N6 zero-subscriber isolation and N5 conditional command cleanup remain nonblocking. Prior fixes and analyzer clarifications are credited. Redfish41 has merged; existing external review and image/release evidence remain separate.

Reviewed revision `8fd84017fc27f07c22e99346a2b794ba76dface2`. Report: https://github.com/yxieca/sonic-review-reports/pull/26. Retained full source panel on verified unchanged scope plus bounded independent correction crosscheck and coordinator grounding. No new native/live tests; historical evidence is not current-head execution. Check freshness and existing discussion before submission.