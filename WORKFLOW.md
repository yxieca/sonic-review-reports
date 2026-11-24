# Proposed report-review workflow

1. Create one report PR per target PR (or explicitly identified review scope). Pin target head/base and actual coverage. Keep report revisions on the same branch; do not discard discussion through replacement PRs.
2. Use stable local issue IDs. Severity, disposition and whether feedback was submitted are separate. Record fixes with their target SHA; retain withdrawn/deferred findings with reasons.
3. Watch report comments, review threads and target changes through the existing assistant backlog watcher. Read changed comments with their surrounding discussion; report-only questions do not require restarting unchanged code panels.
4. The assistant owns watching target commits and author replies, reviewing the exact changed scope and updating the report, action drafts and page accordingly. Preserve the original finding and append dated issue-level history containing the author-response link, reviewed target SHA, evidence and changed disposition (fixed, deferred, withdrawn or still open). Keep stable IDs and normal commit history; no silent deletion, renumbering or force-push. Clearly separate the current verdict from the historical claim. New findings require source grounding; a material policy or acceptance decision belongs to the human reviewer.
5. Provide two navigation links plus copyable feedback drafts appropriate to the current verdict. GitHub does not offer a reliable URL that submits a prefilled formal review as the reader: readers select the verdict and submit with their own account. Do not claim one-click request-changes/approval, solicit tokens or impersonate the report owner.
6. Check current head and existing target discussion before feedback. Links do not automatically post; target writes by the assistant retain exact-command preview/authorization rules. External readers can submit their own reviews under repository permissions.
7. Reviewers approve the report PR; they need not merge it. After the target is verified MERGED or CLOSED, update its terminal state and each issue outcome. With the report's current revision approved and no unresolved report-review objections, the assistant merges ONLY the report PR in yxieca/sonic-review-reports and removes that report's unique action page from the published site. This is Ying's narrowly scoped authorization (2026-11-24), not permission to merge target SONiC PRs. Closed-withdrawn targets are not equivalent to fixed findings. GitHub merge and Pages cleanup are separate operations: verify both, retain failure state and retry only unfinished work; never claim atomic completion.

## Monitoring ownership

The report PR conversation must stay current as well as the report file. Reply to human questions in their existing threads; maintain the PR body as the current summary (target SHA, issue dispositions, rendered-report and action links); append dated comments for substantive target responses, fixes or verdict changes. Preserve earlier comments and mark superseded conclusions explicitly rather than deleting history. Do not spam unchanged monitoring status or post target feedback automatically.

The requesting assistant retains the originating report review and uses the established hourly/daily backlog workflow, not a new GitHub Actions workflow or credential-bearing bot. Monitor errors and missed delivery must remain visible. This repository contains no automated target mutation, workflow dispatch, merge, webhook or token storage.

## Public/private boundary

Publish the explanatory report, not entire local transcripts, raw model prompts, credentials, private inventories/hostnames, absolute local paths or nonpublic build/runtime data. Public source links and concise attributed evidence suffice. Keep raw review artifacts in their existing private location. Before any broader report migration, inspect each report separately; permission to publish this pilot is not permission to publish all local review files.

## Initial pilot

Target: sonic-net/sonic-mgmt #28850. Report and drafts are prepared for human review, not additional target feedback. R1/R3 are before-landing findings; R2 has a proposed deferral option that is not yet accepted. Templates in this PR are drafts, not imposed repository policy until the human review accepts them.
