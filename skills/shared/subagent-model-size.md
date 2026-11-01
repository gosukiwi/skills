# Subagent model size

Prefer the **smallest model that can finish the task reliably**. When the host can express tiers, do not default to the coordinator's model.

## Resolve (each dispatch)

Choose a tier (small / medium / large) using Tiers + Heuristics, then run the
bundled resolver with Python 3.11+ from the project root:

```sh
python3 <skills-directory>/shared/scripts/resolve_model.py --host codex --tier large
```

Use the actual installed skills directory containing this file and the current
harness key (`codex`, `claude-code`, `pi`, or another host's config key).
When running elsewhere, pass `--project-root /path/to/project`.
Use the JSON object on stdout as dispatch options; `{}` means leave model and
reasoning unset. Do not parse config or calculate precedence yourself. On a
nonzero exit, report the error and stop dispatch; do not bypass the resolver.

On Codex, explicit model/reasoning overrides require `fork_turns: "none"`, so
supply task context in the prompt. If the dispatch tool cannot express an option
or rejects an ID, stop and report it; never silently drop or rewrite options.

## Config

Config: project `.agents/gosumode.toml`, otherwise `~/.agents/gosumode.toml`.

```toml
[hosts.codex.models]
small = "gpt-6-luna"
medium = "gpt-6.1-terra"
large = "gpt-6.1-sol"
```

Optional `[models]` entries provide defaults for all hosts. Each tier accepts a
model ID string or a table with `model` and optional `reasoning_effort`.

## Tiers

| Tier | Use for |
|------|---------|
| **Small / fast** | Narrow edits, boilerplate, single-file TDD, obvious renames, "make this test green" |
| **Medium** | Multi-file tasks within a clear plan, routine review, straightforward API wiring |
| **Large** | Ambiguous requirements, cross-cutting design, tricky failures, high-risk correctness |

## Heuristics

- **Implementer:** size to the *task*, not the whole feature. A two-line change → small.
- **Reviewer:** capability ≥ that task's implementer; prefer a *different* model ID when the host/config offers one at that bar. If the implementer already used the strongest available (or no different ID exists), same model is OK — still use a fresh review subagent. Never review with a weaker model.
- **Fix after REJECTED:** same size as the implementer unless the rejection needs deeper reasoning → bump one tier.
- When unsure between two tiers, pick the **smaller**; bump only after a failed attempt or a clearly hard task.

## Do not

- Hard-code vendor model IDs in task breakdowns (put project IDs in `.agents/gosumode.toml`)
- Use a large model for mechanical RED/GREEN on an already-specified task
- Treat a model catalog, store, or picker listing as a set of IDs you may pass
- Probe IDs with throwaway `Reply with exactly: OK` subagents
- Read a subagent that returns no text as a verdict on the model — retry once on the session model, then report the failure
