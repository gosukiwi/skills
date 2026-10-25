---
name: create-issue
description: Explore an idea with the user and draft a GitHub issue ready for address-issue.
disable-model-invocation: true
---

Turn a rough idea into a GitHub issue. If the user gave you no idea, ask for one.

This skill explores; it does not decide. `address-issue` runs `grilling` when the work starts, against the code as it is then. So the issue carries the user's intent, the choices the user made, and the open questions — never your own preference as a settled decision.

# Research

Finding facts is your job. Read the code and docs, and search online when it helps. Do not guess. You may run throwaway scripts, but they write only to a temp dir: never change the repo, git state, or anything remote.

Search the project's **open** issues before you draft. If one already covers the idea, show it and ask whether to update that issue instead of filing a new one. A confirmed draft is not permission to file a duplicate: create nothing until the user chooses. If they choose the existing issue, update it with the agreed sections and create nothing.

# Explore

Build the issue one section per round, in this order. Each round is a short numbered list with no preamble, so the user can reference an item by number; wait for the user's reaction before the next.

1. **Problem** — what is wrong or missing and why it matters, linking the key code or docs.
2. **Solution** — what is true when this is done, including limits the user set and what is excluded.
3. **Open questions** — each with 2–3 options, their trade-offs, and your recommendation.

Revise a section when the user corrects it, but do not reopen agreed sections. More than about three open questions means the idea is too big for one issue: say so and suggest what to cut.

Stop after these rounds, even if the user wants to keep going. A choice still open goes in as an open question with your recommendation. Do not settle it here, and do not write your preference as the chosen design.

# Draft

Assemble the agreed sections into the full issue text and show it in chat. Each question the user answered becomes one line under **Decisions**, stating only what was chosen — no rejected options, trade-offs, or option letters. Only questions the user left unanswered stay under **Open questions** with their options and your recommendation. Omit a section that would be empty.

Create the issue only after the user confirms the draft, even if they asked for an issue earlier. If they decline, the draft is the result.

When creating the issue, look at the existing tags and properly tag this new issue.

After creating it, check the other open issues it touches: a tracking issue that should list it, one it overlaps, one it supersedes. List each with the exact edit — a cross-reference, a checklist entry, a close pointing at the new issue. Apply only the edits the user confirms; leave every other issue untouched. The URL alone is not done: give it with the proposed edits.
