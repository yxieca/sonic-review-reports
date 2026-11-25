# Self-contained reader drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/39

Reviewed target head: `d5bc80720c7438cc48033976442cabb576ac5ac8`. Existing issue dispositions, coverage limits and target-feedback receipts remain unchanged. This presentation update submits no target feedback.



## Questions without verdict

Questions for correction or explanation; no formal verdict.

**P2 — exact-T2 generator/template mismatch for newly recognized NH-4210 variants.** `tests/common/helpers/pfc_storm.py:39,190–195,278–314,439–454` deploys the XGS executable for newly recognized NH-4210 SKUs on exact `t2`, but still selects the CPU start/stop templates `pfc_storm_sonic_t2.j2` and its stop counterpart. Their -t/-s/-n options are rejected by the XGS parser before storm generation; the all-port caller then waits for a storm never started. Pair executable with compatible start/stop templates, preserve the T2 CPU executable if intentional, or explicitly exclude unsupported topology. This newly affects variants such as P128-C1; the O256 mismatch is inherited. LT2 controls are compatible and are not claimed broken. Source/retained renderer evidence is not a lab-incidence or hardware measurement.

Source: https://github.com/sonic-net/sonic-mgmt/blob/d5bc80720c7438cc48033976442cabb576ac5ac8/tests/common/helpers/pfc_storm.py#L278-L314

Reviewed target head: `d5bc80720c7438cc48033976442cabb576ac5ac8`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/39.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Request changes with comment

Request-changes reader draft for the retained findings below.

**P2 — exact-T2 generator/template mismatch for newly recognized NH-4210 variants.** `tests/common/helpers/pfc_storm.py:39,190–195,278–314,439–454` deploys the XGS executable for newly recognized NH-4210 SKUs on exact `t2`, but still selects the CPU start/stop templates `pfc_storm_sonic_t2.j2` and its stop counterpart. Their -t/-s/-n options are rejected by the XGS parser before storm generation; the all-port caller then waits for a storm never started. Pair executable with compatible start/stop templates, preserve the T2 CPU executable if intentional, or explicitly exclude unsupported topology. This newly affects variants such as P128-C1; the O256 mismatch is inherited. LT2 controls are compatible and are not claimed broken. Source/retained renderer evidence is not a lab-incidence or hardware measurement.

Source: https://github.com/sonic-net/sonic-mgmt/blob/d5bc80720c7438cc48033976442cabb576ac5ac8/tests/common/helpers/pfc_storm.py#L278-L314

Reviewed target head: `d5bc80720c7438cc48033976442cabb576ac5ac8`. Retained source evidence and its stated scope/coverage are reused; this audit executed no candidate code, native tests, build, device, service or network payload validation. Supporting report: https://github.com/yxieca/sonic-review-reports/pull/39.

Check current revision and replies, and avoid duplicating existing feedback. This editable draft does not submit anything automatically.



## Prior draft history

The prior wording is preserved in the preceding report commit. This update expands author-facing explanations only; it does not change findings, severity, source coverage, target verdict or submission state.
