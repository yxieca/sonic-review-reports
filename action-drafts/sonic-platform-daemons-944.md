# Feedback drafts for sonic-platform-daemons #944

Report: https://github.com/yxieca/sonic-review-reports/pull/55
Reviewed: `ee2b2fc2df0f9d5712bbbb95ad30e022b66942ff`

## Questions

Could you address or clarify these remaining distinct source concerns?

Two distinct source concerns remain for consideration:

Configuration-removal control: https://github.com/sonic-net/sonic-platform-daemons/blob/ee2b2fc2df0f9d5712bbbb95ad30e022b66942ff/crates/ycabled/src/daemon.rs#L245-L279 and https://github.com/sonic-net/sonic-platform-daemons/blob/ee2b2fc2df0f9d5712bbbb95ad30e022b66942ff/crates/ycabled/src/actor/mod.rs#L348-L393. Deleting MUX_CABLE without a transceiver event leaves an existing actor's cached cable type/driver able to handle a queued or later toggle. Please revalidate actionable/telemetry admission or deliver ordered invalidation; test deletion with unchanged TRANSCEIVER_INFO and require no later driver/RPC action.

Persistent-hang mailbox resource bound: https://github.com/sonic-net/sonic-platform-daemons/blob/ee2b2fc2df0f9d5712bbbb95ad30e022b66942ff/crates/ycabled/src/actor/mod.rs#L296-L331. Continuing probes/toggles accumulate in an unbounded queue while a handler's cable call never returns; backlog logging cannot run until receives resume. Please provide bounded ordered coalescing/reconciliation preserving lifecycle and latest command/state semantics, and verify held-port bounds alongside healthy-port progress. Do not restore silent dropping.

Replay-read recovery, firmware single-flight and queued CLI selector/argument mismatch are already raised in target discussions; avoid duplicate reposting. Credit fragmented SETTINGS, early transceiver ingress, notified-row error, restart-lifetime and startup SIGHUP corrections. Syslog and malformed-frame/mapping questions are nonblocking in this report.

Reviewed ee2b2fc2df0f9d5712bbbb95ad30e022b66942ff, source-only incremental review with prior unchanged full coverage. No native tests/builds or hardware/service validation executed. Report: https://github.com/yxieca/sonic-review-reports/pull/55. Check current head and replies before submission.

## Request changes

Please resolve these remaining distinct source concerns before accepting the implementation:

Two distinct source concerns remain for consideration:

Configuration-removal control: https://github.com/sonic-net/sonic-platform-daemons/blob/ee2b2fc2df0f9d5712bbbb95ad30e022b66942ff/crates/ycabled/src/daemon.rs#L245-L279 and https://github.com/sonic-net/sonic-platform-daemons/blob/ee2b2fc2df0f9d5712bbbb95ad30e022b66942ff/crates/ycabled/src/actor/mod.rs#L348-L393. Deleting MUX_CABLE without a transceiver event leaves an existing actor's cached cable type/driver able to handle a queued or later toggle. Please revalidate actionable/telemetry admission or deliver ordered invalidation; test deletion with unchanged TRANSCEIVER_INFO and require no later driver/RPC action.

Persistent-hang mailbox resource bound: https://github.com/sonic-net/sonic-platform-daemons/blob/ee2b2fc2df0f9d5712bbbb95ad30e022b66942ff/crates/ycabled/src/actor/mod.rs#L296-L331. Continuing probes/toggles accumulate in an unbounded queue while a handler's cable call never returns; backlog logging cannot run until receives resume. Please provide bounded ordered coalescing/reconciliation preserving lifecycle and latest command/state semantics, and verify held-port bounds alongside healthy-port progress. Do not restore silent dropping.

Replay-read recovery, firmware single-flight and queued CLI selector/argument mismatch are already raised in target discussions; avoid duplicate reposting. Credit fragmented SETTINGS, early transceiver ingress, notified-row error, restart-lifetime and startup SIGHUP corrections. Syslog and malformed-frame/mapping questions are nonblocking in this report.

Reviewed ee2b2fc2df0f9d5712bbbb95ad30e022b66942ff, source-only incremental review with prior unchanged full coverage. No native tests/builds or hardware/service validation executed. Report: https://github.com/yxieca/sonic-review-reports/pull/55. Check current head and replies before submission.
