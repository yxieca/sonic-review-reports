# Current reader drafts: sonic-mgmt #27902

Report: https://github.com/yxieca/sonic-review-reports/pull/33

## Comment

The original design clarifications are addressed: E3-04 now uses distinct100+10ccounts under fresh map windows; named queues/zero-other-queue deltas and fresh sub-run captures are explicit; E5-01 starts a freshTTL15chain; E4-04 permits256labels repeated40times (10,240packets). These corrections are source-verified and do not claim platform qualification. Thank you for clarifying them; the earlier questions are not being reposted.

Nonblocking TTL-expiry counter-window clarification. In docs/testplan/scaleup/scaleup_esun_testplan.md, the new common verification rule at368defines one fresh counter window per step/varied parameter value. ESUN-E5-02 at440still sends100TTL1frames and100TTL0frames, then expects a combined+200ingress-drop delta. Clearing/snapshotting per TTL sub-run gives100in each window, so the final individual window cannot show200even for intended correct behavior. Please state that the two expiry batches share one baseline/combined200check, or assert100per fresh sub-run and explicitly sum200. This is prospective wording, not an implemented-test failure or a new blocker; it does not reopen the corrected E5-01TTLsequence.

ReviewedHEAD:af0fa70af966032f46d90f0173411142e5d0e25a, BASEd0f1689605c5198308646a272c8bd0caba9ed7b8. Original full review at a8b9d1a retained; new independent general and separate-SME delta source checks plus coordinator arithmetic/grounding. Prospective test-plan review only: no implemented SAI/PTF/DUT/native tests or ESUN qualification. Report: https://github.com/yxieca/sonic-review-reports/pull/33. Verify current revision and replies before submission.

## Questions

The original design clarifications are addressed: E3-04 now uses distinct100+10ccounts under fresh map windows; named queues/zero-other-queue deltas and fresh sub-run captures are explicit; E5-01 starts a freshTTL15chain; E4-04 permits256labels repeated40times (10,240packets). These corrections are source-verified and do not claim platform qualification. Thank you for clarifying them; the earlier questions are not being reposted.

Could E5-02 explicitly choose one of these valid counter-window interpretations?

Nonblocking TTL-expiry counter-window clarification. In docs/testplan/scaleup/scaleup_esun_testplan.md, the new common verification rule at368defines one fresh counter window per step/varied parameter value. ESUN-E5-02 at440still sends100TTL1frames and100TTL0frames, then expects a combined+200ingress-drop delta. Clearing/snapshotting per TTL sub-run gives100in each window, so the final individual window cannot show200even for intended correct behavior. Please state that the two expiry batches share one baseline/combined200check, or assert100per fresh sub-run and explicitly sum200. This is prospective wording, not an implemented-test failure or a new blocker; it does not reopen the corrected E5-01TTLsequence.

ReviewedHEAD:af0fa70af966032f46d90f0173411142e5d0e25a, BASEd0f1689605c5198308646a272c8bd0caba9ed7b8. Original full review at a8b9d1a retained; new independent general and separate-SME delta source checks plus coordinator arithmetic/grounding. Prospective test-plan review only: no implemented SAI/PTF/DUT/native tests or ESUN qualification. Report: https://github.com/yxieca/sonic-review-reports/pull/33. Verify current revision and replies before submission.
