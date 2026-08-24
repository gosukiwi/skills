---
name: pr-stabilization
description: Use before requesting human review or marking a PR "ready" — runs adversarial red/blue self-review cycles until only nits remain, backed by green gates and fail-on-base tests. Invoke after writing a change and before pushing for peer review, or when the user says "stabilize this PR" / "self-review before review".
disable-model-invocation: true
---

# PR Stabilization & Self-Review

Stabilize a change through adversarial self-review **before** a human sees it. A one-off / zero-shot push is the failure mode: it makes reviewers hunt trivial bugs the author could have caught. Treat the first draft as **confident but likely flawed** — a base, not the final product.

Goal: by the time a human reviews, the only open items are nits (cosmetic / stylistic / inconsequential). Human review time is for architecture and trade-offs, not bug-hunting.

## The loop

Repeat **Red → Blue → Prove** until the termination bar is met.

### 1. Red team — isolated reviewer
Attack the code from a fresh perspective. **Run this as a subagent (e.g. a dedicated review agent), not in the authoring context** — the author-context already believes the code is correct and reads its intent into it, so it rationalizes instead of finding bugs.
- Give the reviewer only the **diff + requirements**, NOT your reasoning for why it's correct.
- Use a neutral/adversarial prompt: *"assume this is flawed, find what's wrong."* Never *"review this code I'm confident in"* — that re-injects the bias.
- Rotate the lens each round rather than repeating one: **correctness / edge cases → security & authorization → scale (does it hold at production data volume?) → cross-surface consistency ("did I fix EVERY instance of this bug, not just the first?") → do the tests actually prove anything?**
- For larger changes, fan out several reviewers in parallel, one lens each.

### 2. Blue team — fixer, in the main context
Fix what the red team found, in the authoring context (it needs the full picture to fix the cause, not silence the symptom).
- Treat findings as **input to verify, not gospel** — some are wrong; push back on those with reasoning rather than performing agreement.
- Keep related fixes coherent.

### 3. Prove — evidence, not assertion
Before believing anything is fixed, run the real checks:
- Linter, type/compile check, the relevant tests, CI.
- **Fail-on-base rule (hard):** every new regression test must be demonstrated to fail on the pre-fix code. A test that passes either way proves nothing.
- For high-stakes correctness/security findings, add a **refute-first adversarial-verify** subagent whose job is to try to disprove the finding.

## Termination bar

Stop **only** when BOTH hold:
1. A fresh adversarial pass surfaces **only nits** (nothing affecting how it works), AND
2. The gates are **actually green** (lint, build/typecheck, tests, CI).

The iteration *count* is not the target — the clean bar is. A few rounds is typical; treat ~5 as a ceiling for substantial work. **Do not request human review while any functional or architectural issue remains.**

## Scope discipline

Red team will surface pre-existing, unrelated issues. Sort them:
- Caused or amplified by this change → **fix now**.
- Genuinely pre-existing and unrelated → **file a follow-up issue**; don't scope-creep this change.

## Keep the loop local

Do **not** post each red-team round as a PR comment — that's noise and defeats the purpose of reducing reviewer burden. The PR receives the **hardened result + one concise summary** at "ready for review." Commit history is the traceability.

## Scale rigor to the change

- Trivial mechanical edit (a one-liner) → a single fresh-eyes pass; skip the full fan-out.
- New feature / security surface / DB migration → the full loop: parallel diverse reviewers + adversarial verify, favor thoroughness over speed.

## Provenance

Formalizes an established PR-stabilization practice (red/blue cycles until only inconsequential minors remain), with refinements: terminate on evidence rather than a fixed cycle count; make fail-on-base a hard test rule; isolate the reviewer but keep the fixer in the main context; keep the loop off the PR.
