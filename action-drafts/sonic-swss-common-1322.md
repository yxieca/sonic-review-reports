## Current Q3 disposition — keep-together rationale accepted

A separate prerequisite PR is no longer requested as an acceptance condition. The Lua override is an opt-in shared-runtime adaptation needed by the chosen private gNMI test layout, preserving legacy loading when unset/empty. The SWIG directives address the selected generator's const-correctness issue in an existing shared interface. Keeping them with Bazel enablement is reasonable with explicit shared-consumer compatibility and validation limits.

[Clarification posted](https://github.com/sonic-net/sonic-swss-common/pull/1322#issuecomment-7201132831). This accepts the organizational rationale, not a new-head build/ABI or source-equivalence result. Current-head independent reconciliation remains pending; historical drafts stay disabled. Earlier split requests and approvals remain historical, not current requirements or live approval receipts.

<!-- source-evidence-hold-1030-27b1ac06249a76c481728d396356131ce1f8632c -->

**Historical drafts — not actionable at the current head.**

**Needs Report Update — current revision not yet qualified.** Target advanced from the covered revision `766d9b117023cd2c1edab74158e96098d3f96069` to `27b1ac06249a76c481728d396356131ce1f8632c`. Changed source and its reached dependency contracts require independent reconciliation. Prior completed full-panel and bounded follow-up evidence remain preserved; historical findings are not current-head qualification. The author explains the downstream gNMI Lua-loader dependency and proposes isolating that scope in a dedicated commit (https://github.com/sonic-net/sonic-swss-common/pull/1322#issuecomment-7200324467). The prior approval is now dismissed; it does not qualify the new head. Reported tests remain author-reported, not reviewer execution. The coverage gap is not a confirmed code defect. Do not submit historical feedback drafts.

**Current Q3 disposition: keep-together rationale accepted; separate-PR split is no longer requested. Prior approval is dismissed and these historical drafts are not actionable at the new head.**

# Reader drafts: Common #1322

Report: https://github.com/yxieca/sonic-review-reports/pull/73

## Comment
Source approval within the reviewed Common library/binding/package contracts; no confirmed introduced blocker. Shared source/SONAME/header/native dependency ownership and Lua override compatibility are source-supported. Generated output/ABI, every original authentication case and installed image acceptance remain separate.

Nonblocking N1 — docs/bazel.md’s no-YANG installed-check example omits required --libnl-package arguments and --netlink-probe. tools/bazel/runtime/installed_check.py::main declares both required, so the documented command stops at argument parsing rather than performs the installed-library check. Adding only the later YANG option does not fix it. Mirror .github/workflows/bazel-native.yml’s three selected libnl archives and bazel-bin/tests/shared_netlink/consumer, preserving architecture/YANG selection. The actual workflow already supplies them; this can be a separate documentation correction, not a native CI failure.

HEAD766d9b117023cd2c1edab74158e96098d3f96069 BASE54f2f0e9ce455b37aeffc5b4e08b522d708defa0. Full cumulative three-independent-general plus separate-SME source review and coordinator grounding; only missing source scopes supplemented. Current externalnative run45805377204 executed23/24targets by YANGmode plusseparatechecks, on mergee396307b with Cargo.lock/CodeQLbasechanges—notidenticalHEAD. No reviewer compile/Bazel/native imports/tests/Redis/DUT/install/archivepayload or generated-wrapper execution. Source/string/parser controls only; generated ABI/external locks/deployment notcertified. Report: https://github.com/yxieca/sonic-review-reports/pull/73. Check source/current CI/reviewer state before manual feedback.

## Source approval
Source approval with a nonblocking documentation follow-up.

Source approval within the reviewed Common library/binding/package contracts; no confirmed introduced blocker. Shared source/SONAME/header/native dependency ownership and Lua override compatibility are source-supported. Generated output/ABI, every original authentication case and installed image acceptance remain separate.

Nonblocking N1 — docs/bazel.md’s no-YANG installed-check example omits required --libnl-package arguments and --netlink-probe. tools/bazel/runtime/installed_check.py::main declares both required, so the documented command stops at argument parsing rather than performs the installed-library check. Adding only the later YANG option does not fix it. Mirror .github/workflows/bazel-native.yml’s three selected libnl archives and bazel-bin/tests/shared_netlink/consumer, preserving architecture/YANG selection. The actual workflow already supplies them; this can be a separate documentation correction, not a native CI failure.

HEAD766d9b117023cd2c1edab74158e96098d3f96069 BASE54f2f0e9ce455b37aeffc5b4e08b522d708defa0. Full cumulative three-independent-general plus separate-SME source review and coordinator grounding; only missing source scopes supplemented. Current externalnative run45805377204 executed23/24targets by YANGmode plusseparatechecks, on mergee396307b with Cargo.lock/CodeQLbasechanges—notidenticalHEAD. No reviewer compile/Bazel/native imports/tests/Redis/DUT/install/archivepayload or generated-wrapper execution. Source/string/parser controls only; generated ABI/external locks/deployment notcertified. Report: https://github.com/yxieca/sonic-review-reports/pull/73. Check source/current CI/reviewer state before manual feedback.

## Questions — Q3 prerequisite split

Could the shared runtime/binding changes be split into a prerequisite PR, with this Bazel build PR depending on it?

Two changes affect consumers outside Bazel:
- `common/redisapi.h::loadLuaScript()` introduces the `SWSS_COMMON_LUA_DIR` runtime override and its path-validation behavior. The unset/empty case preserves legacy behavior, but the nonempty case is a shared library feature.
- `pyext/swsscommon.i` changes Python/Go wrapping of static string constants. This shared interface is also consumed by the existing build paths.

The SWIG changes appear needed for the selected SWIG 4.3-generated wrappers to compile: the automatic wrapper uses mutable char pointers for const-pointer constants. The Lua override instead supports loading scripts from the staged runtime; it is not a fix for a C++ compilation failure.

A separate prerequisite PR would let these shared compatibility/API changes be reviewed independently, then the Bazel build can retain the necessary dependency. Could you confirm the minimal required changes and their Make/Bazel validation? This requests separation and clarification, not removal of a necessary build fix or a claim that either feature is inherently wrong.

Supporting report: https://github.com/yxieca/sonic-review-reports/pull/73
Reviewed head: `766d9b117023cd2c1edab74158e96098d3f96069`. This assessment inspected source; it did not independently rebuild with the changes reverted.
