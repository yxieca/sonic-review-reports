# Human-operated drafts for sonic-platform-daemons #944

Report: https://github.com/yxieca/sonic-review-reports/pull/55
Reviewed revision: `2401414a5f4e27a2ee62b2e2c2b656e3d8c24980`

## Questions without verdict

Could you address or clarify these three distinct source-contract concerns?

1. Configuration-removal control revocation — https://github.com/sonic-net/sonic-platform-daemons/blob/2401414a5f4e27a2ee62b2e2c2b656e3d8c24980/crates/ycabled/src/daemon.rs#L245-L271 and https://github.com/sonic-net/sonic-platform-daemons/blob/2401414a5f4e27a2ee62b2e2c2b656e3d8c24980/crates/ycabled/src/actor/mod.rs#L348-L393: deleting CONFIG_DB MUX_CABLE without a transceiver event leaves an existing actor's cached cable classification/driver active. A queued or later toggle still performs the vendor operation. Revalidate actionable/telemetry admission or deliver ordered actor invalidation; test configuration removal with unchanged TRANSCEIVER_INFO and require no subsequent driver/RPC call.

2. Persistent-hang mailbox bound — https://github.com/sonic-net/sonic-platform-daemons/blob/2401414a5f4e27a2ee62b2e2c2b656e3d8c24980/crates/ycabled/src/actor/mod.rs#L296-L331: unbounded mailboxes keep retaining continuing probe/toggle messages while a handler's cable call never returns; backlog warnings cannot run until the actor receives again. Please implement bounded ordered coalescing/reconciliation preserving lifecycle events and latest command/state semantics, and test held-port resource bounds alongside healthy-port progress. Do not restore silent event dropping or restart every healthy port merely to empty one queue.

3. Firmware download single-flight — https://github.com/sonic-net/sonic-platform-daemons/blob/2401414a5f4e27a2ee62b2e2c2b656e3d8c24980/crates/ycabled/src/cli.rs#L582-L663: every accepted download spawns detached work, and releasing the bridge's admission slot after 10 ms does not release a held blocking driver call. Repeated downloads on one port can exceed the documented per-port worker bound. Reserve one actual in-flight download per port before spawning, retain that reservation until the call returns across cable changes, and reject duplicates with the documented error response; keep normal requests available during the download.

The transport-fragment, first-request bootstrap, startup removal, unread notification and early-restart concerns are already present in the current target discussion. Please reconcile them there rather than posting duplicate comments. TCP/TLS deadline and the original replay-before-actor fixes are credited; the remaining incomplete-frame boundary is not a repeat of the old TCP-before-TLS claim.

Reviewed source `2401414a5f4e27a2ee62b2e2c2b656e3d8c24980`. These are conditional static source findings, not locally reproduced hardware outages or newly executed test failures. No native tests/builds, dependency installation, hardware/service operations or CI actions were performed. Report: https://github.com/yxieca/sonic-review-reports/pull/55. Verify the current head and author replies before using this draft.

## Request changes with comment

Please resolve these three distinct source-contract concerns before accepting the new implementation:

1. Configuration-removal control revocation — https://github.com/sonic-net/sonic-platform-daemons/blob/2401414a5f4e27a2ee62b2e2c2b656e3d8c24980/crates/ycabled/src/daemon.rs#L245-L271 and https://github.com/sonic-net/sonic-platform-daemons/blob/2401414a5f4e27a2ee62b2e2c2b656e3d8c24980/crates/ycabled/src/actor/mod.rs#L348-L393: deleting CONFIG_DB MUX_CABLE without a transceiver event leaves an existing actor's cached cable classification/driver active. A queued or later toggle still performs the vendor operation. Revalidate actionable/telemetry admission or deliver ordered actor invalidation; test configuration removal with unchanged TRANSCEIVER_INFO and require no subsequent driver/RPC call.

2. Persistent-hang mailbox bound — https://github.com/sonic-net/sonic-platform-daemons/blob/2401414a5f4e27a2ee62b2e2c2b656e3d8c24980/crates/ycabled/src/actor/mod.rs#L296-L331: unbounded mailboxes keep retaining continuing probe/toggle messages while a handler's cable call never returns; backlog warnings cannot run until the actor receives again. Please implement bounded ordered coalescing/reconciliation preserving lifecycle events and latest command/state semantics, and test held-port resource bounds alongside healthy-port progress. Do not restore silent event dropping or restart every healthy port merely to empty one queue.

3. Firmware download single-flight — https://github.com/sonic-net/sonic-platform-daemons/blob/2401414a5f4e27a2ee62b2e2c2b656e3d8c24980/crates/ycabled/src/cli.rs#L582-L663: every accepted download spawns detached work, and releasing the bridge's admission slot after 10 ms does not release a held blocking driver call. Repeated downloads on one port can exceed the documented per-port worker bound. Reserve one actual in-flight download per port before spawning, retain that reservation until the call returns across cable changes, and reject duplicates with the documented error response; keep normal requests available during the download.

The transport-fragment, first-request bootstrap, startup removal, unread notification and early-restart concerns are already present in the current target discussion. Please reconcile them there rather than posting duplicate comments. TCP/TLS deadline and the original replay-before-actor fixes are credited; the remaining incomplete-frame boundary is not a repeat of the old TCP-before-TLS claim.

Nonblocking: synchronous syslog backpressure and startup SIGHUP handling can be followed up separately.

Reviewed source `2401414a5f4e27a2ee62b2e2c2b656e3d8c24980`. These are conditional static source findings, not locally reproduced hardware outages or newly executed test failures. No native tests/builds, dependency installation, hardware/service operations or CI actions were performed. Report: https://github.com/yxieca/sonic-review-reports/pull/55. Verify the current head and author replies before using this draft.
