# day 112 - week 16 wrap-up: numpy comprehensive review (applied)
# opt-log | consistency over perfection.
import numpy as np
import pandas as pd


# 2D array: rows = subjects, columns = 5 days
hrs_2d = np.array([
    [5, 2, 4, 4, 5],  # math
    [1, 2, 2, 1, 2],  # english
    [4, 3, 3, 2, 5]   # korean
])


print(hrs_2d)
print(f"shape: {hrs_2d.shape}")
print()


# axis review
print(f"total per subject: {hrs_2d.sum(axis=1)}")
print(f"total per day: {hrs_2d.sum(axis=0)}")
print()


# boolean indexing review
print(f"days with more than 2 hours (math row): {hrs_2d[0][hrs_2d[0] > 2]}")
print()


# reshape review
flat = hrs_2d.flatten()
print(f"flattened: {flat}")
reshaped = flat.reshape(5, 3)
print(f"reshaped 5x3:\n{reshaped}")
print()


# numpy -> pandas
df = pd.DataFrame(hrs_2d.T, columns=["math", "english", "korean"])
df.index = ["mon", "tue", "wed", "thu", "fri"]
print(df)
