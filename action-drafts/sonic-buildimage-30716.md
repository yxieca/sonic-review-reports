# Human-operated feedback drafts

Coordinator-only source assessment at bb9507f33c9f0b0bceeb7657a61847b679c8ed23. Required independent three-general-lens and SME coverage remains missing. No runtime/hardware validation was executed. Report: https://github.com/yxieca/sonic-review-reports/pull/21. Check the current head and existing replies before posting; this draft does not assert anyone else's approval.

## Questions

Could you address the fault-worker liveness and startup recovery issues in the existing threads? Stale heartbeat: https://github.com/sonic-net/sonic-buildimage/pull/30716#discussion_r4679066011. Setup-failed retained worker: https://github.com/sonic-net/sonic-buildimage/pull/30716#discussion_r4679066018. A per-select timeout does not bound a whole bank wait, and subsequent interrupts are queued to the same object even after run() exits on setup failure. The repeated shared-ELS fanout concern is nonblocking: https://github.com/sonic-net/sonic-buildimage/pull/30716#discussion_r4679066024. Please preserve bank-local faults and later relatches. This is a question without approval/formal verdict, not duplicate feedback.

Coordinator-only source assessment at bb9507f33c9f0b0bceeb7657a61847b679c8ed23. Required independent three-general-lens and SME coverage remains missing. No runtime/hardware validation was executed. Report: https://github.com/yxieca/sonic-review-reports/pull/21. Check the current head and existing replies before posting; this draft does not assert anyone else's approval.

## Request changes

Please fix the new fault-reporting liveness/recovery paths before source acceptance: bound or defer stale-bank freshness waits so another module's interrupts and idle reconciliation can progress (https://github.com/sonic-net/sonic-buildimage/pull/30716#discussion_r4679066011), and recover from setup failure without retaining a permanently dead consumer or losing queued faults (https://github.com/sonic-net/sonic-buildimage/pull/30716#discussion_r4679066018). Add matching stale-A/healthy-B and setup-failure/recovery controls. Shared-ELS duplicate fanout is a separate nonblocking diagnostic/efficiency follow-up, not an extra blocking condition. Parent30430 dependency/source gates and failed CI remain separate. This references existing feedback rather than reposting findings.

Coordinator-only source assessment at bb9507f33c9f0b0bceeb7657a61847b679c8ed23. Required independent three-general-lens and SME coverage remains missing. No runtime/hardware validation was executed. Report: https://github.com/yxieca/sonic-review-reports/pull/21. Check the current head and existing replies before posting; this draft does not assert anyone else's approval.
