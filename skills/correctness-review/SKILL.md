---
name: correctness-review
description: Review a diff for functional bugs, security, intent fit, and whether tests actually prove the change — not style or architecture. Use when the user asks for a correctness review, or as the correctness pass in review-loop.
disable-model-invocation: true
---

# Correctness Review

Review the change, not the codebase. Ignore style, naming, and structure.

## Setup

Run as a **fresh subagent**. Give it the diff and the stated intent (PR / commit / task). Do **not** pass the author's rationale for why the code is correct.

Assume the change is flawed. Find what is wrong.

## Lenses

1. **Intent** — Does the diff do what was asked? Does the code contradict the PR, commit, or names?
2. **Correctness** — Logic bugs, broken callers, missed states, bad contracts, races. Name the input or caller that breaks.
3. **Security** — Injection, secrets, missing authz, unsafe eval/deser, untrusted input at a boundary.
4. **Every instance** — If this class of bug or fix appears once, did we miss the others?
5. **Proof** — Do tests cover the changed behavior? Would they fail if the bug were still there? Run the obvious targeted tests if a command is clear.

Do not flag issues that need impossible inputs. If something looks intentional but risky, ask — don't assert. Be precise: the bug, the trigger, why it matters.

## Output

Only findings. No fixes. For each finding: `Blocker | Should-Fix | Nit`, `file:line`, and the issue (trigger + why it matters).

- **Blocker** — breaks behavior, corrupts data, is exploitable, silently wrong for existing callers, or an uncovered behavior change when this area already has tests to extend.
- **Should-Fix** — likely bug or likely hole with a plausible production path, or an uncovered behavior change when the area has no suite (don't invent a harness).
- **Nit** — context-dependent or low-probability.

If nothing qualifies, say so in one line. Do not pad with nits.
