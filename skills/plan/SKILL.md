---
name: plan
description: Scope a GitHub issue to one PR — rewrite it to the slice spec and peel leftover work onto a new issue. Use to plan an issue before implement.
disable-model-invocation: true
---

Requires a GitHub issue. If the caller did not pass one, ask and stop. Never implement.

Fetch the issue.

# Size

One issue is one PR: small enough for one agent session to hold the spec and later task coordination; shippable on its own; testable on its own. Work that exceeds any of these is more than one slice — this issue becomes slice 1 only.

# Rewrite this issue

Review for inconsistencies and unresolved ambiguity. Don't guess: read the code to confirm, or ask the user when the code can't settle a product choice. Technical facts go in Design. Pre-write research does not replace this pass.

Replace the issue so it *is* this PR. Narrow the title if needed. Body:

```markdown
## Goal
## Success Criteria
## Out of Scope
## Design
```

Keep it high-level and unambiguous. Success Criteria must be falsifiable. Out of Scope is drive-by and proximity work a later implementer could take for its own job — not the rest of the original request (that is the tail). Design is approach and decisions — not file paths or type dumps.

Fold decisions already made in this session into Goal, Success Criteria, Out of Scope, and Design. Do not paste the conversation.

Do not write a task list.

# Peel the tail

If anything from the original request does not fit slice 1, create **one** new issue (not a spec, just a problem statement). Put every leftover bullet on that one issue. First line of the body: `Cut when scoping #<this-issue>.` No parent, no blocked-by, no `Fixes` links.

If there is no tail, do not create an issue.

# Stop

Report the slice issue URL, and the remainder issue URL if you created one. Do not branch, implement, or open a PR.
