---
name: address-issue
description: Addresses a GitHub issue
disable-model-invocation: true
---

The user gave you an issue to address. If they haven't, ask for one.

# Common Understanding

The first step is to read the issue. If there's something that's not clear, use the `grilling` skill to reach a common understanding on the issue. After that's done, suggest to update the issue if you think it's needed.

# Spec and Implement

Work in a new branch. Create a spec using `flow-spec`, follow the skill until the implementation is done.

# Review

Review the branch using the `pr-stabilization` skill. Once that's done, run the `thermo-nuclear-code-quality-review` skill using a subagent. The thermo nuclear review tends to over-report so re-classify the findings into Blocker, Should-Fix, and Nit. Address Blockers + Should-Fix.

# Open PR

Open a PR and include all the remaining findings as optional fixes (from `pr-stabilization` and `thermo-nuclear-code-quality-review`). Include steps so the user can verify themselves that the issue has been properly addressed.
