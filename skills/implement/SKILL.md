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

Prove each user-observable Success Criterion by driving the app the way a user would. Start it if it isn't running. Use the project's own way in if it documents one — a verification skill, a dev or serve command, an e2e suite — else a connected browser tool for web, plain HTTP for services, or a PTY for CLIs. Capture the evidence — screenshot, transcript, response body — and keep it.

The check commands are not this step. Internal setters, test-only endpoints, and modes that disable the behavior prove nothing, even when documented, and a green suite is not live proof.

Then run the usual checks — tests, lint, typecheck, formatters, build.

Before handing back, print one line per criterion: `VERIFY <criterion>: live — <evidence>` or `VERIFY <criterion>: tests-only — <what stopped you from driving it>`. Hand back only when every user-observable criterion has a line. Report, do not fix: no new tests or driver scripts; a behavior that deserves a permanent check was a missed task. The caller owns review, PR, merge, and push.
