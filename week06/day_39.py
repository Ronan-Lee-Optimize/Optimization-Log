# day 39 - review: list comprehension (applied)
# opt-log | Consistency over perfection.

scores = [45, 82, 91, 63, 77, 88, 55]


passed = [s for s in scores if s >= 70]   # filter passing scores
failed = [s for s in scores if s < 70]    # filter failing scores



print(f"passed: {passed}")

print(f"failed: {failed}")

print(f"pass count: {len(passed)}")

print(f"fail count: {len(failed)}")
