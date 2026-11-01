---
name: setup-gosumode
description: Walk through creating or updating Gosumode model tiers for one or more harnesses.
disable-model-invocation: true
---

Configure model tiers through a short conversation. Use choices already supplied
in the session; ask only what is missing. Read existing project and home
`.agents/gosumode.toml` files before proposing changes.

## Explore

Ask one short numbered round at a time, with options and a recommendation. Wait
for the answer before the next round; skip rounds already settled.

1. **Scope and harnesses.** Personal defaults (`~/.agents/gosumode.toml`, recommended
   for personal preferences) or this project (`.agents/gosumode.toml`)? Which
   harnesses? Infer the current harness when clear; ask about others.
2. **Tiers.** Which of small, medium, and large should be configured? Check
   `../shared/scripts/resolve_model.py` for built-in ladders. For a laddered host,
   suggest its small/medium/large defaults and explain that accepting them needs
   no config. For a host without a ladder, recommend inheriting the current
   session model, or ask the user for exact model IDs for the tiers they want.
   Do not invent a ladder or choose IDs from a catalog.
3. **Overrides.** For explicit mappings, settle each selected tier's model.
   Default reasoning needs no field; ask about reasoning only if requested.

No overrides chosen? Create no file. Existing config stays unchanged unless the
user explicitly chooses to remove its overrides. Explain the effective fallback:
a built-in ladder where supported, otherwise the current session model.

## Write

Read `references/config.md` for schema and precedence. Explain if the chosen
scope is shadowed or a project file will replace home defaults as a whole.
Preserve unrelated settings in an existing file; resolve conflicting values
with the user. Once scope and mappings are settled, validate the draft in a
temporary project root with the resolver, then write the chosen config.
Report its path and effective model per selected tier. Do not dispatch probe
workers, install skills, or modify harness settings.
