---
name: review-loop
description: Clear correctness blockers in a loop, then report leftover findings and a refactor review.
disable-model-invocation: true
---

# Review Loop

Use this skill to review the current branch thoroughly, while auto-fixing blocking changes.

If the git tree is not clean (uncommitted changes), warn the user before continuing.

## 1. Correctness Review

Use subagents to run the correctness review. If the `review-bugbot` skill is installed, use that skill for correctness review, otherwise, just do it yourself.

## 2. Loop Fix Blockers

Use subagents to fix the blockers in the correctness review. If the `flow-patch` skill is installed, use that skill, otherwise, just do it yourself.

Run step 1 again, re-reviewing for correctness and fixing blockers until there are no more blockers.

## 3. Refactor Review

Run the `thermo-nuclear-code-quality-review` skill with subagent. Report all findings (remaining correctness non-blocking + thermo nuclear), numbered, prioritized and categorized by "Blocker", "Should-Fix" and "Minor".

When displaying issues, don't use jargon and speak coherently. State them simply and concisely, like one human talking to another.
