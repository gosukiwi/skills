# Subagent model size

Choose the smallest tier that can finish reliably, then run the resolver:

```sh
python3 <skills-directory>/shared/scripts/resolve_model.py --host <harness> --tier <tier>
```

Use the installed skills directory and current harness key (e.g. `codex`,
`claude-code`, `pi`). Run from the project root or pass `--project-root DIR`.
Apply the returned JSON options through the host's dispatch tool; `{}` means
leave model/reasoning unset. Report resolver errors or unsupported/rejected options and stop;
never guess or map tiers directly to host enum names, substitute IDs,
drop options, or calculate precedence yourself without resolver output.
For configuration, use `setup-gosumode`.

## Tiers

| Tier | Use for |
|------|---------|
| small | Fully specified, mechanical changes: renames, style extraction, boilerplate, straightforward caller updates, and review of those changes—even across several files |
| medium | Bounded work requiring judgment about behavior or integration: API changes, focus handling, interacting components, and review of those changes |
| large | Ambiguous requirements, cross-cutting design, tricky failures, high-risk correctness |

- Size implementers to the individual task. Never use large for mechanical RED/GREEN.
- Reviewers must be at least as capable as the implementer. Prefer a different
  model at that bar when available; otherwise use the same model in a fresh worker.
- After rejection, keep the implementer's tier; bump one tier for deeper reasoning.
- When unsure, choose the smaller tier; bump after failure or clearly hard work.
- Keep model IDs out of task breakdowns. Catalogs are not dispatch mappings;
  never probe IDs with throwaway workers.
- An empty worker response is not model evidence: retry once on the session
  model, then report failure.
