# day 104 - new: numpy boolean indexing (applied)
# opt-log | consistency over perfection.
import numpy as np

hrs = np.array([3, 4, 2, 5, 3, 6, 1])

# a comparison on the whole array returns True/False for each element
is_long_day = hrs > 3
print(f"long study days (comes out True/False): {is_long_day}")



# use that True/False array to filter - only keep values where condition is True
long_days = hrs[hrs > 3]
print(f"actual hours on long days: {long_days}")



# count how many days matched
print(f"number of long days: {(hrs > 3).sum()}")



# combine conditions with & (and), | (or)
mid_range = hrs[(hrs >= 3) & (hrs <= 5)]
print(f"days between 3 and 5 hours: {mid_range}")

#boolean indexing = filtering an array with a condition (no loop needed)
