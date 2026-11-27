# Feedback drafts for daemons #944

Report: https://github.com/yxieca/sonic-review-reports/pull/55
Revision: `8c34cb37da83f45f3108eeeac74e9f1af2d151e4`

## Questions

Could you address or clarify this newly identified validation-read gap and the carried source concerns?

Execution-time command revalidation must distinguish a DB error from a withdrawn request: https://github.com/sonic-net/sonic-platform-daemons/blob/8c34cb37da83f45f3108eeeac74e9f1af2d151e4/crates/ycabled/src/cli.rs#L188-L202 uses Db::get, while https://github.com/sonic-net/sonic-platform-daemons/blob/8c34cb37da83f45f3108eeeac74e9f1af2d151e4/crates/ycabled/src/db.rs#L626-L640 logs HGETALL errors and returns None. A valid command successfully delivered to its actor can be silently skipped if only its later validation read fails while pub/sub remains healthy; its row stays pending without a new notification or retry. Please use a fallible correctness-critical read, separating successfully observed absence/mismatch from failed observation, and retry in order or invoke the established recovery policy. Test successful initial delivery followed by failure of only the validation read.

Two unchanged source concerns also remain: configuration removal without TRANSCEIVER_INFO leaves cached actor classification able to process later hardware requests (daemon.rs existing-actor fast path and actor/mod.rs::handle_request); revalidate membership or invalidate the actor, requiring no later driver/RPC call after MUX_CABLE deletion. The actor's unbounded mailbox also accumulates continuing probes/toggles while a cable call never returns; provide bounded ordered reconciliation preserving lifecycle/latest state without restoring silent dropping.

In-flight CLI completion ownership and atomic telemetry publication are already raised in the current target discussions; address them there rather than duplicating feedback. Credit queued-command, single-flight download, replay-read, logging, index validation and lazy-platform fixes.

Reviewed source 8c34cb37da83f45f3108eeeac74e9f1af2d151e4; independent material changed-scope review plus verified unchanged coverage. No native tests/builds or hardware/service validation performed. Report: https://github.com/yxieca/sonic-review-reports/pull/55. Verify head/replies before use.

## Request changes

Please resolve the validation-read recovery gap and carried source concerns before accepting this implementation:

Execution-time command revalidation must distinguish a DB error from a withdrawn request: https://github.com/sonic-net/sonic-platform-daemons/blob/8c34cb37da83f45f3108eeeac74e9f1af2d151e4/crates/ycabled/src/cli.rs#L188-L202 uses Db::get, while https://github.com/sonic-net/sonic-platform-daemons/blob/8c34cb37da83f45f3108eeeac74e9f1af2d151e4/crates/ycabled/src/db.rs#L626-L640 logs HGETALL errors and returns None. A valid command successfully delivered to its actor can be silently skipped if only its later validation read fails while pub/sub remains healthy; its row stays pending without a new notification or retry. Please use a fallible correctness-critical read, separating successfully observed absence/mismatch from failed observation, and retry in order or invoke the established recovery policy. Test successful initial delivery followed by failure of only the validation read.

Two unchanged source concerns also remain: configuration removal without TRANSCEIVER_INFO leaves cached actor classification able to process later hardware requests (daemon.rs existing-actor fast path and actor/mod.rs::handle_request); revalidate membership or invalidate the actor, requiring no later driver/RPC call after MUX_CABLE deletion. The actor's unbounded mailbox also accumulates continuing probes/toggles while a cable call never returns; provide bounded ordered reconciliation preserving lifecycle/latest state without restoring silent dropping.

In-flight CLI completion ownership and atomic telemetry publication are already raised in the current target discussions; address them there rather than duplicating feedback. Credit queued-command, single-flight download, replay-read, logging, index validation and lazy-platform fixes.

Reviewed source 8c34cb37da83f45f3108eeeac74e9f1af2d151e4; independent material changed-scope review plus verified unchanged coverage. No native tests/builds or hardware/service validation performed. Report: https://github.com/yxieca/sonic-review-reports/pull/55. Verify head/replies before use.
