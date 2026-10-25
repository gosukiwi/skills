---
name: implement
description: Break a scope into TDD tasks and implement with subagent review. Pass a GitHub issue (read-only) or an ad-hoc brief.
disable-model-invocation: true
---

Orchestrator only: **subagents** implement. No production code in this session. Never write GitHub issues. Never wait for OK. Never create a branch. Never open a PR.

# Scope

- **Issue** (number or URL) — That body is source of truth. Do not trust chat over it. If fetch fails, stop.
- **Ad-hoc brief** — The pasted text is the scope. Do not fetch or infer an issue.

If neither was passed, ask and stop.

# Tasks

Read `references/tdd-red-green.md`. Break the scope into sequential tasks a subagent can finish alone. Structure each as RED → GREEN where a test makes sense. A task list has no unresolved alternatives — paths, names, commit splits, or hedge phrases (`or`, `either`, `equivalent`, `prefer X if Y`, "implementer decides"). Unsettled → read the code. Don't guess.

Review the tasks against the codebase: match existing conventions, confirm APIs/helpers exist.

Print the task breakdown, then execute immediately.

# Execute

Follow `references/execute-loop.md`. Task text comes from the breakdown you just wrote — paste it into the prompt; do not tell subagents to read the issue or chat history.

# Verify

Run the project's usual checks — tests, lint, typecheck, formatters, build — whichever exist.

Then prove the scope's Success Criteria that a user can observe, by doing what a user does. Run the project's own user-level harness if it has one — a verification skill or an end-to-end suite. Otherwise drive the running app with a connected browser-automation tool for web surfaces, or plain HTTP / a PTY for services and CLIs. Capture the evidence — screenshot, transcript, response body — and keep it after teardown.

The action and what you observe must both be open to a user. Internal setters, test-only endpoints, and modes that disable the behavior prove nothing, however the repo documents them. A green suite is not live proof, however tightly its assertions map to the criteria. A missing browser tool changes how you drive the app, not whether you do.

Verify writes no tests or driver scripts. A behavior that deserves a permanent check was a task that got missed — report it, do not add it here. Do not fix what you find either.

Report each criterion as proven live, proven by tests only, or not observable here, with the reason. Then stop — the caller owns review, PR, merge, and push.
