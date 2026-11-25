# Human-operated feedback drafts

Full standalone link-up source review at 8f306a0d2dcd8d369d4364caa0a4cc30c56be761: three independent general roles, separate SME and coordinator grounding. Closed inert controls only; no native/image/HW validation or downstream firmware requirement. Report: https://github.com/yxieca/sonic-review-reports/pull/22. Check current head/replies; no automatic submission or approval.

## Questions

Could you address the newly identified standalone integration concerns R4/R5? R4: the selected media-setting caller uses get_sfp(CPO).get_xcvr_api() in eligible cold-start notification, but this platform intentionally returns no SFP at CPO indices; the resulting AttributeError can stop the worker. Could the selected consumer use its technology-aware device accessor? R5: switching ThermalManager to get_all_ports bypasses ModularChassis line-card aggregation; could modular polymorphic enumeration be preserved and tested? Existing R1/R2 ELS-hook/ASIC-event discussions remain relevant without duplicate posts. R3 is now nonblocking: actual default selection prefers JSON, while the alternate INI still differs. Q1/Q2 remain topology/poll-subset questions, not physical outage claims.

Full standalone link-up source review at 8f306a0d2dcd8d369d4364caa0a4cc30c56be761: three independent general roles, separate SME and coordinator grounding. Closed inert controls only; no native/image/HW validation or downstream firmware requirement. Report: https://github.com/yxieca/sonic-review-reports/pull/22. Check current head/replies; no automatic submission or approval.

## Request changes

Please correct new R4/R5 before source acceptance: align the selected CPO media-key caller with technology-separated get_sfp/get_cpo access, and preserve modular line-card thermal enumeration when using get_all_ports. Add eligible CPO/SFP notification and modular subclass-dispatch regression controls. Existing R1/R2 should be resolved in their current threads, without duplicating their feedback. R3 is a nonblocking JSON/INI consistency item after actual JSON-first selection verification; Q1/Q2 remain qualified. Preserve standalone link-up scope and conservative hardware policy; no downstream firmware/CDB/fault/VDM implementation is required by this draft.

Full standalone link-up source review at 8f306a0d2dcd8d369d4364caa0a4cc30c56be761: three independent general roles, separate SME and coordinator grounding. Closed inert controls only; no native/image/HW validation or downstream firmware requirement. Report: https://github.com/yxieca/sonic-review-reports/pull/22. Check current head/replies; no automatic submission or approval.
