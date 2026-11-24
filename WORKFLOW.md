# Proposed report-review workflow

1. Create one report PR per target PR (or explicitly identified review scope). Pin target head/base and actual coverage. Keep report revisions on the same branch; do not discard discussion through replacement PRs.
2. Use stable local issue IDs. Severity, disposition and whether feedback was submitted are separate. Record fixes with their target SHA; retain withdrawn/deferred findings with reasons.
3. Watch report comments, review threads and target changes through the existing assistant backlog watcher. Read changed comments with their surrounding discussion; report-only questions do not require restarting unchanged code panels.
4. Update the report and action drafts for factual corrections and answers. Preserve prior conclusions in commit history and a short issue-level revision note. New findings require source grounding. A material policy or acceptance decision belongs to the human reviewer.
5. Provide two navigation links plus copyable feedback drafts appropriate to the current verdict. GitHub does not offer a reliable URL that submits a prefilled formal review as the reader: readers select the verdict and submit with their own account. Do not claim one-click request-changes/approval, solicit tokens or impersonate the report owner.
6. Check current head and existing target discussion before feedback. Links do not automatically post; target writes by the assistant retain exact-command preview/authorization rules. External readers can submit their own reviews under repository permissions.
7. When target merges/closes, update terminal state and issue outcomes. Mark archival ready and notify the maintainer. The assistant does not merge target or report PRs; existing no-merge ownership remains. Closed-withdrawn target is not equivalent to fixed findings.

## Monitoring ownership

The requesting assistant retains the originating report review and uses the established hourly/daily backlog workflow, not a new GitHub Actions workflow or credential-bearing bot. Monitor errors and missed delivery must remain visible. This repository contains no automated target mutation, workflow dispatch, merge, webhook or token storage.

## Public/private boundary

Publish the explanatory report, not entire local transcripts, raw model prompts, credentials, private inventories/hostnames, absolute local paths or nonpublic build/runtime data. Public source links and concise attributed evidence suffice. Keep raw review artifacts in their existing private location. Before any broader report migration, inspect each report separately; permission to publish this pilot is not permission to publish all local review files.

## Initial pilot

Target: sonic-net/sonic-mgmt #28850. Report and drafts are prepared for human review, not additional target feedback. R1/R3 are before-landing findings; R2 has a proposed deferral option that is not yet accepted. Templates in this PR are drafts, not imposed repository policy until the human review accepts them.
