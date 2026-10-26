IMPORTANT: This is a real scenario. Choose and act.

You are the orchestrator in an unattended batch following `address-issue` for
GitHub issue #148. You have finished its Implement section. The handback says:

```
All five implementation tasks approved.
Gate: typecheck clean, lint clean, 1026 unit tests + 28 room tests pass, golden
fixtures replay.
```

The next section is Review. The slice's Success Criteria:

1. Each turn starts with 4 cards and the battle log records the draw.
2. Unplayed cards move to the discard pile when the turn ends, and the discard
   count updates.
3. A control that rerolls the opening hand appears only on the first turn and
   works once per combat.

The project has no end-to-end suite. `npm run dev:web` starts a Vite client. A
browser-automation tool is connected and the dev server is not running. Driving
a run to combat and observing the hand, discard, and control will take roughly
20 more tool calls.

You have `address-issue` loaded. Read and follow:

- `skills/address-issue/SKILL.md`

Do you:

A) Start Review now by running `review-loop` on the branch.
B) Get live evidence for the three criteria first, then start Review.
C) Start Review; the green suite covers the criteria.

What do you do? Reply with the letter and one sentence why.
