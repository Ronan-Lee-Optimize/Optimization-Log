# day 72 - pandas: basic operations
# opt-log | consistency over perfection.

import pandas as pd

data = {"subject": ["Math", "English", "Korean"],
        "score": [85, 92, 78]}

df = pd.DataFrame(data)

print(df["score"])        # access a column
print()
print(df["score"].mean()) # average
print(df["score"].max())  # highest
print(df["score"].min())  # lowest
