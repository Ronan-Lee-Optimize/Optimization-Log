# day 107 - review: numpy indexing and broadcasting (applied)
# opt-log | consistency over perfection.
import numpy as np

hrs = np.array([4, 3, 5, 2, 6, 1, 4])


# indexing and slicing review
print(f"monday hours: {hrs[0]}")
print(f"sunday hours: {hrs[-1]}")
print(f"first 3 days: {hrs[:3]}")
print(f"last 3 days: {hrs[-3:]}")


# broadcasting review: apply math to the whole array at once
hrs_plus_30min = hrs + 0.5
print(f"with 30 extra min each day: {hrs_plus_30min}")


hrs_half = hrs / 2
print(f"if i only did half: {hrs_half}")
