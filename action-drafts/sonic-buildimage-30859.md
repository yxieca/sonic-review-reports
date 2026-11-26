<!-- source-followup-7183073461 -->

**HISTORICAL DRAFTS — DO NOT SUBMIT UNTIL CURRENT FOLLOW-UP IS VERIFIED.**

**Needs Report Update — current source acceptance and submission drafts held.** At unchanged target `7d9e0caac5be00833b484fa69e41d1873a83f89a`, the author explains that BMC initialization currently fails before most publication writes, and identifies the component-data consumer and possible BMC-specific initializer scope. These material source/consumer claims require independent reconciliation before updating the recommendation; the explanation is not treated as proven merely by being posted. Original findings and prior feedback remain historical evidence. Current coverage is incomplete for this follow-up, not a new confirmed code blocker.

# Self-contained reader drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/30

Reviewed target head: `7d9e0caac5be00833b484fa69e41d1873a83f89a`. Existing issue dispositions, coverage limits and target-feedback receipts remain unchanged. This presentation update submits no target feedback.



## Questions — metadata consequences

Questions for correction or explanation; no formal verdict.

**R1 — account for required BMC publications omitted by the whole-service mask (before-approval scope clarification).** `files/build_scripts/aspeed_bmc_filter_services.py` masks switch-platform-init.service. The selected `scripts/switch_platform_init.py` main also publishes CHASSIS_INFO image/build metadata, SW_COMP_INFO software/kernel information, syslog-server state and SWITCH_PLATFORM_INIT readiness. If a BMC consumer requires those rows/state and no other producer supplies them, masking removes the data/readiness it relies on; which concrete consumers and replacement producers apply? Preserve any required publications through a BMC-compatible initializer or split incompatible CPU/DMI operations instead of disabling all responsibilities. The separate ASPEED platform-init installs wheels/symlink and does not establish equivalent metadata publication. The boot-failure/masking rationale is credited. No supported consumer failure, universal telemetry break or live boot regression was established; this remains a scope/compensation question, not a manufactured runtime blocker.

Source: https://github.com/sonic-net/sonic-buildimage/blob/7d9e0caac5be00833b484fa69e41d1873a83f89a/files/build_scripts/aspeed_bmc_filter_services.py#L22-L35
Selected initializer: https://github.com/sonic-net/sonic-host-services/blob/7f82db29696ff4d6967a5067b92444da737f2bb8/scripts/switch_platform_init.py

Reviewed target head: `7d9e0caac5be00833b484fa69e41d1873a83f89a`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/30.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Request changes — clarify R1

Request-changes reader draft for the retained findings below.

**R1 — account for required BMC publications omitted by the whole-service mask (before-approval scope clarification).** `files/build_scripts/aspeed_bmc_filter_services.py` masks switch-platform-init.service. The selected `scripts/switch_platform_init.py` main also publishes CHASSIS_INFO image/build metadata, SW_COMP_INFO software/kernel information, syslog-server state and SWITCH_PLATFORM_INIT readiness. If a BMC consumer requires those rows/state and no other producer supplies them, masking removes the data/readiness it relies on; which concrete consumers and replacement producers apply? Preserve any required publications through a BMC-compatible initializer or split incompatible CPU/DMI operations instead of disabling all responsibilities. The separate ASPEED platform-init installs wheels/symlink and does not establish equivalent metadata publication. The boot-failure/masking rationale is credited. No supported consumer failure, universal telemetry break or live boot regression was established; this remains a scope/compensation question, not a manufactured runtime blocker.

Source: https://github.com/sonic-net/sonic-buildimage/blob/7d9e0caac5be00833b484fa69e41d1873a83f89a/files/build_scripts/aspeed_bmc_filter_services.py#L22-L35
Selected initializer: https://github.com/sonic-net/sonic-host-services/blob/7f82db29696ff4d6967a5067b92444da737f2bb8/scripts/switch_platform_init.py

Reviewed target head: `7d9e0caac5be00833b484fa69e41d1873a83f89a`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/30.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Prior draft history

The prior wording is preserved in the preceding report commit. This update expands author-facing explanations only; it does not change findings, severity, source coverage, target verdict or submission state.
