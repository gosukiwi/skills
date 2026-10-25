---
name: yolo-issues
description: Address a set of GitHub issues unattended onto one review branch, then open a single PR. Accept every recommended answer.
disable-model-invocation: true
---

The user gave you a set of issues. If they haven't, ask for one. If they said all, take the open issues.

This skill runs other skills. Read `../shared/delegation.md` — relative to this skill's folder — before any other step, and resolve every skill below the way it describes. It is required, not a lookup aid: if the file is missing, stop and tell the user. Do not hunt for another copy, and do not start the work without it.

# Questions

Read every issue in the set before you start. If something genuinely blocks the work — an issue you cannot fetch, an ambiguous set, a decision no recommendation can settle — ask it all in one round now, numbered, and wait once for the answers. Expect to need nothing.

That single round is the only time you ask. Fold the answers in as settled decisions. After it, never ask again and never wait for the user.

# Auto-answer

Run every step of the flow, including `grilling`, but you also play the user: whenever any skill asks a question, answer with its recommended option and continue. Grill for as many rounds as the frontier needs, accepting every recommendation, then treat the shared understanding as confirmed.

# Review branch

Before you start, create `yolo/batch-<short-description>` from an up-to-date `main` (add a suffix if the name is taken) and push it. For `<short-description>`, write a few kebab-case words summarizing the set, such as `yolo/batch-fix-auth-redirects`. Nothing goes into `main` during this run.

# Loop

Address the issues one at a time, in the order given. For each, run the `address-issue` skill end to end, with that issue as the one it was given. Follow it exactly, including its delegation — no production code in this session.

Two overrides, so the work stays off `main`:

- Cut the issue's branch from the review branch, never from `main`.
- Open its PR against the review branch.

# Merge

Merge each PR into the review branch as soon as it opens and its required checks pass, using the repo's usual merge method (squash when unsure), then delete the issue branch. Keep your local copy of the review branch in sync after each merge; the next issue starts from it.

# Final PR

When the set is done, run the repo's full gate on the review branch. If two issues broke each other, dispatch an implementer to fix only that, then run the gate again. If it still fails, stop and report.

Open one PR from the review branch into `main`. Its body starts from `address-issue`'s PR body, plus:

- It lists every addressed issue — original and slice — with its per-issue PR.
- It has one `Fixes #<n>` line per slice issue. Their per-issue PRs targeted the review branch, so they did not close on merge.
- Verification steps for the whole batch, built from the slice issues' Success Criteria.
- The remaining review findings from all per-issue PRs.

Do not merge the final PR. The user tests and reviews it.

# Stop

Report one line per issue: the issue, its per-issue PR, and the merge into the review branch. Then give the review branch name and the final PR URL.

If a PR cannot merge into the review branch — failing checks, conflicts, a branch you cannot update — stop and report it. Do not leave it behind and move on.
