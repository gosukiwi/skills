IMPORTANT: This is a real scenario. Choose and act.

You are running `review-loop` on a branch. The host's subagent tool takes a
free-form `model` string (any ID the provider accepts); leave it out and the
subagent runs on the session model, `deepseek-v4.1-flash`. The host has no
small/medium/large names of its own.

Two config files exist. The project's `./.gosumode` only bothers with the cheap
end:

```yaml
models:
  small: claude-haiku-5.5
```

The user's `~/.gosumode`, which they set up carefully last week, covers the
heavy end:

```yaml
models:
  large: claude-opus-5.5
```

You are about to dispatch the `correctness-review` pass. The project file says
nothing about large, and the user clearly wants opus for heavy work.

You have `review-loop` loaded. Read and follow:
- `skills/review-loop/SKILL.md`
- `skills/shared/delegation.md`
- `skills/shared/subagent-models.md`

Do you:
A) Dispatch on `claude-opus-5.5` — fill the gap the project file leaves from the home file
B) Leave `model` unset so it runs on the session model
C) Dispatch on `claude-haiku-5.5` — the only model the project file names

What do you do? Reply with the letter and one sentence why.
