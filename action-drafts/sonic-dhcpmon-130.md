# Reader drafts: sonic-dhcpmon #130

Report: https://github.com/yxieca/sonic-review-reports/pull/63

## Comment

Source review supports the additive build/package path: ten production translation units retained, paired JsonCpp include correction, real util.cpp-linked test with correctly typed shared-mutex fixture, and declared runtime/debug/metadata ownership. No introduced blocker found.

Nonblocking documentation — correct the configured registry name. README.bazel.md:3 says canonical securely1g registry, but .bazelrc selects sonic-net/sonic-bazel-registry/main plus BCR. Change the prose to SONiC registry; no configured wrong-origin bug was found.

Optional utility coverage — explicitly exercise an unaligned byte accumulator input. tests/util_behavior_test.cpp sweeps lengths0..65 at one bytes.data() address; it does not deliberately set unaligned starting alignment. Add an alignas backing buffer and data()+1 case to checksum_accumulate_words, compared with its reference. The production function already reads bytes and no alignment defect was found; do not create misaligned iphdr pointers. This can follow separately.

Optional checker coverage — add focused rejection controls for .github/scripts/check_dhcpmon_artifacts.py::verify/copy_payload and check_dhcpmon_metadata.py::verify. Current hosted CI exercises the positive CLI path, but no dedicated owner regression tests reject extra/wrong/nonregular payloads, wrong owner/mode/machine, mismatched build ID/debuglink CRC, wrong payload/control hash or missing target provider. Use the existing helpers with inert fixtures, not another daemon/native campaign. No current false acceptance was demonstrated.

Provider-verification scope question: the metadata checker matches Depends package names/control architecture and library basenames against DT_NEEDED; it does not independently establish provider ELF machine/SONAME/versioned-alternative ABI. Please keep its claim at provider-name consistency or add separately scoped strengthening if a complete provider-ABI proof is intended. The underlying metadata generator is stronger; this is nonblocking, not a proved dependency bug.

Reviewed HEAD:65b99647b87eb0955009310c531d0fadcb840c60, BASE3e7160d9b89ad7c701a0827af80367ab1b206ccf. Full independent three-general-plus-separate-SME source review and coordinator grounding. No reviewer compiler/Bazel/native utility test, DB/Redis/DHCP traffic, install or payload probe. Existing hosted native AMD64/ARM64 utility and artifact/metadata checks succeeded externally. Report: https://github.com/yxieca/sonic-review-reports/pull/63. Verify current revision, CI and replies before using this draft.

## Approve

Source review supports approval; the notes below are optional/nonblocking and can follow separately. Approval does not claim daemon health, DB/dual-ToR or live forwarding qualification.

Nonblocking documentation — correct the configured registry name. README.bazel.md:3 says canonical securely1g registry, but .bazelrc selects sonic-net/sonic-bazel-registry/main plus BCR. Change the prose to SONiC registry; no configured wrong-origin bug was found.

Optional utility coverage — explicitly exercise an unaligned byte accumulator input. tests/util_behavior_test.cpp sweeps lengths0..65 at one bytes.data() address; it does not deliberately set unaligned starting alignment. Add an alignas backing buffer and data()+1 case to checksum_accumulate_words, compared with its reference. The production function already reads bytes and no alignment defect was found; do not create misaligned iphdr pointers. This can follow separately.

Optional checker coverage — add focused rejection controls for .github/scripts/check_dhcpmon_artifacts.py::verify/copy_payload and check_dhcpmon_metadata.py::verify. Current hosted CI exercises the positive CLI path, but no dedicated owner regression tests reject extra/wrong/nonregular payloads, wrong owner/mode/machine, mismatched build ID/debuglink CRC, wrong payload/control hash or missing target provider. Use the existing helpers with inert fixtures, not another daemon/native campaign. No current false acceptance was demonstrated.

Provider-verification scope question: the metadata checker matches Depends package names/control architecture and library basenames against DT_NEEDED; it does not independently establish provider ELF machine/SONAME/versioned-alternative ABI. Please keep its claim at provider-name consistency or add separately scoped strengthening if a complete provider-ABI proof is intended. The underlying metadata generator is stronger; this is nonblocking, not a proved dependency bug.

Reviewed HEAD:65b99647b87eb0955009310c531d0fadcb840c60, BASE3e7160d9b89ad7c701a0827af80367ab1b206ccf. Full independent three-general-plus-separate-SME source review and coordinator grounding. No reviewer compiler/Bazel/native utility test, DB/Redis/DHCP traffic, install or payload probe. Existing hosted native AMD64/ARM64 utility and artifact/metadata checks succeeded externally. Report: https://github.com/yxieca/sonic-review-reports/pull/63. Verify current revision, CI and replies before using this draft.
