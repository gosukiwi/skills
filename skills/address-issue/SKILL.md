---
name: address-issue
description: Take a GitHub issue from grilling through slice, implementation, review, and PR.
disable-model-invocation: true
---

The user gave you an issue to address. If they haven't, ask for one.

This skill runs other skills. Read `shared/delegation.md` from your skills directory first, and resolve every skill below the way it describes.

# Common Understanding

Read the issue, then run the `grilling` skill.

# Slice

Run the `slice` skill on that issue.

# Implement

Work in a new branch. Run the `implement` skill and pass the slice issue.

# Review

Review the branch by running the `review-loop` skill.

# Open PR

Open a PR that `Fixes` the slice issue. Keep the PR body concise and without jargon, using Simplified Technical English (ASD-STE100).

The PR body must contain:

- A brief summary of what the PR does
- Steps so the user can verify themselves that the issue has been properly addressed, built from the slice issue's Success Criteria
- The remaining review findings as optional fixes, calling out separately anything left unfixed because it needed a rewrite
- A "Merge Danger" section: 1) Is the PR easily reversible? Does it involve expensive migrations? 2) What's the blast radius? If things go wrong, how bad will it be (e.g. total service downtime/boot crash vs isolated feature failure)? Are there deployment prerequisites or configuration dependencies (e.g. new required ENV variables that will crash the server or prevent boot if missing)? 3) Give a verdict on what's the danger of merging this PR and what would be the best way for a human reviewer to handle it
