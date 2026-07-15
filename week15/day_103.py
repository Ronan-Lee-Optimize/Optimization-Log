# day 103 - new: numpy arange and reshape (applied)
# opt-log | consistency over perfection.
import numpy as np

# arange: like range(), but makes a numpy array directly
days = np.arange(1, 8)
print(f"days 1-7: {days}")



# reshape: turn a 1D array into a 2D shape
# 7 days -> reshape into (7, 1): 7 rows, 1 column
days_column = days.reshape(7, 1)
print(f"reshaped to column:\n{days_column}")



# another example: reshape a 6-element array into 2 rows x 3 cols
hrs = np.arange(6)
hrs_2d = hrs.reshape(2, 3)
print(f"reshaped 2x3:\n{hrs_2d}")
