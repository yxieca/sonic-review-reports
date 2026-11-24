# Editable target feedback drafts

Report PR: https://github.com/yxieca/sonic-review-reports/pull/10
Target: https://github.com/sonic-net/sonic-platform-daemons/pull/923
Reviewed head: `ea5e907b411a882410f06a31e3fb5fc1c219e22a`

## comment

```text
AI-assisted review report: https://github.com/yxieca/sonic-review-reports/pull/10

Source acceptable; no new demonstrated code blocker. Existing human startup/guard objection remains; publication does not release it.

/ actual redesign versus historical review
- Critical triggers configured graceful_shutdown now dispatch direct power_off, not old JOIN/rank lending. Three FIFO lanes serve power_off, graceful_shutdown, then raises; no BUSY/JOIN or per-action workers.
- Main thread owns platform power and HOST_STATE records; only gNOI/local link reads use the bounded helper. Queued higher-priority requests cancel waits, not indivisible native platform calls.
- Fresh leak gate immediately precedes every raise. Raise bookkeeping fails closed; removals proceed despite bookkeeping failures. Stable power labels require observed confirmation; interrupted/unconfirmed calls retain uncertainty.
- Graceful report attribution and physical power removal remain distinct. A confirmed host HALT is not proof power was removed; removal failure reports POWER_OFF_FAILED.
- Startup reconciles abandoned records/RM rows, preserves uncertain OFFLINE labels and runs startup power-on as a recorded/preemptible in-place operation. Current source retains base startup check order; it is not the earlier queued helper design named in an older author reply.

Reviewed target revision: ea5e907b411a882410f06a31e3fb5fc1c219e22a. Retained source review and bounded validation were reused, not rerun. No independent hardware qualification is claimed.

Existing human startup/guard objections must remain open until the reviewer agrees; this draft does not override them.

Any submission reflects the reader’s own review and judgment; this comment is not an approval.
```

## approve

```text
AI-assisted review report: https://github.com/yxieca/sonic-review-reports/pull/10

Source acceptable; no new demonstrated code blocker. Existing human startup/guard objection remains; publication does not release it.

/ actual redesign versus historical review
- Critical triggers configured graceful_shutdown now dispatch direct power_off, not old JOIN/rank lending. Three FIFO lanes serve power_off, graceful_shutdown, then raises; no BUSY/JOIN or per-action workers.
- Main thread owns platform power and HOST_STATE records; only gNOI/local link reads use the bounded helper. Queued higher-priority requests cancel waits, not indivisible native platform calls.
- Fresh leak gate immediately precedes every raise. Raise bookkeeping fails closed; removals proceed despite bookkeeping failures. Stable power labels require observed confirmation; interrupted/unconfirmed calls retain uncertainty.
- Graceful report attribution and physical power removal remain distinct. A confirmed host HALT is not proof power was removed; removal failure reports POWER_OFF_FAILED.
- Startup reconciles abandoned records/RM rows, preserves uncertain OFFLINE labels and runs startup power-on as a recorded/preemptible in-place operation. Current source retains base startup check order; it is not the earlier queued helper design named in an older author reply.

Reviewed target revision: ea5e907b411a882410f06a31e3fb5fc1c219e22a. Retained source review and bounded validation were reused, not rerun. No independent hardware qualification is claimed.

Existing human startup/guard objections must remain open until the reviewer agrees; this draft does not override them.

Any approval must reflect the submitting reviewer’s own judgment and permissions; this saved draft is not a claim that anyone has approved it.
```
