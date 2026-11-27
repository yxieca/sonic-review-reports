# Archived review — target merged

Target https://github.com/sonic-net/sonic-mgmt-framework/pull/203 merged at `2026-11-27T05:48:55Z` (merge commit `740be66d46a5e1b2b8815cdac4aec85a01580e71`). Reviewed head: `6c932ad921a3519beb0ecc429f1825f03be27a25`. [Current-head source approval](https://github.com/sonic-net/sonic-swss/pull/203#pullrequestreview-6083964447) remains verified. Required CI passed. No target merge or other target mutation was performed during archival.

R1 is source-resolved: Make cleanup excludes BUILD.bazel alongside routes.go. Q1 syntax-probe isolation and N1 dependency documentation remain nonblocking recommendations; merge does not establish these follow-ups fixed. Original full and incremental source coverage and validation limits are preserved below. Earlier waiting states and reader drafts are historical; temporary actions are retired.

## Historical drafts — not actionable

# Current editable feedback

## Comment
**Source correction verified:** [models/openapi_codegen.mk](https://github.com/sonic-net/sonic-mgmt-framework/blob/6c932ad921a3519beb0ecc429f1825f03be27a25/models/openapi_codegen.mk#L119-L129) now excludes `BUILD.bazel` alongside `routes.go`. Retained root `models-clean`, `rest-clean` and `clean` callers preserve the permanent OpenAPI package while other regular generated files remain selected for deletion. This is the exact minimal fix; no cleanup or native build was executed.

**Nonblocking Q1:** `CLI/bazel/installed_probe.py` still omits `CLISH_NOAUTH`; owned plugin startup can select `/var/run/rest-local.sock` before syntax-only command checking. Prefer `CLISH_NOAUTH=1` for command-tree-only checks or a private authentication fixture. This is qualified test isolation, not a new production-authentication defect; exact archive/native startup remains untested.

**Nonblocking N1:** `tools/bazel/README.md` and `CLI/bazel/README.md` retain older Common/Infra dependency references than `MODULE.bazel`. Update or mark those historical so readers inspect the correct selected contracts.

Reviewed HEAD `6c932ad921a3519beb0ecc429f1825f03be27a25`. Full report: https://github.com/yxieca/sonic-review-reports/pull/80. The existing suggestion7209324673 is preserved; do not duplicate it. No compiler, imports, services, tests, package/archive, device or target GitHub action was performed.

## Approval draft
**Source correction verified:** [models/openapi_codegen.mk](https://github.com/sonic-net/sonic-mgmt-framework/blob/6c932ad921a3519beb0ecc429f1825f03be27a25/models/openapi_codegen.mk#L119-L129) now excludes `BUILD.bazel` alongside `routes.go`. Retained root `models-clean`, `rest-clean` and `clean` callers preserve the permanent OpenAPI package while other regular generated files remain selected for deletion. This is the exact minimal fix; no cleanup or native build was executed.

**Nonblocking Q1:** `CLI/bazel/installed_probe.py` still omits `CLISH_NOAUTH`; owned plugin startup can select `/var/run/rest-local.sock` before syntax-only command checking. Prefer `CLISH_NOAUTH=1` for command-tree-only checks or a private authentication fixture. This is qualified test isolation, not a new production-authentication defect; exact archive/native startup remains untested.

**Nonblocking N1:** `tools/bazel/README.md` and `CLI/bazel/README.md` retain older Common/Infra dependency references than `MODULE.bazel`. Update or mark those historical so readers inspect the correct selected contracts.

Reviewed HEAD `6c932ad921a3519beb0ecc429f1825f03be27a25`. Full report: https://github.com/yxieca/sonic-review-reports/pull/80. The existing suggestion7209324673 is preserved; do not duplicate it. No compiler, imports, services, tests, package/archive, device or target GitHub action was performed.

Source-favorable manual draft only; check current head and CI/integration readiness before any formal approval.