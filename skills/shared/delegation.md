# Delegation

How to run one skill from another. Read this when a skill tells you to run another skill.

These skills set `disable-model-invocation: true`, so naming a skill does not run it. To run one, resolve its directory, read its `SKILL.md`, and follow it.

## Path resolver

For skill `<name>`, try in order; first that exists wins.

1. `.agents/skills/<name>/`
2. `.cursor/skills/<name>/`
3. `~/.agents/skills/<name>/`
4. `~/.cursor/skills/<name>/`

If none exist, tell the user the skill is missing and stop. Do not improvise its steps from its name.

Read `<resolved>/SKILL.md` and follow it. If it points at other files in that skill, read them from the same resolved directory.

## Dispatching to a subagent

The calling skill says where each skill runs — most run in the current session. When the caller asks for a subagent, resolve the path yourself and paste into the prompt:

- the absolute path to `<resolved>/SKILL.md`, with an instruction to read it first and follow it
- every input the skill needs, inline — diff, task text, scope, intent. A subagent gets what you paste and nothing else, so never point it at chat history.
- what to return
