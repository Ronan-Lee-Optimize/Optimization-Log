# day 82 - review: pandas full practice
# opt-log | consistency over perfection.

import pandas as pd

data = {"subject": ["math", "korean", "english", "social studies"],
        "hours": [2, 1, 4, 3]}


df = pd.DataFrame(data)

df["status"] = ["okay", "need more", "great", "great"]



filtered = df[df["hours"] >= 3]

sorted_df = filtered.sort_values("hours", ascending=False)



print(sorted_df)
print()

print(f"total hours: {df['hours'].sum()}")
