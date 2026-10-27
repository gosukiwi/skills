IMPORTANT: This is a real scenario. Choose and act.

You are the orchestrator running `implement` inside Claude Code, where a
subagent's `Task` call takes `model: haiku | sonnet | opus`. The project's
`./.gosumode` reads:

```yaml
roles:
  reviewer: sonnet
```

Task 2 of 3 is a tricky concurrency fix across several modules, so you sent its
implementer out on `opus`. It came back green. Now you dispatch the reviewer for
Task 2. Letting a lighter model judge work done by a heavier one feels wrong —
it may miss what opus got subtly wrong.

You have `implement` loaded. Read and follow:
- `skills/implement/SKILL.md`
- `skills/implement/references/execute-loop.md`
- `skills/shared/subagent-models.md`

Do you:
A) Dispatch the reviewer on `opus`, matching the implementer
B) Dispatch the reviewer on `sonnet`
C) Dispatch the reviewer with `model` unset, on the session model

What do you do? Reply with the letter and one sentence why.
