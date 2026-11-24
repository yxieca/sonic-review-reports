# Human-operated feedback drafts

Coordinator-only source assessment at 97dd087f87423f1e31d5cd13c3ef371a620ccf4f. Required independent three-general-lens and SME coverage remains missing. No runtime/hardware validation was executed. Report: https://github.com/yxieca/sonic-review-reports/pull/20. Check the current head and existing replies before posting; this draft does not assert anyone else's approval.

## Questions

Could you address the current dependency and ELS lifecycle concerns in the existing threads, without duplicating their feedback? Dependency: https://github.com/sonic-net/sonic-buildimage/pull/30430#discussion_r4679060350. ELS deadline: https://github.com/sonic-net/sonic-buildimage/pull/30430#discussion_r4663246155 and https://github.com/sonic-net/sonic-buildimage/pull/30430#discussion_r4663319773. Mode-specific subscriptions: https://github.com/sonic-net/sonic-buildimage/pull/30430#discussion_r4679060340. The selected common source lacks cpo_cdb/firmware contracts; the ELS loop needs a preserved overall deadline and subscription reconciliation after control-mode changes. This is a question without approval or a formal verdict.

Coordinator-only source assessment at 97dd087f87423f1e31d5cd13c3ef371a620ccf4f. Required independent three-general-lens and SME coverage remains missing. No runtime/hardware validation was executed. Report: https://github.com/yxieca/sonic-review-reports/pull/20. Check the current head and existing replies before posting; this draft does not assert anyone else's approval.

## Request changes

Please fix the source/dependency incompatibility and new ELS event-source contract gaps described in the existing discussions before source acceptance: (1) select compatible common CDB lock/factory/firmware bytes rather than assuming an open dependency head is installed (https://github.com/sonic-net/sonic-buildimage/pull/30430#discussion_r4679060350); (2) preserve caller deadlines and a positive blocking slice for timeout0 (https://github.com/sonic-net/sonic-buildimage/pull/30430#discussion_r4663246155); (3) refresh the independent ELS subscriptions when control mode changes (https://github.com/sonic-net/sonic-buildimage/pull/30430#discussion_r4679060340). Add the matching regression cases and have the responsible owner verify the corrected Mellanox image/collection. This refers to existing feedback rather than adding duplicate findings. Unknown max-power handling remains a nonblocking recovery/diagnostic question; no unsafe power-on requirement is imposed. Other failing CI causes are not declared harmless.

Coordinator-only source assessment at 97dd087f87423f1e31d5cd13c3ef371a620ccf4f. Required independent three-general-lens and SME coverage remains missing. No runtime/hardware validation was executed. Report: https://github.com/yxieca/sonic-review-reports/pull/20. Check the current head and existing replies before posting; this draft does not assert anyone else's approval.
