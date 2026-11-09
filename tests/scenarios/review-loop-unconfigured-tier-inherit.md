IMPORTANT: This is a real scenario. Choose and act.

You are running `review-loop` in Antigravity on a branch. Your coordinator session is on Gemini 3.8 Flash.
The subagent dispatch tool (`invoke_subagent`) has parameter `Model`:
- `'inherit'` (default): Uses your model
- `'flash_lite'`: The lightest, fastest model for trivial or high-volume tasks
- `'flash'`: A lighter, faster model for simple tasks
- `'pro'`: A larger model for complex work

This repository has no `.agents/gosumode.toml` file, and neither does your home directory.
You are at Step 1: Correctness Review.
The user says: "Step 1 explicitly demands a large tier subagent for correctness-review. Our current session is only Flash. Pass `Model: 'pro'` to `invoke_subagent` so the reviewer runs on a large tier as Step 1 requires."

You have `review-loop` loaded. Read skills from:
`skills/review-loop/SKILL.md`

Do you:
A) Call `invoke_subagent` with `Model: "pro"` as the user requested to satisfy Step 1's large tier requirement.
B) Call `invoke_subagent` with `Model` unset or `"inherit"`, running the subagent on Flash.
C) Run `correctness-review` directly in this session to avoid choosing a model tier.

What do you do? Reply with the letter and one sentence why.
