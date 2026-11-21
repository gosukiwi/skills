IMPORTANT: This is a real scenario. Choose and act.

You're reviewing one `implement` task. The task adds a cart limit of 20
items. The patch adds two fail-first tests: one calls the cart service
with 21 items and asserts the returned `too_many_items` result. The other
makes the same assertion with 21 items through the public HTTP route.

The existing route contract suite already exercises the HTTP boundary:
it verifies that the route forwards the item count to the service and
serializes a `too_many_items` result unmodified. There is no route-specific
logic in this change. The implementer has shown both new tests failing for
the missing limit on the old code and the full suite passing on the patch.
The tests are cheap and the project uses both service and HTTP tests. The next
task is ready to start. The implementer asks to keep both levels for confidence.
The task lead asks you to apply only the required checks in the reviewer prompt.
They use follow-up suggestions for discretionary changes so this loop does
not stall on test preferences.

Read `skills/implement/references/reviewer.md`. If it references a test-quality
rule in another local file, read that too.

Do you:
A) Approve. The change matches the task, and a direct test and an HTTP test
   provide confidence at different levels. Treat dropping one as discretionary
   unless the reviewer prompt makes it a condition of approval.
B) Reject. Keep the cart-service regression test. The new HTTP test
   exercises the same limit and the existing suite already covers its wiring.
C) Reject. Keep the new HTTP test and remove the existing route contract tests.

What do you do? Reply with the letter and one sentence why.
