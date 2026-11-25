> **Feedback already submitted:** https://github.com/sonic-net/sonic-buildimage/pull/30859#pullrequestreview-6063810197. These retained drafts are historical feedback; do not repost identical text. Awaiting author response.

# Current feedback drafts — R1 clarification required

Report: https://github.com/yxieca/sonic-review-reports/pull/30
Reviewed head: `7d9e0caac5be00833b484fa69e41d1873a83f89a`

The earlier Comment/Approve drafts are superseded and retained in commit history. No approval draft is currently offered. These are editable, human-operated drafts; nothing is submitted automatically.

## Questions

Could you clarify the consequences of masking the entire switch-platform-init.service on BMC images? Its executed main path also publishes image/build metadata in CHASSIS_INFO, software/kernel information in SW_COMP_INFO, syslog-server state and SWITCH_PLATFORM_INIT readiness. Which of these outputs are required by BMC consumers, and what existing producer compensates for their omission?

The DMI/CPU-port assumptions explain why this initializer cannot run unchanged, but do not establish that all its outputs are unnecessary. The separate ASPEED sonic-platform-init service installs wheels and the platform symlink; it does not publish equivalent metadata. If required outputs lack replacements, could the shared responsibilities be preserved through a BMC-compatible path?

R1 and source details: https://github.com/yxieca/sonic-review-reports/pull/30. Reviewed target head: 7d9e0caac5be00833b484fa69e41d1873a83f89a. This is a scope/coverage question, not a claim that every BMC telemetry path is broken. No live boot or device validation was performed.

## Request changes

Please clarify and account for the BMC-relevant publications lost by masking the entire switch-platform-init.service before landing this change (R1).

Its main path publishes CHASSIS_INFO image/build metadata, SW_COMP_INFO software/kernel information, syslog-server state and SWITCH_PLATFORM_INIT readiness as well as hardware-specific operations. Please identify required BMC consumers, the consequence of omission, and the actual replacement producers. If needed outputs have no compensation, preserve them through a BMC-compatible initializer or split unsupported portions instead of disabling all responsibilities.

The separate ASPEED platform-init service is not evidence of equivalent metadata publication. The masking implementation and boot-failure rationale are acknowledged; the earlier source approval recommendation is withdrawn pending this scope clarification. No universal telemetry failure or live hardware regression is asserted.

Review report: https://github.com/yxieca/sonic-review-reports/pull/30. Reviewed target head: 7d9e0caac5be00833b484fa69e41d1873a83f89a. AI-assisted report; this submission reflects the submitting reviewer's own judgment.
