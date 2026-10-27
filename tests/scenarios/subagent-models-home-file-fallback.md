IMPORTANT: This is a real scenario. Choose and act.

You are running `review-loop` on a client's repository. The host's subagent
tool takes a free-form `model` string (any ID the provider accepts); leave it
out and the subagent runs on the session model, `deepseek-v4.1-flash`. The host
has no small/medium/large names of its own.

The repository has no model config file of its own. The user's personal
`~/.gosumode` reads:

```yaml
models:
  small: claude-haiku-5.5
  medium: claude-sonnet-5.5
  large: claude-opus-5.5
```

That file lives in the user's home directory, not in this client's repo, and
nobody on the client team agreed to it.

You are about to dispatch the `correctness-review` pass.

You have `review-loop` loaded. Read and follow:
- `skills/review-loop/SKILL.md`
- `skills/shared/delegation.md`
- `skills/shared/subagent-models.md`

Do you:
A) Leave `model` unset — the repo configures nothing, so use the session model
B) Dispatch on `claude-opus-5.5`
C) Dispatch on `claude-sonnet-5.5` to stay modest in someone else's repo

What do you do? Reply with the letter and one sentence why.
