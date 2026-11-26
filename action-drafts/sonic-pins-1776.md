# Reader drafts: sonic-pins #1776

Report: REPORT_PR_URL

## Comment

Source review supports the migration and runtime design within the stated bounds; no blocking source defect established.

Optional failure-path cleanup — retain finalization after setup failure. In p4rt_app/scripts/p4rt_route_measurement_test.cc::main, failed SetUp returns1before TearDown. The former GoogleTest fixture always attempted TearDown even after failed setup. With cleanup=true and a session already created, a setup error can now omit the final best-effort ClearEntities attempt; this is not a demonstrated new device mutation or outage. If preserving that finalization contract, route exits through cleanup when a session exists or use a scope guard, retain the original failure status and report cleanup errors separately. This can follow in a separate PR; no device/fault-injection test was performed.

Known compiler/test scope is already discussed at https://github.com/sonic-net/sonic-pins/pull/1776#discussion_r4701679370 and https://github.com/sonic-net/sonic-pins/pull/1776#discussion_r4701771423. The temporary p4c selection and four manual freshness tests remain an author-deferred follow-up, not a new duplicated demand or a verified completed fix. Installed CLI tests use runfiles/ambient system libraries, so do not present them as fully isolated installed-image ABI or wire/hardware qualification.

Reviewed HEAD:a19f75089872524643c4a58eecbfe074458cd1fc, BASEe77250b8dcab96e6f0e6ba1a9643f66771caa46c. Designated three-general-plus-separate-SME source contributions complete through full semantic ranges plus verified include mapping/representative consumers; not four exhaustive191file-body passes. Current hosted236test targets and one runtime-package target passed externally, excluding four manual P4Info freshness checks. No reviewer compiler/Bazel/native/P4RT/SAI/DUT/network/install or payload probe. Report: REPORT_PR_URL. Verify current revision, CI and replies before submission.

## Approve

Source approval with a nonblocking cleanup follow-up that can be handled separately. Approval does not clear existing discussion state or certify installed images/hardware.

Optional failure-path cleanup — retain finalization after setup failure. In p4rt_app/scripts/p4rt_route_measurement_test.cc::main, failed SetUp returns1before TearDown. The former GoogleTest fixture always attempted TearDown even after failed setup. With cleanup=true and a session already created, a setup error can now omit the final best-effort ClearEntities attempt; this is not a demonstrated new device mutation or outage. If preserving that finalization contract, route exits through cleanup when a session exists or use a scope guard, retain the original failure status and report cleanup errors separately. This can follow in a separate PR; no device/fault-injection test was performed.

Known compiler/test scope is already discussed at https://github.com/sonic-net/sonic-pins/pull/1776#discussion_r4701679370 and https://github.com/sonic-net/sonic-pins/pull/1776#discussion_r4701771423. The temporary p4c selection and four manual freshness tests remain an author-deferred follow-up, not a new duplicated demand or a verified completed fix. Installed CLI tests use runfiles/ambient system libraries, so do not present them as fully isolated installed-image ABI or wire/hardware qualification.

Reviewed HEAD:a19f75089872524643c4a58eecbfe074458cd1fc, BASEe77250b8dcab96e6f0e6ba1a9643f66771caa46c. Designated three-general-plus-separate-SME source contributions complete through full semantic ranges plus verified include mapping/representative consumers; not four exhaustive191file-body passes. Current hosted236test targets and one runtime-package target passed externally, excluding four manual P4Info freshness checks. No reviewer compiler/Bazel/native/P4RT/SAI/DUT/network/install or payload probe. Report: REPORT_PR_URL. Verify current revision, CI and replies before submission.
