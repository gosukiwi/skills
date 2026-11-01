# Model configuration

Requires Python 3.11+, with no third-party packages. Config files are TOML:
project `.agents/gosumode.toml`, otherwise `~/.agents/gosumode.toml`.
The first file wins whole, including an empty file. Host overrides win per tier
over flat `[models]` entries in that file. Omitted tiers use the resolver's
built-in host ladder, otherwise inherit the session model.

Prefer host-specific entries for mappings that vary by harness. Flat `[models]`
entries apply to every host without an override. Supported tiers are `small`,
`medium`, and `large`; host keys include `codex`, `claude-code`, and `pi`.

```toml
[hosts.codex.models]
small = "gpt-6-luna"
medium = "gpt-6.1-terra"
large = "gpt-6.1-sol"
```

A tier accepts a model ID string, or a table with `model` and optional
`reasoning_effort`. For an explicit reasoning override, replace that tier's
string entry with a table:

```toml
[hosts.codex.models.large]
model = "gpt-6.1-sol"
reasoning_effort = "high"
```

To validate before writing, place the draft at `.agents/gosumode.toml` inside a
temporary directory. Run the installed sibling helper for each configured host
and tier, using that directory as `--project-root`:

```sh
python3 <skills-directory>/shared/scripts/resolve_model.py --host codex --tier large --project-root <temporary-directory>
```

A nonzero exit rejects the draft. Check the JSON matches the agreed choices.
This validates configuration, not provider availability; never silently rewrite
an ID rejected by a dispatch tool.
