# Config

TOML paths: project `.agents/gosumode.toml`, then `~/.agents/gosumode.toml`.
First file wins whole, even empty. Within it, `hosts.<harness>.models.<tier>`
overrides `models.<tier>`. Missing tiers use the resolver's ladder or inherit.
Host keys include `codex`, `claude-code`, `pi`; tiers are small, medium, large.
Prefer host mappings when models vary across harnesses:

```toml
[hosts.codex.models]
small = "gpt-6-luna"
medium = "gpt-6.1-terra"
large = "gpt-6.1-sol"
```

Tier values accept a model string or `{ model = "...", reasoning_effort = "high" }`.
Omit `reasoning_effort` for default reasoning.

Validate with Python 3.11+: place the draft at `.agents/gosumode.toml` in a temp
directory, then run for each configured host/tier:

```sh
python3 <skills-directory>/shared/scripts/resolve_model.py --host <harness> --tier <tier> --project-root <temp-directory>
```

Require exit zero and JSON matching the agreed mappings. This checks config,
not provider availability; never silently rewrite a rejected ID.
