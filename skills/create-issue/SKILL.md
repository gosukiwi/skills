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

Talk it through with the user in a few rounds at most:

- Restate the problem and why it matters.
- Propose 2–3 approaches with their trade-offs.
- Surface risks and what is out of scope.

Stop once the problem and scope are clear, even if the user wants to keep going. A design choice still open at that point goes into the issue as an open question with your recommendation. Do not settle it here, and do not write your preference as the chosen design.

# Draft

Show the full issue text in chat:

- **Problem** — what is wrong or missing and why it matters, linking the key code or docs
- **Outcome** — what is true when this is done, including limits the user set and what is excluded
- **Open questions** — each with its options, trade-offs, and your recommendation

Create the issue only after the user confirms the draft, even if they asked for an issue earlier. Then give the URL. If they decline, the draft is the result.
