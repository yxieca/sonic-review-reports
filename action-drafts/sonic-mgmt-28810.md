# Feedback drafts: sonic-mgmt #28810

Report: https://github.com/yxieca/sonic-review-reports/pull/4

No blockers. S1 is optional and already suggested in the target discussion; avoid duplicate posting. These drafts do not override Ying’s separate approval hold.

## Comment without approval

No blocking issues found in the reviewed change. Using continue keeps processing later test items while the function-scoped ASIC fixture reads each current item’s own marker.

AI-assisted review report: https://github.com/yxieca/sonic-review-reports/pull/4. This submission reflects my own review and decision.

## Approve with comment

No blocking issues found in the reviewed change. Using continue keeps processing later test items while the function-scoped ASIC fixture reads each current item’s own marker.

AI-assisted review report: https://github.com/yxieca/sonic-review-reports/pull/4. This submission reflects my own review and decision.

## Historical validation evidence update — not a new submission

The author reports a VS KVM run at the unchanged reviewed head: 23 tests collected and 23 skipped, exit 0, with 22 warnings. All 8 VXLAN and 5 ACL cases skipped as Unsupported platform; 10 ECMP cases used their separate Broadcom check. The author discloses a dirty testbed/configuration checkout and modified platform conftest, while reporting the changed collection plugin itself unmodified. This supports reported later-case skip behavior, not independent device execution or full 23-item fixture-guard instrumentation; the latter was not measured in this run. No source verdict changes: source approval and optional S1 regression-coverage follow-up remain. Existing target feedback is not duplicated. [Author evidence](https://github.com/sonic-net/sonic-mgmt/pull/28810#issuecomment-7188336707).
