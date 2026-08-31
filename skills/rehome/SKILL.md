---
name: rehome
description: Propose one better home for a concept — where it lives now, where it should live, what moves. Point it at a concept, a module, a PR, or a whole repo. Not a code review, not an implementation.
disable-model-invocation: true
---

# Rehome

Take any scope: a concept, a module, a PR, or a whole repo. A wide scope is not a reason to ask a question — read it, then cut.

Whatever the scope, the report names one home for one concept. Cut to the concept whose missing or cramped home costs the most, and say that is the cut.

A PR is evidence, not the area: the concept is the one the diff had to touch in several places, or the one it leaves more cramped than it found.

# Job

Propose a better **place** for the concept. Ignore correctness, style, naming-as-taste, and local cleanup.

A one-off that works for a single instance is not a design. The test: when the next similar thing arrives, does it have a home, or does someone bolt on another special case? Authorization as one `if` in a handler is a one-off; a `policies/` module — role and action in, allow or deny out — is a home.

# Current

A report that names a home has counted the callers. Give the count and the name you searched for. A project document tells you what its author meant; only the call sites tell you what is true today. This is a list of modules, not a line audit.

A home that fits three callers and forces the fourth is not one home. Say so when one caller wants something different.

# Proposed

One design. If another home is close, choose between them and report the winner only.

What moves is modules and responsibilities, not functions. Callers that do not care about the new instance should not have to change.

A move keeps the behavior unless you say it does not. Name the behavior that changes and who sees it. Do not count the edits and the test updates as a cost.

# Output

Simplified Technical English (ASD-STE100).

```markdown
## Current
Where it lives, every caller you found, and why the next instance is expensive.

## Proposed
The home. What moves. What behavior changes, if any. Why the next instance is cheaper.
```

No code. No patches. No `file:line` notes. No catalog of nits. No second design. Name each caller by its module.

# Stop

Report the design. Do not branch, implement, or open a PR.
