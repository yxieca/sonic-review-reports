# Reader drafts: sonic-dbsyncd #101

Report: REPORT_PR_URL

## Comment

The additive owner-wheel/runtime source is acceptable within the reviewed scope; no introduced production blocker was found.

Nonblocking packaging fidelity — preserve supported Maintainer metadata. In BUILD.bazel::sonic_dbsyncd_wheel, maintainer and maintainer_email are omitted. tests/bazel/installed_wheel_probe.py::test_complete_owner_payload_and_metadata requires their absence and README.md says the wheel API cannot represent them. However the selected rules_python1.9.0.sonic.2 patch0003 explicitly adds both attributes and emits/tests those METADATA fields. The new wheel therefore loses fields present in setup.py for a tooling limitation that does not apply. Please pass the existing setup-contract fields to the wheel rule and compare them in the installed-wheel test, removing the unsupported-fields exception/documentation; alternatively state an intentional omission policy accurately. This does not affect normal LLDP operation and can follow separately.

Nonblocking test cleanup — retain Redis ownership across outer probe timeout. In tests/bazel/installed_wheel_probe.py::test_native_redis_sync_without_owner_source_or_original_mocks, subprocess.run(... timeout=60) can kill the native probe process after it starts redis-server. The Redis process is cleaned only by tests/bazel/native_redis_probe.py::main finally in that killed child, so a stall can leave the grandchild until Bazel/container teardown. Please use a surviving-parent owner or a dedicated process group/session with bounded timeout cleanup, preserving the private Unix socket and normal terminate/wait/kill path. This is conditional test robustness, not a reproduced production outage; it can follow separately.

Existing nonblocking README version and future canonical test-fixture source threads are already raised at https://github.com/sonic-net/sonic-dbsyncd/pull/101#discussion_r4694416620 and #discussion_r4694519381; respond there rather than duplicating them. The installed fixture borrows declared dependencies and uses an LLDP JSON input; it does not establish full image closure or live lldpd/daemon execution.

Reviewed HEAD:8a7eb9f3da4ea3e350c35dcc25635ee4c0b0a413. Full independent three-general-plus-separate-SME source review and coordinator grounding. No reviewer Bazel/compiler/native imports, Redis/LLDP test, install or payload probe. Current hosted unit/installed targets reused cached results, not newly executed test bodies. Report: REPORT_PR_URL. Check current revision, CI and replies before submission.

## Approve

Source approval with optional follow-ups, not a claim of fresh native or live LLDP qualification. No introduced production blocker was found; wheel payload/entry ownership and private native-binding probe design are coherent.

Nonblocking packaging fidelity — preserve supported Maintainer metadata. In BUILD.bazel::sonic_dbsyncd_wheel, maintainer and maintainer_email are omitted. tests/bazel/installed_wheel_probe.py::test_complete_owner_payload_and_metadata requires their absence and README.md says the wheel API cannot represent them. However the selected rules_python1.9.0.sonic.2 patch0003 explicitly adds both attributes and emits/tests those METADATA fields. The new wheel therefore loses fields present in setup.py for a tooling limitation that does not apply. Please pass the existing setup-contract fields to the wheel rule and compare them in the installed-wheel test, removing the unsupported-fields exception/documentation; alternatively state an intentional omission policy accurately. This does not affect normal LLDP operation and can follow separately.

Nonblocking test cleanup — retain Redis ownership across outer probe timeout. In tests/bazel/installed_wheel_probe.py::test_native_redis_sync_without_owner_source_or_original_mocks, subprocess.run(... timeout=60) can kill the native probe process after it starts redis-server. The Redis process is cleaned only by tests/bazel/native_redis_probe.py::main finally in that killed child, so a stall can leave the grandchild until Bazel/container teardown. Please use a surviving-parent owner or a dedicated process group/session with bounded timeout cleanup, preserving the private Unix socket and normal terminate/wait/kill path. This is conditional test robustness, not a reproduced production outage; it can follow separately.

Existing nonblocking README version and future canonical test-fixture source threads are already raised at https://github.com/sonic-net/sonic-dbsyncd/pull/101#discussion_r4694416620 and #discussion_r4694519381; respond there rather than duplicating them. The installed fixture borrows declared dependencies and uses an LLDP JSON input; it does not establish full image closure or live lldpd/daemon execution.

Reviewed HEAD:8a7eb9f3da4ea3e350c35dcc25635ee4c0b0a413. Full independent three-general-plus-separate-SME source review and coordinator grounding. No reviewer Bazel/compiler/native imports, Redis/LLDP test, install or payload probe. Current hosted unit/installed targets reused cached results, not newly executed test bodies. Report: REPORT_PR_URL. Check current revision, CI and replies before submission.
