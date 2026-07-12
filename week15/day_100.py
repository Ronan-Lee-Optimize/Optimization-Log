# day 100 - new: numpy indexing and array math (applied)
# opt-log | consistency over perfection.
import numpy as np

hrs = np.array([3, 4, 2, 5, 3])


# indexing works just like lists
print(f"first day: {hrs[0]}")
print(f"last day: {hrs[-1]}")


# slicing also works like lists
print(f"first 3 days: {hrs[:3]}")


# numpy math applies to the WHOLE array at once (no loop needed!)
hrs_doubled = hrs * 2
print(f"doubled: {hrs_doubled}")


hrs_plus_one = hrs + 1
print(f"plus one hour each day: {hrs_plus_one}")


print("day 100! numpy math on the whole array, zero loops needed 🎯")
