# SONiC review reports

Public, revision-pinned AI-assisted review reports for SONiC pull requests.

Reports are discussed in pull requests here before anyone decides whether to submit feedback to the target repository. A report's recommendation is not a submitted GitHub review and does not establish CI, image or hardware qualification.

This repository is being piloted. Report analysis and repository-wide documentation are reviewed in separate pull requests.

## How to use a review report

This repository hosts revision-pinned, AI-assisted reviews of SONiC pull requests. A report PR is a place to examine the analysis and improve it before deciding what feedback belongs on the target PR.

A report is evidence to evaluate, not an automatic approval, a substitute for your judgment, or proof that a device/image has been qualified.

### 1. Find the target and read the formatted report

Open the report PR and follow **Read the formatted review report** at the top of its description. GitHub renders the Markdown headings, tables and links there. Use **Files changed** when you want to leave a comment on a particular report line.

Confirm:
- The linked **target PR** is the change you intend to review.
- The report's **reviewed head/base commits** match the scope you care about.
- The report is not marked stale or coverage-incomplete.
- Its validation distinguishes executed tests, inert controls, author-reported results and unverified runtime behavior.

A branch-based reading link follows later report edits. Use a commit permalink when referring to a specific historical version.

### 2. Understand the category and recommendation

- **Focused Review:** a directly requested review.
- **Community Service:** a proactive community review.

These labels describe how the review originated, not its quality, urgency or verdict. Repository setup/documentation PRs are not target review reports.

Read the recommendation together with its evidence and scope limits. Source correctness, CI status, dependency deployment and merge readiness are separate questions. A green checker does not prove every finding is fixed; a failed unrelated job is not automatically a code defect.

Check actual coverage. A reused completed panel plus scoped updates is not a fresh panel on every current byte. Missing review roles or unavailable evaluators must remain explicit.

### 3. Discuss findings using stable IDs

Each issue has an ID unique within the report PR, such as **R1**, **N1**, **Q1** or **S1**. Use that ID in a line comment or conversation comment:

> R1: Does this cleanup path also run after a skip?

> N1: The description is already accurate at the linked revision; can we withdraw this nit?

> R2: Could this be deferred if the affected path is explicitly excluded?

Read each finding's:
- Kind and severity: blocking concern, conditional concern, nit, question or optional suggestion.
- Current disposition: open, fixed, deferred, withdrawn or unresolved.
- Immutable source anchor and relevant caller.
- Condition and additional consequence attributable to the change.
- Evidence and supported-platform assumptions.
- Existing target discussion and author reply.

Challenge the analysis when an assumption, severity or reproduction is wrong. Include a source link, counterexample, test result or supported-scope explanation where possible. A request for clarification should not be mistaken for an instruction to make an unrelated implementation change.

### 4. Review author replies and revisions

The maintainer watches target commits and author responses, as well as questions on the report PR. When new evidence changes a conclusion, the report is revised with a dated entry identifying the response, target commit and reason.

IDs remain stable. Original findings, withdrawals and accepted deferrals remain accessible through the report and commit/discussion history. A discussion being marked resolved is not, by itself, proof that code changed or that its technical concern was accepted.

If the target head advances, treat the report as stale until the changed scope has been checked. Report-only wording edits do not necessarily require another production-code review. Conversely, an old report's successful tests do not qualify a new implementation automatically.

### 5. Use the human-operated action page

The report PR description and its **Reader actions** section link to a page named for the target repository and PR. Each report has its own page and drafts.

When blockers remain, the page offers:
1. A request-changes draft.
2. A question-comment draft without a formal verdict.

When no blockers remain, it offers:
1. A comment draft without approval.
2. An approval-with-comment draft.

On the page:
1. Check the target revision, report backlink and existing discussion.
2. Read and edit the draft to reflect your own judgment.
3. Select **Copy draft and open GitHub**.
4. Paste into the target PR. For a formal review, select **Review changes** and the intended verdict.
5. Review the final text and submit using your own signed-in account and repository permissions.

The page does not log you in, request a token, post automatically, choose a verdict on your behalf or merge anything. If clipboard access is unavailable, copy the selected text manually. Opening a page is not evidence of a submitted review.

Avoid duplicate feedback. If a target thread already raises the same concern, respond there or reference it rather than present the issue as newly discovered. Keep the report backlink so readers can inspect the reasoning and evidence limits. Do not claim another person's acceptance or use an attribution that does not reflect your review.

### 6. Distinguish reviewing the report from reviewing the target

Comments and reviews on the report PR discuss the analysis. A formal review submitted to the target PR expresses your judgment about the implementation. Do not assume one is automatically copied to the other.

Authors cannot formally approve their own GitHub PRs. Other reviewers may review the report normally. The target repository determines who can submit qualifying reviews and which checks/approvals are required.

A favorable report does not override an outstanding human objection, deployment requirement or repository protection rule. Resolve the relevant agreement or evidence question before treating the target as ready to land.

### 7. After the target merges or closes

The report remains open while the target is being worked on. Once the target is merged or closed, the maintainer records its terminal outcome and the final disposition of findings, then archives the report through the report repository's normal review process.

The Markdown report, report PR discussion and commit history remain available. Its temporary action page is removed from the published site because active feedback drafts are no longer needed. Other open reports' pages remain available.

Use the archived reading link for the permanent report. Old action-page links may stop working. A closed or withdrawn target does not mean all findings were fixed; the archive should preserve that distinction.

### What to expect from this pilot

Reports and the site are evolving. Check the PR description for actual publication, coverage and monitoring status. If a link is wrong, a report appears stale or a question has not been addressed, leave a precise comment on the relevant report PR. Do not assume a scheduled monitor has run unless an observation or update is recorded.

## Report labels

Labels distinguish review origin, current workflow state, and verified feedback. A label is not an automatic target verdict or permission to merge.

### Category
- **Focused Review:** directly requested review.
- **Community Service:** proactive community-service review.

Keep one category per report. Metadata and documentation PRs are not target reports.

### Workflow state
Keep exactly one current state on each report PR; preserve the detailed reason in its body.

| Label | Meaning |
|---|---|
| Awaiting Reviewer | Report ready for human review. |
| Needs Report Update | Target revision or new evidence needs reconciliation. |
| Waiting Author Response | Feedback submitted; waiting for explanation or correction. |
| Waiting CI | Source review cleared; remaining CI readiness gate. |
| Waiting External Review | External reviewer agreement or repository landing decision remains; the body identifies the gate. |
| Ready to Archive | Target terminal; report archival and page/branch cleanup are due. |
| Archived | Report archived and its action page/branch cleanup verified. |

### Verified target feedback
These describe feedback submitted through the report maintainer's account, not merely drafted recommendations or another reviewer's approval.

- **Target Approved:** verified APPROVED review submitted to the target.
- **Target Changes Requested:** verified REQUEST_CHANGES review submitted to the target.
- **Target Commented:** verified comment-only target feedback.
- **Merged Without Our Approval:** the target merged without a verified approval from the maintainer's account before landing. This does not prove the report was ignored or unused; comments and other reviewers may still have informed the decision.

### Attention
- **Blocking Findings:** confirmed blocking findings in the currently reviewed scope.
- **Coverage Incomplete:** required review coverage is missing or partial.

Stale historical findings are not automatically current blockers. Categories do not change when states change. Monitoring removes superseded state labels and preserves unrelated labels.

### Historical archival

New actionable report intake normally excludes already-terminal targets. An existing historical report can be explicitly retained and merged as an archive, with no live target-action page. The original reasoning, previous closure/reopening decisions and terminal outcome remain recorded; archival does not certify every finding was fixed.
