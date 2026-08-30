---
name: plan
description: Scope one PR from a GitHub issue or this session — open a GitHub issue for that PR, and a leftover issue if needed.
disable-model-invocation: true
---

Never implement.

# Request

The original request is one of:

- **Issue** (number or URL) — Fetch it. That body is the request.
- **This session** — No issue. The request is the work just settled (last interview or last stated intent), not the whole transcript. File in this working tree (`gh` default). If `gh` cannot resolve a repo, ask and stop.

If there is no issue and no identifiable request, ask what to plan, then stop. Do not ask for a ticket number. Do not start an interview.

# Size

One issue is one PR: small enough for one agent session to hold the spec and later task coordination; shippable on its own; testable on its own. Work that exceeds any of these is more than one slice — slice 1 is a new issue.

# Slice issue

Review for inconsistencies and unresolved ambiguity. Don't guess: read the code to confirm, or ask the user when the code can't settle a product choice. Technical facts go in Design. Pre-write research does not replace this pass.

Create a **new** issue that *is* this PR. Narrow the title if needed. Body:

```markdown
## Goal
## Success Criteria
## Out of Scope
## Design
```

Keep it high-level and unambiguous. Success Criteria must be falsifiable. Out of Scope is drive-by and proximity work a later implementer could take for its own job — not the rest of the original request (that is the tail). Design is approach and decisions — not file paths or type dumps.

Fold decisions already made in this session into Goal, Success Criteria, Out of Scope, and Design. Do not paste the conversation.

Do not write a task list.

When the request was a GitHub issue, that issue remains the request. The slice spec is not written onto it.

When the request was this session, there is no request ticket — only the slice (and leftover, if any).

# Peel the tail

If anything from the original request does not fit slice 1, create **one** new issue (not a spec, just a problem statement). Put every leftover bullet on that one issue. First line of the body: `Cut when scoping #<slice-issue>.` No parent, no blocked-by, no `Fixes` links.

If there is no tail, do not create an issue.

# Close the original

If the request was this session, do not close anything.

If the request was a GitHub issue: close the original only after the slice issue exists, and after the leftover issue exists when there is a tail. Close as not planned. The close comment names each successor by role: `Slice to implement: #<slice>.` and, if a tail was filed, `Leftover: #<tail>.`

A close comment that omits the leftover while a tail exists is incomplete — file the leftover first.

# Stop

Report the slice issue URL and the remainder issue URL if you created one. If the request was a GitHub issue, report that the original is closed. Do not branch, implement, or open a PR.
