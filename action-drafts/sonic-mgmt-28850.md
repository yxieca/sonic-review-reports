# Human-operated feedback drafts: sonic-mgmt #28850

Report: https://github.com/yxieca/sonic-review-reports/pull/1  
Target: https://github.com/sonic-net/sonic-mgmt/pull/28850  
Reviewed head: `834b687c739eb0b5e72ad49770afc8a9a9cd6a30`

These are draft text, not submitted reviews. Confirm the head, read existing discussion and revise to reflect your own judgment. Existing R1/R2/R3 discussions already cover these concerns; reference them rather than duplicating them. The signed-in person submitting is responsible for the verdict. No draft impersonates Ying or claims human approval not yet given.

## 1. Request-changes review draft

[Open target Files changed](https://github.com/sonic-net/sonic-mgmt/pull/28850/files), select **Review changes → Request changes**, and paste/edit:

> I reviewed the findings in https://github.com/yxieca/sonic-review-reports/pull/1 against the target change. Before landing, please resolve or explain R1 (unconfirmed test-leak cleanup finishing normally) and R3 (vendor MINOR-to-MAJOR escalation missing power recovery). R2's probe-episode synchronization needs either a reliable boundary or an explicit, supported deferral/containment decision.
>
> These points are already discussed in the linked target threads; I am referencing those discussions rather than raising them as newly discovered issues. Please use the report IDs when explaining a correction or disagreement. The report includes the exact reviewed revision, scope and evidence limits.
>
> AI-assisted review report: https://github.com/yxieca/sonic-review-reports/pull/1. This submission reflects my own review and decision.

## 2. Comment-as-questions draft

[Open target conversation](https://github.com/sonic-net/sonic-mgmt/pull/28850#issuecomment-new) and paste/edit:

> Following the existing discussions, could you clarify the remaining points in https://github.com/yxieca/sonic-review-reports/pull/1?
>
> - R1: what establishes unsuccessful teardown or verified cleanup if bulk withdrawal returns false? The warning-only decision is acknowledged.
> - R2: what ensures reinjection starts a new daemon episode if the recovery predicate observes the old No row before publication? Could this be safely deferred with an explicit containment?
> - R3: should the vendor recovery guard include the MINOR-to-MAJOR escalation case when MAJOR can remove power?
>
> I am asking for correction or explanation, not asserting a physical outage. The report distinguishes new-path gaps, the direct recovery regression, and source/inert versus hardware evidence.
>
> AI-assisted review report: https://github.com/yxieca/sonic-review-reports/pull/1. This comment is not an approval or a Changes Requested verdict.

## If blockers are later resolved

Reconcile evidence and update issue dispositions first. Then replace the two action drafts with **comment without approval** and **approve with comment**. Keep any remaining nits explicitly optional, preserve this report backlink, and retain the previous draft/disposition history through normal commits. Never offer an approval link merely because CI is green.
