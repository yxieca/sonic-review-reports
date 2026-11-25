# Human-operated feedback drafts

**Approval already submitted:** https://github.com/sonic-net/sonic-mgmt/pull/29474#pullrequestreview-6062153263 at `125f15cddd6a5ebe86d90f5a36bf6cb1e67d6abb`. Retained drafts are historical; do not resubmit identical feedback. The target bot reports all1changed file has qualified approval ([coverage receipt](https://github.com/sonic-net/sonic-mgmt/pull/29474#issuecomment-7169703970)); this is its reported result, not independently recomputed mapping. **Waiting CI** is the remaining observed gate: the aggregate Azure.sonic-mgmt check is QUEUED and its Probe UT/IT child is CANCELLED, while other returned checks are successful/skipped. Source approval is separate from pipeline completion, actual BMC/gNMI execution and202608 branch/backport evidence. No CI retry or target merge was performed.

Full source review at 125f15cddd6a5ebe86d90f5a36bf6cb1e67d6abb: three independent general lenses, separate SME and coordinator grounding. Native C++/BMC/Redis/D-Bus tests were not run. Report: https://github.com/yxieca/sonic-review-reports/pull/28. Existing inherited follow-ups remain tracked; check current head/replies and review gates before use. Actual PR targets master;202608 applicability is separate. Nothing is submitted automatically.

## Comment

Source review is favorable for the container-scoped gNMI port fallback. It now selects the server executable from docker top for the intended container, preserves CONFIG_DB priority, accepts space/equals port flags and keeps the existing defaults. Exact source controls reproduce the baseline wrong-first-port case and corrected argv/failure cases without executing Docker or gNMI. The inherited process-name bootstrap and202608 release/image evidence remain separate limitations; no new blocker retained.

Full source review at 125f15cddd6a5ebe86d90f5a36bf6cb1e67d6abb: three independent general lenses, separate SME and coordinator grounding. Native C++/BMC/Redis/D-Bus tests were not run. Report: https://github.com/yxieca/sonic-review-reports/pull/28. Existing inherited follow-ups remain tracked; check current head/replies and review gates before use. Actual PR targets master;202608 applicability is separate. Nothing is submitted automatically.

## Approve with comment

The current source is favorable: container-scoped process selection fixes the reported host-PID cross-container port mix-up, with CONFIG_DB precedence and defaults retained. Add isolated parser regression coverage if useful, but no new code blocker was found. Author BMC three-run202608 evidence is reported, not this review’s execution; current destination branch/backport was not verified. Check current head/replies/evidence before selecting approval; nothing is submitted automatically.

Full source review at 125f15cddd6a5ebe86d90f5a36bf6cb1e67d6abb: three independent general lenses, separate SME and coordinator grounding. Native C++/BMC/Redis/D-Bus tests were not run. Report: https://github.com/yxieca/sonic-review-reports/pull/28. Existing inherited follow-ups remain tracked; check current head/replies and review gates before use. Actual PR targets master;202608 applicability is separate. Nothing is submitted automatically.
