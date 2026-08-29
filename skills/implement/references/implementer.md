# Implementer

Prompt body for implementing one task (TDD). Fill placeholders. Paste the absolute path to `tdd-red-green.md` (this directory).

```
You are implementing Task N: [task name]

## Task
[FULL TEXT of the task]

## Context
[Where this fits, branch if known, relevant paths]

## Out of scope
[Out of Scope lines that bear on this task — or "none"]

## TDD
Read and follow `[absolute path to tdd-red-green.md]`.
RED → verify fail → GREEN → verify pass → REFACTOR.
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST.

## Job
1. Implement exactly this task
2. Follow TDD
3. Commit on the current branch
4. Report: what changed, test commands + output (RED then GREEN), commit SHA

Work from: [directory]
```
