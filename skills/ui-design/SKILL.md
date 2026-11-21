---
name: ui-design
description: Design, refine, or review a web interface when the request concerns layout, visual hierarchy, interaction, or usability. Use for new UI, design critiques, and scoped improvements to existing screens or components.
---

# UI Design

## Start with the task

Identify who uses the surface, what they need to accomplish, and the records, controls, or evidence they work with. Use the brief and the existing product to infer ordinary design decisions. Ask when missing context would materially change the workflow or deliverable.

For existing products, check nearby screens, shared components, and design tokens. Use them as the starting point and honor the requested scope.

Ask what the user must see together to make their next decision or take their next action. Use the answer to decide what stays visible, what belongs side by side, and what can be revealed on demand. Preserve those relationships when the layout adapts.

- If the job is to **compare** invoices, align the values people compare across records and keep each value tied to its vendor.
- If the job is to **approve** invoices, keep the current invoice, supporting evidence, and decision controls close enough to use together.
- If the job is to **monitor** overdue payments, surface urgent exceptions and give each a path to its details.

## Choose the mode

- **Create.** Pick a composition that serves the primary task and build the requested surface. Use representative content and cover the states the workflow can enter, such as loading, empty, error, and success. Verify the result.
- **Review.** Follow the primary workflow and inspect the relevant states. Report findings in order of user impact and leave implementation files untouched. For each finding, give its location and trigger, what you observed, how it affects the task, and the smallest change likely to help. Mark findings inferred from source as such.
- **Refine.** Inspect the target and use any relevant existing findings as leads. Confirm they still apply, fix issues within the requested scope, and rerun the affected workflow. For a specific edit, keep the inspection and changes focused on that target.

Infer the mode from the request. A request to improve an existing interface uses Refine and includes the inspection needed to choose changes. A request to review and fix explicitly uses both in one pass. Read [Common UI pitfalls](references/pitfalls.md) for reviews and broad refinements, or when a creation or targeted edit raises one of those issues.

## Verify changes

Replay the primary task in the rendered interface when available. Check the conditions that could invalidate the design, such as long content, narrow screens, keyboard navigation, or failure and retry. Compare the result to the original finding or task and adjust if it still gets in the way. Say what you checked and flag any material behavior you could only inspect in source.
