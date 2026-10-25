# Delegation

How to run one skill from another. Read this when a skill tells you to run another skill.

These skills set `disable-model-invocation: true`, so naming a skill does not run it. To run one, resolve its directory, read its `SKILL.md`, and follow it.

## Where the shared files are

`shared/` sits beside the skill folders, in the same skills directory the calling skill was loaded from. Anchor on the folder that holds the calling `SKILL.md`: its parent is the skills root, and the skills root's `shared/` holds this file and `subagent-model-size.md`. Do not search for them, and do not resolve them against the working directory.

If this file or another shared file is missing from that folder, stop and tell the user. Do not borrow a copy from a different skills directory, and do not run the calling skill's steps without it.

## Path resolver

For skill `<name>`, try in order; first that exists wins.

1. `<skills-root>/<name>/`
2. `.agents/skills/<name>/`
3. `.commandcode/skills/<name>/`
4. `.claude/skills/<name>/`
5. `.cursor/skills/<name>/`
6. `~/.agents/skills/<name>/`
7. `~/.commandcode/skills/<name>/`
8. `~/.claude/skills/<name>/`
9. `~/.cursor/skills/<name>/`

`<skills-root>` is the parent of the folder holding the calling `SKILL.md`.

If none exist, tell the user the skill is missing and stop. Do not improvise its steps from its name.

Read `<resolved>/SKILL.md` and follow it. If it points at other files in that skill, read them from the same resolved directory.

## Dispatching to a subagent

The calling skill says where each skill runs — most run in the current session. When the caller asks for a subagent, resolve the path yourself and paste into the prompt:

- the absolute path to `<resolved>/SKILL.md`, with an instruction to read it first and follow it
- the absolute path to any shared file the subagent needs (`<skills-root>/shared/<file>`), never a bare `shared/<file>` for the subagent to resolve against its own working directory
- every input the skill needs, inline — diff, task text, scope, intent. A subagent gets what you paste and nothing else, so never point it at chat history.
- what to return

When choosing the subagent's model, resolve the tier specified by the calling skill per `subagent-model-size.md`, beside this file.
