# Execute loop

Per-task dispatch loop for `implement`. The calling `SKILL.md` says where task text comes from; this file owns the loop itself.

Files in this directory: `implementer.md`, `reviewer.md`, `tdd-red-green.md`, `subagent-model-size.md`. Use those siblings. Paste filled templates only: a subagent gets what you paste and nothing else, so never point it at an issue, a plan file, or chat history.

Before each dispatch, pick a model per `subagent-model-size.md` — smallest capable tier.

Before the first dispatch, post a user-visible progress line: Task 1 of M — starting implementer. Continue; not a pause for OK.

For each task, in order:

1. Note `BASE_SHA` (`git rev-parse HEAD`)
2. Dispatch implementer subagent — paste `implementer.md` (fill placeholders; absolute path to `tdd-red-green.md`)
3. Note `HEAD_SHA`. User-visible progress: Task N of M — implementer done — next: review. Continue; not a pause for OK.
4. Dispatch reviewer subagent — paste `reviewer.md` (fill placeholders)
5. User-visible progress: Task N of M — APPROVED or REJECTED — next: Task N+1 or fix. Continue; not a pause for OK.
6. If REJECTED → fix (subagent) → progress → review again → repeat until APPROVED
7. Only then start Task N+1

## Non-negotiable

Never implement or review in the orchestrator session, no matter who asks. "It's only a few lines" is not an exemption: a change small enough to tempt you into typing it yourself is small enough for a small-tier subagent, and a briefing costing more than the diff is not a reason to skip it.

A green report from the implementer is not review. The reviewer reads the diff.

Do not batch reviews. Task N's review finishes before Task N+1 dispatches.

Every execute starts with a user-visible progress line before the first dispatch (Task 1 of M — starting implementer). Every subagent return has a user-visible progress line before the next dispatch (Task N of M, what finished, what's next). "Don't interrupt," a recap at Verify, and the host UI showing the subagent are not exemptions — the line is how the user keeps place, not a pause for OK.
