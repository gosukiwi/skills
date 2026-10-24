# Subagent model size

Prefer the **smallest model that can finish the task reliably**. When the host can express tiers, do not default to the coordinator's model.

## Resolve (each dispatch)

1. Load config: `Read` (or `test -f` / shell) `.flow` at that exact path before choosing a model. Do **not** treat a failed Glob/grep/search as "no config" — the file is often gitignored and invisible to search tools.
2. Choose a **tier** (small / medium / large) using Tiers + Heuristics.
3. Resolve that tier to a **model**:
   - If the file defines `models.<tier>`, use that exact ID. It wins on every host.
   - Else, if the host has a **tier ladder** — its model option accepts documented values per size (the host's own small/medium/large names) — use the value for that tier.
   - Else, leave the model option unset so the session's current model is used.
4. Never invent an ID. If a config ID is rejected by the host, stop and ask the user — do not silently rewrite it.

A free-form model ID — any string the tool will accept, chosen from a catalog or picker — is **not** a ladder. On such a host with no `.flow` tier, subagents inherit the session model.

Config is optional (missing file → host ladder, else the session model). Example `.flow`:

```yaml
models:
  small: composer-2.5-fast
  medium: grok-4.5-xhigh
  large: grok-4.5-xhigh
```

A present tier key wins over any host default the model feels like.

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

- Hard-code vendor model IDs in task breakdowns (put project IDs in `.flow`)
- Skip the path Read because Glob/search returned nothing
- Ignore `.flow` when it defines the chosen tier
- Silently rewrite a config ID to a similar host name
- Use a large model for mechanical RED/GREEN on an already-specified task
- Treat a model catalog, store, or picker listing as a set of IDs you may pass
- Probe IDs with throwaway `Reply with exactly: OK` subagents
- Read a subagent that returns no text as a verdict on the model — retry once on the session model, then report the failure
