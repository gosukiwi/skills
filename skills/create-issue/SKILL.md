---
name: create-issue
description: Explore an idea with the user and draft a GitHub issue ready for address-issue.
disable-model-invocation: true
---

Turn a rough idea into a GitHub issue. If the user gave you no idea, ask for one.

This skill explores; it does not decide. `address-issue` runs `grilling` when the work starts, against the code as it is then. So the issue carries the user's intent and the open questions — not settled decisions.

# Research

Finding facts is your job. Read the code and docs, and search online when it helps. Do not guess. You may run throwaway scripts, but they write only to a temp dir: never change the repo, git state, or anything remote.

# Explore

Build the issue one section per round, in this order. Each round is a few bullets with no preamble; wait for the user's reaction before the next.

1. **Problem** — what is wrong or missing and why it matters, linking the key code or docs.
2. **Outcome** — what is true when this is done, including limits the user set and what is excluded.
3. **Open questions** — each with 2–3 options, their trade-offs, and your recommendation.

Revise a section when the user corrects it, but do not reopen agreed sections. More than about three open questions means the idea is too big for one issue: say so and suggest what to cut.

Stop after these rounds, even if the user wants to keep going. A choice still open goes in as an open question with your recommendation. Do not settle it here, and do not write your preference as the chosen design.

# Draft

Assemble the agreed sections into the full issue text and show it in chat. Create the issue only after the user confirms the draft, even if they asked for an issue earlier. If they decline, the draft is the result.

When creating the issue, look at the existing tags and properly tag this new issue. Then give the URL. 
