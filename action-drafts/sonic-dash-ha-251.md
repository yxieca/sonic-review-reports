# Current source-favorable drafts

## Comment
The current source `40e7c6dee7406a99511e4411dca89498e742fc8d` now incorporates the reviewed fork correction: canonical workspace Cargo inputs select tracing without the previous static caps, and Common Rust sources match the lock while native Common C ownership remains separate. R1's original static-cap selection is source-resolved; Q1's canonical source contract is addressed. No repeated target feedback is requested.

The recorder regression reads a DEBUG event back from the real independent file layer. Its scope does not establish the complete production INFO-main/TRACE-recorder composition or a generated graph/native ABI result. Those remain qualifications, not a newly proven current-head defect. Source review ran no native tests, compiler, imports, services or package/device probes. Full report: https://github.com/yxieca/sonic-review-reports/pull/79. Recheck CI/integration and current revision before any manual verdict.

## Approval draft
The current source `40e7c6dee7406a99511e4411dca89498e742fc8d` now incorporates the reviewed fork correction: canonical workspace Cargo inputs select tracing without the previous static caps, and Common Rust sources match the lock while native Common C ownership remains separate. R1's original static-cap selection is source-resolved; Q1's canonical source contract is addressed. No repeated target feedback is requested.

The recorder regression reads a DEBUG event back from the real independent file layer. Its scope does not establish the complete production INFO-main/TRACE-recorder composition or a generated graph/native ABI result. Those remain qualifications, not a newly proven current-head defect. Source review ran no native tests, compiler, imports, services or package/device probes. Full report: https://github.com/yxieca/sonic-review-reports/pull/79. Recheck CI/integration and current revision before any manual verdict.

Source-favorable manual draft; no automatic approval or release of CI/qualification gates.