---
name: review-pr
description: Verify a GitHub PR, run parallel correctness and maintainability reviews, re-classify findings, and post a confirmed plain-language review.
disable-model-invocation: true
---

# Review PR

Review a GitHub PR without changing it: never edit code, commit, or push to the PR branch.

The user gave you a GitHub PR (number or URL). If they haven't, ask for one and stop.

This skill runs other skills. Read `shared/delegation.md` from your skills directory (such as `~/.gemini/antigravity-cli/skills/`, `~/.agents/skills/`, `~/.claude/skills/`, or `.agents/skills/`) first, and resolve every skill below the way it describes.

## 1. Temp Worktree & Context

Fetch the PR metadata (title, body, author, base/head refs, linked issue if any) and diff with `gh pr view` and `gh pr diff`.

Check out the PR head into a temporary detached git worktree (for example, fetch `pull/<n>/head` and `git worktree add --detach`) so your current branch and uncommitted files stay untouched. Remove the temporary worktree when finished.

## 2. Verify

Run verification inside the temporary worktree. Green CI on GitHub is not a substitute for local verification.

- Run the repo's checks (tests, lint, typecheck, formatters, build).
- When the PR adds or changes user-observable behavior (UI, HTTP service, CLI, or linked Success Criteria), prove it by driving the app the way a user would — using the project's documented verification path if one exists, else a connected browser tool for web, plain HTTP for services, or a CLI/PTY invocation. Do not rely on internal test-only hooks that bypass the real path. Skip live driving for pure docs, internal refactors, or test-only PRs.
- Record any failed check or unverified behavior; never fix code, add tests, or write driver scripts.

## 3. Parallel Reviews

Run `correctness-review` and `thermo-nuclear-code-quality-review` **in parallel** in separate subagents (both `large` tier per `shared/subagent-model-size.md`). Pass each subagent its resolved `SKILL.md` path, the PR intent (title, body, linked issue), and the PR diff (from the temporary worktree). Scope `thermo-nuclear-code-quality-review` strictly to what this PR introduced or made worse — not the surrounding codebase.

## 4. Re-classify

`thermo-nuclear-code-quality-review` over-reports, so re-classify its findings by what each problem costs later:

- **Blocker** if future edits here will likely introduce bugs or new code will copy the pattern.
- **Should-Fix** if it is real drag that gets more expensive with time.
- **Nit** otherwise.

Merge in any failed verification checks or failed live behavior as **Blockers**.

## 5. Propose & Confirm

Choose the default recommended review action:

- **Approve** — no remaining findings and verification passed.
- **Request changes** — at least one **Blocker**.
- **Comment** — only **Should-Fix** or **Nit** findings (or when the PR author is you, since GitHub disallows approving or requesting changes on your own PR).

Draft a single top-level review body (no inline diff comments). Write it simply, concisely, and without jargon — like one human talking to another. Mention what you verified only when something failed or could not be run, or when it adds needed context.

Show the proposed action and the full review draft to the user and **wait for confirmation** before posting anything to GitHub. Never post without explicit approval.

Once confirmed (with any edits or action override), post the top-level review with `gh pr review` and remove the temporary worktree.
