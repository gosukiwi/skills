---
name: address-issue
description: Take a GitHub issue from shared understanding through spec, implementation, review, and PR.
disable-model-invocation: true
---

The user gave you an issue to address. If they haven't, ask for one.

This skill runs other skills. Read `shared/delegation.md` from your skills directory first, and resolve every skill below the way it describes.

# Common Understanding

Read the issue, then run the `grilling` skill. After that's done, suggest to update the issue if you think it's needed.

# Spec and Implement

Work in a new branch. Create a spec by running the `flow-spec` skill, and follow it until the implementation is done.

# Review

Review the branch by running the `review-loop` skill.

# Open PR

Open a PR. Keep the PR body concise and without jargon, using Simplified Technical English (ASD-STE100).

The PR body must contain:

- A summary of what the PR does
- What the most relevant files and changes are
- Steps so the user can verify themselves that the issue has been properly addressed, built from the spec's Success Criteria
- The remaining review findings as optional fixes, calling out separately anything left unfixed because it needed a rewrite
