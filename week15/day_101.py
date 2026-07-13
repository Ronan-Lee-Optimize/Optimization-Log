# day 101 - new: numpy 2D arrays (applied)
# opt-log | consistency over perfection.
import numpy as np

# 2D array: rows = subjects, columns = days (mon, tue, wed)
hrs_2d = np.array([
    [2, 3, 1],  # math
    [1, 2, 2],  # english
    [2, 1, 3]   # korean
])

print(hrs_2d)
print(f"shape: {hrs_2d.shape}")  # (rows, columns)


# access a specific row (subject)
print(f"math hours: {hrs_2d[0]}")


# access a specific element (row, column)
print(f"english on wed: {hrs_2d[1, 2]}")


# sum across the whole 2D array
print(f"total hours: {hrs_2d.sum()}")


# sum per row (total per subject)
print(f"total per subject: {hrs_2d.sum(axis=1)}")



# 2D arrays = table-like data, just like a mini spreadsheet
