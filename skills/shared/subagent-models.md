# Subagent models

Every subagent dispatch names a **role**. The role picks the model. This covers subagents only: the orchestrator runs on whatever the user chose for the session.

## Roles

| Role | Dispatched for | Default |
|------|----------------|---------|
| `implementer` | `implement` tasks | `auto` |
| `fixer` | a fix after REJECTED, or for review findings | `auto` |
| `reviewer` | `implement`'s per-task review | `auto` |
| `correctness-review` | the `correctness-review` pass | `large` |
| `quality-review` | the code-quality pass | `large` |

A dispatch that matches no role leaves the model option unset, so it runs on the session model.

## Config: `.gosumode`

Before choosing, `Read` (or `test -f`) `./.gosumode` at the project root, then `~/.gosumode`. Do **not** treat a failed Glob/grep/search as "no file": it is often gitignored and invisible to search tools.

The **first file found is the config, whole**. Never fill a key the project file leaves out from the home file. A home file applies to any project that has none of its own.

```yaml
models:            # the tier ladder
  small: claude-haiku-5.5
  medium: claude-sonnet-5.5
  large: claude-opus-5.5
roles:             # per role: auto | small | medium | large | a literal model ID
  reviewer: medium
  correctness-review: claude-opus-5.5
```

Both sections are optional. Roles the file omits keep their default from the table above, so a file with only `models:` still sends `correctness-review` to `large`.

## Resolve (each dispatch)

1. **Role → value:** the config's `roles.<role>`, else the default.
2. **Value → model:**
   - **Literal ID:** use it as is.
   - **Tier:** the config's `models.<tier>`, else the host ladder's value for that tier, else leave the model option unset.
   - **`auto`:** pick a tier with the rules below, then resolve it as a tier.

A **host ladder** is a model option with documented per-size values, such as Claude Code's `haiku | sonnet | opus`. A free-form ID field (any string from a catalog or picker) is **not** a ladder.

A role set in the config is **exact**. The `auto` rules below never move it up or down, even when the reviewer ends up lighter than the implementer it checks.

Never invent an ID. If the host rejects a configured ID, stop and ask the user. Do not rewrite it to a similar name.

## `auto`

| Tier | Use for |
|------|---------|
| **small** | Narrow edits, boilerplate, single-file TDD, obvious renames, "make this test green" |
| **medium** | Multi-file tasks within a clear plan, routine review, straightforward API wiring |
| **large** | Ambiguous requirements, cross-cutting design, tricky failures, high-risk correctness |

- **implementer:** size the *task*, not the whole feature. A two-line change is small. When torn between two tiers, pick the smaller one.
- **fixer:** the implementer's tier. Go one tier up on a repeat rejection, or when the rejection needs deeper reasoning.
- **reviewer:** at least the implementer's tier. Prefer a different model ID at that level when one exists; otherwise reuse the same model in a fresh subagent.

## Do not

- Hard-code vendor model IDs in task breakdowns (they belong in `.gosumode`)
- Skip the path Read because Glob/search returned nothing
- Treat a model catalog, store, or picker listing as a set of IDs you may pass
- Probe IDs with throwaway `Reply with exactly: OK` subagents
- Read a subagent that returns no text as a verdict on the model. Retry once on the session model, then report the failure
