# Reader drafts: sonic-platform-common #824

Report: https://github.com/yxieca/sonic-review-reports/pull/69

## Comment
Source review supports the additive owner wheel and test-root design. No introduced blocking defect established. Source/installed API checks and exact rebuild/no-op accounting are meaningful but are not full independently installable image, native ABI or hardware qualification.

Optional descriptive metadata parity — BUILD.bazel::sonic_platform_common_wheel omits setup.py’s maintainer, maintainer_email, classifiers and keywords, though the selected packaging rule supports them. The installed contract compares name/version/requirements, not all descriptive fields, so metadata descriptions differ between build paths without a runtime/API failure. Copy the literal setup attributes into py_wheel if complete descriptive parity is intended; this can follow separately.

Nonblocking description clarification — the PR body says the wheel includes templates. BUILD.bazel::wheel_payload selects owner Python/API stubs/py.typed and licenses; generator/** templates are test_sources/build inputs, consistent with setup.py rather than installed owner payload. Clarify that generator templates are test/build inputs and the wheel carries owner API source/type files; no missing runtime data is asserted and no unrelated templates need packaging.

ReviewedHEAD:c70f9594b30780851fa4f0e7285c9c6885bede4d, BASE8b707ee55d463756e1e239083284320d0a4ad2b0. Full cumulative three-general plus separate-SME source review and coordinator grounding; only concrete missing-source gaps supplemented. Current hosted run uses merge9fd7da9 with two extra base CPO paths, not byte-identical HEAD. Two test targets and11incremental-control cases passed externally; no current2996case claim. Installed wheel checks borrow declared external/native dependencies; no reviewer Bazel/compiler/native imports/wheelinstall/tests/device/HW/network operation. Report: https://github.com/yxieca/sonic-review-reports/pull/69. Check current source, CI/integration and dependency selection before submission.

## Approve
Source approval with optional follow-ups that can be handled separately.

Source review supports the additive owner wheel and test-root design. No introduced blocking defect established. Source/installed API checks and exact rebuild/no-op accounting are meaningful but are not full independently installable image, native ABI or hardware qualification.

Optional descriptive metadata parity — BUILD.bazel::sonic_platform_common_wheel omits setup.py’s maintainer, maintainer_email, classifiers and keywords, though the selected packaging rule supports them. The installed contract compares name/version/requirements, not all descriptive fields, so metadata descriptions differ between build paths without a runtime/API failure. Copy the literal setup attributes into py_wheel if complete descriptive parity is intended; this can follow separately.

Nonblocking description clarification — the PR body says the wheel includes templates. BUILD.bazel::wheel_payload selects owner Python/API stubs/py.typed and licenses; generator/** templates are test_sources/build inputs, consistent with setup.py rather than installed owner payload. Clarify that generator templates are test/build inputs and the wheel carries owner API source/type files; no missing runtime data is asserted and no unrelated templates need packaging.

ReviewedHEAD:c70f9594b30780851fa4f0e7285c9c6885bede4d, BASE8b707ee55d463756e1e239083284320d0a4ad2b0. Full cumulative three-general plus separate-SME source review and coordinator grounding; only concrete missing-source gaps supplemented. Current hosted run uses merge9fd7da9 with two extra base CPO paths, not byte-identical HEAD. Two test targets and11incremental-control cases passed externally; no current2996case claim. Installed wheel checks borrow declared external/native dependencies; no reviewer Bazel/compiler/native imports/wheelinstall/tests/device/HW/network operation. Report: https://github.com/yxieca/sonic-review-reports/pull/69. Check current source, CI/integration and dependency selection before submission.
