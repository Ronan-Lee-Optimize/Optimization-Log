# day 80 - review: pandas columns and sorting combined
# opt-log | consistency over perfection.

import pandas as pd

data = {"subject": ["math", "english", "korean"],
        "hours": [2, 1, 3]}

df = pd.DataFrame(data)


df["status"] = ["okay", "need more", "great"]  # add column manually


sorted_df = df.sort_values("hours", ascending=False)

print(sorted_df)
