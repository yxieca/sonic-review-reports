# Human-operated feedback drafts

Coordinator-only source assessment at 7b1dccafb8498ee3c30b200e623219d364859aad. Required independent three-general-lens and SME coverage remains missing. No runtime/hardware validation was executed. Report: https://github.com/yxieca/sonic-review-reports/pull/23. Check the current head and existing replies before posting; this draft does not assert anyone else's approval.

## Questions

Could you fix the generator-close cancellation path described in https://github.com/sonic-net/sonic-platform-common/pull/790#discussion_r4679063893? wait_for_cdb_status returns [False,status] for busy timeout/unreadable status, but _abort_download ignores it before dispatching Abort. Please cover that result and an idle control. Separately clarify authoritative live versus mirrored temperature flags in https://github.com/sonic-net/sonic-platform-common/pull/790#discussion_r4679063884; this report does not assume which hardware register is authoritative. Question only, no approval/verdict or duplicate findings.

Coordinator-only source assessment at 7b1dccafb8498ee3c30b200e623219d364859aad. Required independent three-general-lens and SME coverage remains missing. No runtime/hardware validation was executed. Report: https://github.com/yxieca/sonic-review-reports/pull/23. Check the current head and existing replies before posting; this draft does not assert anyone else's approval.

## Request changes

Please ensure the new firmware-mixin cancellation sends Abort only after verified CDB idle/completion, reports cancellation that could not complete, and preserves the original interruption. Existing thread: https://github.com/sonic-net/sonic-platform-common/pull/790#discussion_r4679063893. Add busy-timeout/unreadable and idle-success generator-close controls. The live/mirror temperature register question and broad lookup-catch diagnostics remain separately qualified nonblocking items. Azure failure cause still needs owner verification; merged prerequisites do not establish a tested containing image. This references existing feedback rather than reposting it.

Coordinator-only source assessment at 7b1dccafb8498ee3c30b200e623219d364859aad. Required independent three-general-lens and SME coverage remains missing. No runtime/hardware validation was executed. Report: https://github.com/yxieca/sonic-review-reports/pull/23. Check the current head and existing replies before posting; this draft does not assert anyone else's approval.
