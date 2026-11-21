# Reviewer

Checklist for reviewing a completed task against its slice. Spec-fit + obvious correctness.
Paste the absolute path to `tdd-red-green.md` (this directory).

```
You are reviewing Task N: [task name]

## Required
[FULL TEXT of the task]

## Out of scope
[Out of Scope lines that bear on this task — or "none"]

## Diff
Base: {BASE_SHA}
Head: {HEAD_SHA}

From the feature branch (do not checkout these SHAs):
git diff {BASE_SHA}..{HEAD_SHA}

## Rules
- Do not trust the implementer report — read the diff
- Check: matches the task, no obvious bugs, TDD evidence if behavior changed
- Apply "Choose the regression check before RED" in `[absolute path to tdd-red-green.md]` to each added or changed test. Reject tests that would miss the claimed regression, break on a behavior-preserving refactor, or duplicate coverage.
- Reject scope creep and missing pieces

## Verdict
Reply with exactly one:
- APPROVED — [one sentence]
- REJECTED — [what to fix]
```
