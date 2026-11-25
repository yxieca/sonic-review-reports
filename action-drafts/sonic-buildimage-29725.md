# Human-operated feedback drafts

Coordinator-only source assessment at 8f306a0d2dcd8d369d4364caa0a4cc30c56be761. Required independent three-general-lens and SME coverage remains missing. No runtime/hardware validation was executed. Report: https://github.com/yxieca/sonic-review-reports/pull/22. Check the current head and existing replies before posting; this draft does not assert anyone else's approval.

## Questions

Could you address the standalone integration and mapping questions in the existing threads? ELS consumer/hook: https://github.com/sonic-net/sonic-buildimage/pull/29725#discussion_r4679058875. ASIC physical IDs: https://github.com/sonic-net/sonic-buildimage/pull/29725#discussion_r4679058893. JSON/INI alignment: https://github.com/sonic-net/sonic-buildimage/pull/29725#discussion_r4679058901. Selected dependency source and exact-head data show these concerns remain; downstreams rebasing later does not make this standalone head include their fixes. This is question-only, not an approval or duplicate review.

Coordinator-only source assessment at 8f306a0d2dcd8d369d4364caa0a4cc30c56be761. Required independent three-general-lens and SME coverage remains missing. No runtime/hardware validation was executed. Report: https://github.com/yxieca/sonic-review-reports/pull/22. Check the current head and existing replies before posting; this draft does not assert anyone else's approval.

## Request changes

Please reconcile the standalone source before acceptance: implement or safely gate the ELS event consumer/hook contract (https://github.com/sonic-net/sonic-buildimage/pull/29725#discussion_r4679058875); use physical IDs for correct SFP/ELS event delivery while retaining SDK IDs for hardware access (https://github.com/sonic-net/sonic-buildimage/pull/29725#discussion_r4679058893); align the shipped INI with the new JSON physical indices in both hardware/SimX variants (https://github.com/sonic-net/sonic-buildimage/pull/29725#discussion_r4679058901). Verify the corresponding mapping and lifecycle cases with the responsible test owner. Firmware/VDM full functionality is not an added blocking requirement for this link-only PR. This references existing feedback rather than posting duplicate findings.

Coordinator-only source assessment at 8f306a0d2dcd8d369d4364caa0a4cc30c56be761. Required independent three-general-lens and SME coverage remains missing. No runtime/hardware validation was executed. Report: https://github.com/yxieca/sonic-review-reports/pull/22. Check the current head and existing replies before posting; this draft does not assert anyone else's approval.
