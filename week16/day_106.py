# day 106 - review: numpy array basics (applied)
# opt-log | consistency over perfection.
import numpy as np


# study hours for a full week
hrs = np.array([4, 3, 5, 2, 6, 1, 4])


print(hrs)

# total
print(f"total hours this week: {hrs.sum()}")

# average
print(f"average per day: {hrs.mean():.1f}")

# max
print(f"best day hours: {hrs.max()}")

# min
print(f"worst day hours: {hrs.min()}")
