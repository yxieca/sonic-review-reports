# Pilot draft-action page

`index.html` is a standalone page with two deep-link fragments:
- `#request-changes`
- `#questions`

The button copies the editable draft and opens the corresponding target GitHub page. The reader still pastes, selects any formal review verdict, and submits using their own account. Clipboard failure leaves the text selected for manual copying. No token, API posting, tracking or automatic review/merge exists.

Proposed hosted URLs (not live until Pages is enabled):
- https://yxieca.github.io/sonic-review-reports/#request-changes
- https://yxieca.github.io/sonic-review-reports/#questions

The pilot can be preview-hosted from the report branch `/docs` without merging the report PR. This requires an explicit GitHub Pages setting change. After a maintainer merges the template/report, the Pages source can be moved to `main` by a separately reviewed setting change.

Draft text is copied from the report's action-drafts file; update both if the human changes issue dispositions. The page shows a pinned reviewed head, not a live freshness assertion. A hash navigation resets the selected draft to its saved text. Hosting must use HTTPS for normal clipboard access.
