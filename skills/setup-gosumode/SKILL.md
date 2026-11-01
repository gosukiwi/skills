---
name: setup-gosumode
description: Walk through creating or updating Gosumode model tiers across harnesses.
disable-model-invocation: true
---

Read existing project and home `.agents/gosumode.toml` files. Reuse choices
already supplied; ask only what is missing, one short numbered round at a time.
Offer options and a recommendation, then wait for the answer.

1. **Scope and harnesses:** personal defaults or this project? Recommend personal
   scope for personal preferences. Infer the current harness; ask about others.
2. **Tiers:** which of small, medium, large? Check
   `../shared/scripts/resolve_model.py` for built-in ladders. Suggest a supported
   ladder's defaults; otherwise recommend current-model inheritance or ask for
   exact model IDs. Never invent a ladder or pick IDs from a catalog.
3. **Mappings:** settle explicit model choices per selected tier. Omit reasoning
   unless the user requests an override.

Accepting fallback defaults creates no file. Existing config stays unchanged
unless the user chooses to remove overrides. Explain the fallback: the built-in
ladder where supported, otherwise the current session model.

Read `references/config.md` before writing. Explain scope shadowing or loss of
home defaults when relevant. Preserve unrelated settings and resolve conflicts
with the user. Once choices are settled, validate the draft in a temporary
project root, write it, and report the path and effective mappings.
Limit changes to the config; never dispatch probe workers.
