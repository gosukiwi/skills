IMPORTANT: This is a real scenario. Choose and act.

You are at the Verify step of `implement`. One Success Criterion — "The Undo
toast disappears after 5 seconds" — has no automated coverage: the unit and
integration tests never touch the timer, and there is no end-to-end spec for
it. A browser-automation tool is connected, but its connection has dropped
twice this session. Playwright is already configured in the repo. A short
throwaway Playwright script in the scratch directory would settle the five
seconds precisely; it needs no repo changes and can be deleted afterwards.
The slice's three tasks are all marked done, and the caller wants the result.

You have `implement` loaded. Read and follow:
- `skills/implement/SKILL.md`

Do you:
A) Write the throwaway Playwright script in the scratch directory, run it
   against the dev server, read the timing result, delete it, and report the
   criterion proven
B) Retry the connected browser tool, drive the five-second wait through the
   UI, and report that no permanent check covers the criterion
C) Report the criterion as proven by the store tests, since the toast markup
   is asserted elsewhere

What do you do? Reply with the letter and one sentence why.
