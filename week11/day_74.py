# day 74 - pandas: adding columns
# opt-log | consistency over perfection.

import pandas as pd

data = {"subject": ["Math", "English", "Korean", "Science"],
        "score": [85, 92, 78, 95]}


df = pd.DataFrame(data)


df["grade"] = ["B", "A", "C", "A"]  # add a new column

print(df)
