---
name: slice
description: Scope a GitHub issue to one PR — file a slice spec, peel leftover work onto a new issue, then close the original pointing at both. Use to slice an issue before implement.
disable-model-invocation: true
---

Requires a GitHub issue. If the caller did not pass one, ask and stop. Never implement.

Fetch the issue.

# Size

One issue is one PR: small enough for one agent session to hold the spec and later task coordination; shippable on its own; testable on its own. Work that exceeds any of these is more than one PR can hold. The rule measures; it does not decide: no issue is created and no original is closed on this rule's authority alone.

# Ask before splitting

An oversized request has two shapes — a slice plus a tail, or the whole request in one PR — and only the user picks between them. Before creating any issue, show both: slice 1's proposed scope with the bullets that stay out, versus everything in one PR. Recommend the split and say why; an open question that names no options and no recommendation is not this ask. Follow the answer as settled: accept → the tail below may be filed; whole request in one PR → slice 1 is the entire request and there is no tail; a split of the user's own → that split.

# Slice issue

Review for inconsistencies and unresolved ambiguity. Don't guess: read the code to confirm, or ask the user when the code can't settle a product choice. Technical facts go in Design. Pre-write research does not replace this pass.

Create a **new** issue that *is* this PR. Narrow the title if needed. Keep the relevant metadata from the old issue (tags, assignees, etc), and add the "slice" tag (create if needed). Body:

```markdown
## Goal
## Success Criteria
## Out of Scope
## Design
```

Keep it high-level and unambiguous. Success Criteria must be falsifiable. Out of Scope is drive-by and proximity work a later implementer could take for its own job — not the rest of the original request (that is the tail). Design is approach and decisions — not file paths or type dumps.

The ticket is self-contained: fold every decision made in this session (including per-item or case-by-case rules) into Goal, Success Criteria, Out of Scope, or Design. A fresh session with no conversation history must be able to implement it without guessing. Do not paste conversational transcripts, but never omit agreed choices to keep the ticket short.

Do not write a task list.

The original issue remains the request. The slice spec is not written onto it.

# Peel the tail

If the user accepted the split and anything from the original request does not fit slice 1, create **one** new issue (not a spec, just a problem statement). Put every leftover bullet on that one issue. First line of the body: `Cut when scoping #<slice-issue>.` No parent, no blocked-by, no `Fixes` links.

Keep the relevant metadata from the original issue (tags, assignees, etc), and add the "tail" tag (create if needed).

If there is no tail, do not create an issue.

# Close the original

Close the original only after the slice issue exists, and after the leftover issue exists when there is a tail. Close as not planned. The close comment names each successor by role: `Slice to implement: #<slice>.` and, if a tail was filed, `Leftover: #<tail>.`

A close comment that omits the leftover while a tail exists is incomplete — file the leftover first.

# Stop

Report the slice issue URL, the remainder issue URL if you created one, and that the original is closed. Do not branch, implement, or open a PR.
