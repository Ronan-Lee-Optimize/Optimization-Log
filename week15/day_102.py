# day 102 - new: numpy 2D slicing and axis=0 (applied)
# opt-log | consistency over perfection.
import numpy as np

# rows = subjects (math, english, korean), columns = days (mon, tue, wed)
hrs_2d = np.array([
    [2, 3, 1],
    [1, 2, 2],
    [2, 1, 3]
])



# slicing: get all rows, only 'mon' column (column index 0)
mon_hours = hrs_2d[:, 0]
print(f"mon hours (all subjects): {mon_hours}")


# slicing: get first 2 rows, all columns
first_two_subjects = hrs_2d[:2, :]
print(f"first two subjects:\n{first_two_subjects}")


# axis=0 sums DOWN each column (total per day, across subjects)
print(f"total per day: {hrs_2d.sum(axis=0)}")


# compare: axis=1 was per row (per subject), axis=0 is per column (per day)
print(f"average per day: {hrs_2d.mean(axis=0)}")
