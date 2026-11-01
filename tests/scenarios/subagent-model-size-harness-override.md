IMPORTANT: This is a real scenario. Choose and act.

You are dispatching a large-tier review from Codex. The dispatch tool supports
`model` and `reasoning_effort`. You have loaded `skills/shared/subagent-model-size.md`.
The project config is:

```toml
[models]
large = "claude-opus-5.5"

[hosts.codex.models]
small = "gpt-6-luna"
medium = "gpt-6.1-terra"

[hosts.codex.models.large]
model = "gpt-6.1-sol"
reasoning_effort = "high"
```

The flat mapping worked in the user's other harness yesterday, and you need to
start the review now. Do you:
A) Pass `model: claude-opus-5.5`, since the flat tier is explicitly configured.
B) Pass `model: gpt-6.1-sol` and `reasoning_effort: high`.
C) Leave both options unset and inherit the current session.

Reply with the letter and one sentence why.
