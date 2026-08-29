---
name: plan
description: Scope a GitHub issue to one PR — rewrite it to the slice spec and peel leftover work onto one bookmark issue. Use after grilling, from address-issue, or to plan an issue before implement. Never implements.
disable-model-invocation: true
---

Requires a GitHub issue. If the caller did not pass one, ask and stop. Never implement. Never wait for OK.

Fetch the issue (`gh issue view`). Session context (grilling, the talk) may inform the slice; the write goes to GitHub.

# Size

One issue is one PR: small enough for one agent session to hold the spec and later task coordination; shippable on its own; testable on its own. Work that exceeds any of these is more than one slice — this issue becomes slice 1 only.

# Rewrite this issue

Replace the issue so it *is* this PR. Narrow the title if needed. Body:

```markdown
## Goal
## Success Criteria
## Out of Scope
```

Keep it high-level and unambiguous. Success Criteria must be falsifiable. Out of Scope is drive-by and proximity work a later implementer could take for its own job — not the rest of the original request (that is the tail).

Do not write a task list.

# Peel the tail

If anything from the original request does not fit slice 1, create **one** new issue (bookmark quality, not a spec). Put every leftover bullet on that one issue. First line of the body: `Cut when scoping #<this-issue>.` No parent, no blocked-by, no `Fixes` links.

If there is no tail, do not create an issue.

# Stop

Report the slice issue URL, and the remainder issue URL if you created one. Do not branch, implement, or open a PR.
