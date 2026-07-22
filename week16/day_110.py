# day 110 - review: numpy boolean indexing (applied)
# opt-log | consistency over perfection.
import numpy as np

hrs = np.array([2, 5, 1, 6, 3, 4, 2])


# condition on the whole array
is_short_day = hrs < 3
print(f"short study days (True/False): {is_short_day}")
print()

# filter using the condition
short_days = hrs[hrs < 3]
print(f"actual hours on short days: {short_days}")

print(f"number of short days: {(hrs < 3).sum()}")
print()


# combine conditions
mid_range = hrs[(hrs >= 2) & (hrs <= 4)]
print(f"days between 2 and 4 hours: {mid_range}")
