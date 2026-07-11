# day 99 - new: numpy introduction (applied)
# opt-log | consistency over perfection.
import numpy as np

# make a numpy array (like a list, but faster for math operations)
hrs = np.array([3, 4, 2, 5, 3])

print(hrs)

# numpy gives built-in math functions - no loop needed!
print(f"total: {hrs.sum()}")      # add up all values
print(f"average: {hrs.mean():.1f}")  # mean = average
print(f"max: {hrs.max()}")        # largest value

print("numpy array feels like a supercharged list")
