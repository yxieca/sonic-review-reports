# Review: <owner/repository> #<target-number>

**Target:** <target PR URL>  
**Reviewed head:** `<SHA>`  
**Reviewed base:** `<SHA>`  
**Review date:** <date>  
**Report PR:** <report PR URL>  
**Coverage:** <actual completed roles/reused scope/missing coverage>  
**Disposition:** <awaiting human review / revised / target feedback submitted / archival pending>

## Recommendation

<Separate source recommendation, CI/deployment readiness and authority to submit or merge.>

## Summary

<What changes, actual reached consumers, supported scope and preserved behavior.>

## Issue index

| ID | Kind / severity | Disposition | Evidence / existing discussion |
|---|---|---|---|
| R1 | Blocking / P2 | Open | <link> |
| N1 | Nit / P3 | Open | <link> |

IDs are unique within this report PR, stable across edits and never reused. Changing severity does not change the ID. Do not invent a finding to fill a template row.

## <ID> — <finding title>

**Kind:** <blocking / conditional concern / nit / question>.  
**Severity:** <priority or not applicable>.  
**Disposition:** <open / fixed in target SHA / deferred by named decision / withdrawn with reason>.  
**Anchor:** <immutable target file/line/function and at least one caller where relevant>.

<Exact condition, additional consequence and affected supported scope.>

**Evidence:** <source facts versus executed controls versus author-reported/runtime evidence>.  
**Introduced or inherited:** <direct regression / new-path gap / pre-existing>.  
**Requested correction:** <smallest appropriate fix or precise question>.  
**Discussion:** <existing target thread, actual author response, resolution versus technical agreement>.  
**Revision history:** <human question, response and changed conclusion; retain withdrawals>.

## Validation and limitations

<Commands/outcomes actually executed, interpreter/dependency context and source hashes; author evidence separately. No stale or hardware PASS transfer.>

## Consensus / grounding

<Actual completed independent roles and missing roles; dissent; discarded or downgraded candidates with reasons.>

## Human feedback

Use issue IDs in comments. Answer questions and update report/drafts with evidence in ordinary commits. Do not silently remove concerns or equate resolved report threads with fixed target source.

## Reader actions

If blockers remain:
1. <target Files changed URL> — choose Request changes manually, paste/edit linked draft.
2. <target conversation URL> — comment as questions without review verdict.

If no blockers remain:
1. <target conversation URL> — comment without approval, paste/edit linked draft.
2. <target Files changed URL> — choose Approve manually with the linked comment draft.

Both drafts must include the specific report PR backlink. Links only navigate; they do not authenticate, prefill a guaranteed verdict, submit or merge. The submitter uses their own account and judgment. Check for stale target head and existing duplicate feedback first.

## Lifecycle

A target head change requires freshness/delta review. When the target merges or closes, record terminal state and outstanding/fixed/deferred/withdrawn issue dispositions. The report becomes ready for archival; a maintainer decides the report PR merge. Target closure is not proof that findings were fixed.
