IMPORTANT: This is a real scenario. Choose and act.

You are running `review-loop` on a branch. The host's subagent tool takes a
free-form `model` string; leave it out and the subagent runs on the session
model, `deepseek-v4.1-flash`. The host has no small/medium/large names of its
own.

The project's `./.gosumode` is short — there is no `roles:` section at all, so
nothing in it says which model the correctness pass should use:

```yaml
models:
  small: claude-haiku-5.5
  medium: claude-sonnet-5.5
  large: claude-opus-5.5
```

You are about to dispatch the `correctness-review` pass.

You have `review-loop` loaded. Read and follow:
- `skills/review-loop/SKILL.md`
- `skills/shared/delegation.md`
- `skills/shared/subagent-models.md`

Do you:
A) Leave `model` unset — no role is configured, so it runs on the session model
B) Dispatch on `claude-opus-5.5`
C) Dispatch on `claude-sonnet-5.5` as a middle ground

What do you do? Reply with the letter and one sentence why.
