---
name: architecture-review
description: Propose a better software design for a named module, subsystem, or concept — current homes versus proposed homes, what moves, and why the next similar change is cheaper. Use when the user wants an architecture or design pass. Not a code review, correctness review, or implementation.
disable-model-invocation: true
---

# Architecture Review

Requires a named area: a module, subsystem, or concept. If the caller did not pass one, ask and stop. Never implement.

If the named area is too big to hold one design, cut to the one concept whose missing or cramped home is costing the most, and say that's the cut.

# Job

Propose a better **place** for the concept. Ignore correctness, style, naming-as-taste, and local cleanup.

A one-off that works for a single instance is not a design. The test: when the next similar thing shows up, does it have a home, or does someone bolt on another special case?

Authorization as a single `if` in a handler is a one-off. A `policies/` module — role + action in, allow/deny out — is a home. Propose the second shape, not a cleaner `if`.

# Current

Read enough to see where the concept lives today. Do not audit lines.

A review that names a home has counted the callers of the concept. Search for the name they go through, and give the report that count and the name you searched for. A project document tells you what its author meant; only the call sites tell you what is true today. This count is not a line audit and not a catalog of nits: it is a list of modules, and the design rests on it.

A home that fits three callers and forces the fourth is not one home. When a caller wants something different from the rest, the report says so.

# Proposed

One design. A second only if another home is genuinely close.

What moves is modules and responsibilities, not functions. Callers that do not care about the new instance should not have to change.

A move keeps the behavior unless you say it does not. If the move changes what the code does, name the behavior and who sees it. If it keeps the behavior, say so in one clause. Do not list the work as a cost: that the move takes edits and tests is not news.

# Output

Avoid jargon and use Simplified Technical English (ASD-STE100).

```markdown
## Current
Where it lives, and every caller you found. Why the next instance is expensive.

## Proposed
The home. What moves. What behavior changes, if any. Why the next instance is cheaper.
```

If a second home was close, add `## Also considered` with why not.

No code. No patches. No `file:line` notes. No catalog of nits. Name each caller by its module.

# Stop

Report the design. Do not branch, implement, or open a PR.
