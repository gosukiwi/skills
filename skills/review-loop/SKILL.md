---
name: review-loop
description: Fix correctness findings in a loop, then fix the refactor findings worth fixing and report what's left.
disable-model-invocation: true
---

# Review Loop

Use this skill to review the current branch thoroughly, while auto-fixing blocking changes.

This skill runs other skills. Read `shared/delegation.md` from your skills directory first, and resolve every skill below the way it describes.

If the git tree is not clean (uncommitted changes), warn the user before continuing.

Establish this project's gate commands (lint, typecheck, tests) and run them once now. If something is already failing, say what, and treat it as pre-existing.

## 1. Correctness Review

Run the `correctness-review` skill in a subagent to get the correctness findings.

## 2. Loop Fix Findings

Fix the Blockers and Should-Fix findings by running the `implement` skill. Pass those findings as an ad-hoc brief. Do not run `plan`. A regression test has to fail on the pre-fix code, otherwise it proves nothing.

Run step 1 again, re-reviewing for correctness and fixing findings until only Nits remain and the gates are green.

## 3. Refactor Review

Run the `thermo-nuclear-code-quality-review` skill in a subagent, scoped to what this change introduced or made worse — not the surrounding codebase.

It over-reports, so re-classify by what each problem costs later: Blocker if future edits here will likely introduce bugs or new code will copy the pattern, Should-Fix if it's real drag that gets more expensive with time, Nit otherwise.

Address Blockers + Should-Fix via `implement` only where the fix stays contained. Pass those findings as an ad-hoc brief. Do not run `plan`. Report the ones that turn into a rewrite instead. If you changed anything, run step 1 and the gates once more to confirm nothing regressed.

Report all remaining findings (correctness + thermo nuclear), numbered and prioritized.
