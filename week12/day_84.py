# day 84 - week 12 wrap-up: pandas full review
# opt-log | consistency over perfection.

import pandas as pd

data = {"subject": ["Math", "English", "Korean"],
        "hours": [3, 5, 2]}


df = pd.DataFrame(data)


df["status"] = ["okay", "great", "need more"]

sorted_df = df.sort_values("hours", ascending=False)


print(sorted_df)

print(f"total: {df['hours'].sum()}")
