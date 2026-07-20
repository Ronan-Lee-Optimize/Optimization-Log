# day 108 - review: numpy 2D arrays and axis (applied)
# opt-log | consistency over perfection.
import numpy as np

# rows = subjects, columns = mon/tue/wed/thu
hrs_2d = np.array([
    [2, 3, 1, 2],  # math
    [1, 2, 2, 1],  # english
    [2, 1, 3, 2]   # korean
])


print(hrs_2d)
print()
print(f"shape: {hrs_2d.shape}")
print()

# indexing review
print(f"math row: {hrs_2d[0]}")
print(f"korean on wed: {hrs_2d[2, 2]}")
print()

# slicing review
print(f"tue column (all subjects): {hrs_2d[:, 1]}")
print()

# axis review: axis=1 across rows (per subject), axis=0 down columns (per day)
print(f"total per subject: {hrs_2d.sum(axis=1)}")
print(f"total per day: {hrs_2d.sum(axis=0)}")
