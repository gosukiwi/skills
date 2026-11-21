# Common UI pitfalls

Use these checks to find where people lose information, time, or control. A visual pattern earns a finding when it interferes with the task or conflicts with a relevant requirement.

| Area | Symptom | Check and possible fix |
| --- | --- | --- |
| Composition | Comparable records sit in cards with fields in different places. | Try finding the largest total or earliest due date across several records. If the search repeats on every card, align the key values in rows or columns. |
| Hierarchy | A heading, decorative panel, or repeated set of equally prominent actions pushes the main work out of view. | Open the page at a representative viewport and identify the current object and next action. Give the information needed for that action priority. |
| Interaction feedback | A submitted action leaves the user guessing whether it registered. | Trigger the action with a slow response and then a failure. Show pending, success, or failure in context, guard against accidental repeats, and retain inputs when a retry is possible. |
| Responsive behavior | The small-screen layout fits but loses identity, ordering, or comparison context. | Repeat the desktop task at a narrow width. Preserve the relationships the task needs, for example by keeping record labels beside values or carrying the selected record into the detail view. |
| Keyboard access | A control works with a pointer but is hard to find or operate with the keyboard. | Walk the task using the keyboard. Check that focus is visible and follows a useful order, controls activate as expected, and any overlay lets focus return to the relevant control. |
| Content and states | The layout relies on short sample strings or always-populated data. | Try a long label, an empty result, and a realistic error. Keep the information needed for the next decision readable and give the user a way to continue when appropriate. |
| Design consistency | The same action or state looks different across neighboring screens. | Compare equivalent controls and states. Reuse existing components and tokens unless the difference helps users understand a real change in meaning. |

Use [Nielsen’s usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) for broad interaction checks and [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for specific web accessibility criteria. For a claim about conformance, identify the applicable criterion and level and check its conditions. Treat judgments about the visual composition as contextual and explain the effect on the user’s task.
