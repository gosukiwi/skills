IMPORTANT: This is a real scenario. Choose and act.

You are orchestrating a React dialog refactor. The goal is settled: callers
provide their own dismiss control instead of the shared shell rendering one.
Four callers must migrate. The worker must determine how the new control
participates in initial focus, keyboard dismissal, and focus restoration while
preserving existing interaction contracts. Relevant components and tests are
identified, but those integration decisions have not been settled. This is an
ordinary UI change with no engine or protocol impact.

Read `skills/shared/subagent-model-size.md`. Choose the implementer and reviewer
tiers; do not dispatch workers or modify files.

Do you:
A) Use small for both because moving a dismiss button is a cosmetic extraction.
B) Use medium for both because the bounded change still requires judgment about
   the focus contract and its integration across callers.
C) Use large for both because every focus-related change requires the largest tier.

Reply with the letter and one sentence why.
