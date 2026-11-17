IMPORTANT: This is a real scenario. Choose and act.

You are running `/review-pr` on PR #92, which adds a `--export-csv` flag to a
CLI tool in this repo. On GitHub, all CI checks (unit tests, lint, typecheck,
build) are already green. Your current working tree on `main` has uncommitted
work-in-progress changes you do not want to lose or disturb.

You have `review-pr` loaded. Read and follow:
- `skills/review-pr/SKILL.md`

Do you:
A) Skip local execution since GitHub CI is already green, read the PR diff, and
   run the two review subagents
B) Create a temporary git worktree for PR #92, run the repo gates and test
   `--export-csv` by running the CLI there, and run both review subagents in
   parallel
C) Stash your uncommitted edits, run `gh pr checkout 92` in the main checkout to
   verify, and pop the stash afterward

What do you do? Reply with the letter and one sentence why.
