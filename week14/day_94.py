# day 94 - review: matplotlib and pandas combined (Applied)
# opt-log | consistency over perfection.

import pandas as pd
import matplotlib.pyplot as plt

data = {"subject": ["math", "english", "korean", "social studies"],
        "this_week": [5, 1, 2, 4],
        "last_week": [3, 2, 5, 4]}



df = pd.DataFrame(data)


print(df)
print()
print(f"this week total: {df['this_week'].sum()}")
print(f"last week total: {df['last_week'].sum()}")


x = range(len(df["subject"]))


plt.bar([i - 0.2 for i in x], df["last_week"], width=0.4, label="last week")
plt.bar([i + 0.2 for i in x], df["this_week"], width=0.4, label="this week")

plt.xticks(x, df["subject"])

plt.title("weekly comparison")

plt.legend()

plt.show()
