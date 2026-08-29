---
name: address-issue
description: Take a GitHub issue from grilling through plan, implementation, review, and PR.
disable-model-invocation: true
---

The user gave you an issue to address. If they haven't, ask for one.

This skill runs other skills. Read `shared/delegation.md` from your skills directory first, and resolve every skill below the way it describes.

# Common Understanding

Read the issue, then run the `grilling` skill.

# Plan

Run the `plan` skill on that issue.

# Implement

Work in a new branch. Run the `implement` skill and pass the issue.

# Review

Review the branch by running the `review-loop` skill.

# Open PR

Open a PR that `Fixes` the issue. Keep the PR body concise and without jargon, using Simplified Technical English (ASD-STE100).

The PR body must contain:

- A summary of what the PR does
- What the most relevant files and changes are
- Steps so the user can verify themselves that the issue has been properly addressed, built from the issue's Success Criteria
- The remaining review findings as optional fixes, calling out separately anything left unfixed because it needed a rewrite
