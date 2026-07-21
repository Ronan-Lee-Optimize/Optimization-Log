# day 109 - review: numpy arange and reshape (applied)
# opt-log | Consistency over perfection.
import numpy as np

# arange review: quick way to build a sequence
days = np.arange(1, 11)
print(f"days 1-10: {days}")


# reshape review: turn 1D into 2D
# 10 elements -> reshape into 2 rows x 5 cols
days_2d = days.reshape(2, 5)
print(f"reshaped 2x5:\n{days_2d}")


# another reshape example: 5 rows x 2 cols
days_2d_v2 = days.reshape(5, 2)
print(f"reshaped 5x2:\n{days_2d_v2}")
