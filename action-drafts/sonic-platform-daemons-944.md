# Feedback drafts for daemons #944

Report: https://github.com/yxieca/sonic-review-reports/pull/55
Revision: `570200a7ba4b5063db8a827f464e4275de948294`

## Questions

Could you address or clarify the distinct ownership-read recovery gap and carried source concerns?

Ownership-read recovery: https://github.com/sonic-net/sonic-platform-daemons/blob/570200a7ba4b5063db8a827f464e4275de948294/crates/ycabled/src/cli.rs#L1333-L1369 and https://github.com/sonic-net/sonic-platform-daemons/blob/570200a7ba4b5063db8a827f464e4275de948294/crates/ycabled/src/db.rs#L643-L656. Current-command/result/response checks use a DB read that logs HGETALL failures and returns None. A valid delivered or executed command can therefore be treated as withdrawn after an isolated read failure, with no completion retry or new notification; a result check can fail while a later response succeeds. Please use fallible ownership reads and distinguish failed observation from real absence/mismatch. Preserve already-completed hardware work for bounded publication retry or explicit recovery rather than blindly rerunning non-idempotent effects. Add controls failing only a later validation read after successful delivery.

Carried configuration-removal and mailbox concerns remain: cached actor classification still allows later hardware operations after MUX_CABLE deletion without a transceiver event, and a persistently held port can accumulate unlimited queued probes/toggles. Please revalidate membership/deliver ordered invalidation and provide bounded ordered mailbox reconciliation preserving lifecycle/latest state; verify no later driver/RPC action after configuration deletion and healthy-port progress under held-port load.

Command/argument acquisition/publication ownership and failed response writes followed by command consumption are already raised in target discussion; address them there rather than duplicating feedback. Credit the telemetry publication lock, shared namespace limits, captured arguments and conditional command-row consumption, while checking the remaining boundaries.

Reviewed 570200a7ba4b5063db8a827f464e4275de948294; source-only material review plus verified unchanged full coverage. No native tests/builds or hardware/service validation performed. Report: https://github.com/yxieca/sonic-review-reports/pull/55. Check current head/replies before submission.

## Request changes

Please resolve the ownership-read recovery gap and carried source concerns before accepting this implementation:

Ownership-read recovery: https://github.com/sonic-net/sonic-platform-daemons/blob/570200a7ba4b5063db8a827f464e4275de948294/crates/ycabled/src/cli.rs#L1333-L1369 and https://github.com/sonic-net/sonic-platform-daemons/blob/570200a7ba4b5063db8a827f464e4275de948294/crates/ycabled/src/db.rs#L643-L656. Current-command/result/response checks use a DB read that logs HGETALL failures and returns None. A valid delivered or executed command can therefore be treated as withdrawn after an isolated read failure, with no completion retry or new notification; a result check can fail while a later response succeeds. Please use fallible ownership reads and distinguish failed observation from real absence/mismatch. Preserve already-completed hardware work for bounded publication retry or explicit recovery rather than blindly rerunning non-idempotent effects. Add controls failing only a later validation read after successful delivery.

Carried configuration-removal and mailbox concerns remain: cached actor classification still allows later hardware operations after MUX_CABLE deletion without a transceiver event, and a persistently held port can accumulate unlimited queued probes/toggles. Please revalidate membership/deliver ordered invalidation and provide bounded ordered mailbox reconciliation preserving lifecycle/latest state; verify no later driver/RPC action after configuration deletion and healthy-port progress under held-port load.

Command/argument acquisition/publication ownership and failed response writes followed by command consumption are already raised in target discussion; address them there rather than duplicating feedback. Credit the telemetry publication lock, shared namespace limits, captured arguments and conditional command-row consumption, while checking the remaining boundaries.

Reviewed 570200a7ba4b5063db8a827f464e4275de948294; source-only material review plus verified unchanged full coverage. No native tests/builds or hardware/service validation performed. Report: https://github.com/yxieca/sonic-review-reports/pull/55. Check current head/replies before submission.
