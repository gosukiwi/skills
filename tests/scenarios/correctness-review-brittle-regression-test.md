IMPORTANT: This is a real scenario. Choose and act.

A checkout PR rejects carts over 20 items. Its new service test asserts the
documented error for a 21-item cart and also spies on a private helper to assert
that the service calls it exactly once. The team is already planning to inline
that helper. Inlining it would preserve the checkout response but break the test.
The test fails against the old service, and all checks pass on the PR. The
author asks you to raise findings only under the rules in the review skill.

Read `skills/correctness-review/SKILL.md`.

Do you:
A) Report no findings. The test proves the checkout limit and the extra
   assertion is a matter of test style.
B) Report a finding on the spy assertion. Keep the error assertion and explain
   how inlining the helper would break the test even if checkout still works.
C) Block the PR for missing coverage of the checkout limit.

What do you do? Reply with the letter and one sentence why.
