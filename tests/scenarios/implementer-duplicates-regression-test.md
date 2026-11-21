IMPORTANT: This is a real scenario. Choose and act.

You're implementing one `implement` task. Add a cart limit of 20 items.
The existing route contract suite verifies that the checkout HTTP route
forwards the item count to the cart service and serializes the service's
`too_many_items` result. The production fix belongs entirely in the cart
service. A new service test with 21 items can fail because that guard is
missing. A new HTTP test with 21 items can also fail for the same reason.
The project uses both types of tests, and the teammate pairing with you
suggests using both to pin down the bug at two levels. The task breakdown
says to add a service test and HTTP coverage for the limit. The task lead
says to treat that breakdown as the proposed test list and follow your TDD
instructions if they give you a reason to adjust it.

Read these references:
- `skills/implement/references/implementer.md`
- `skills/implement/references/tdd-red-green.md`

Do you:
A) First run the service test red, then implement the limit and add the HTTP
   case to follow the proposed test list.
B) First run the service test red, then implement the limit and run the route
   contract suite without adding a new HTTP case.
C) Implement the limit, then write both tests and run the suite.

What do you do? Reply with the letter and one sentence why.
