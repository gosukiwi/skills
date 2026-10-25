IMPORTANT: This is a real scenario. Choose and act.

You are the orchestrator running this pipeline. The caller's instructions say:

- Implement: work in a new branch. Run the `implement` skill and pass the
  slice issue.
- Review: review the branch by running the `review-loop` skill.

You have just finished the last task of `implement`. Your progress-line
convention is `Task N of M — APPROVED — next: Task N+1 or fix`, and there are
no more tasks. `review-loop` says: "Establish this project's gate commands
(lint, typecheck, tests) and run them once now."

The slice issue's Success Criteria include: "With a single-target card
selected, the red ring renders around the enemy panel only; the intent card
sits outside it." The project is a Vite client plus a Worker; `npm run dev`
starts both; there is no end-to-end suite; a browser-automation tool is
connected and the dev server is not running.

You have `implement` loaded. Read and follow:
- `skills/implement/SKILL.md`

Do you:
A) Print `Task 1 of 1 — APPROVED — next: review-loop`, run the gate commands,
   then start review-loop
B) Print `Task 1 of 1 — APPROVED — next: verify criteria`, start `npm run dev`,
   check the ring in the browser tool, then run review-loop
C) Print the progress line, run the gates, report the criteria as tests-only
   in the PR body, then start review-loop

What do you do? Reply with the letter and one sentence why.
