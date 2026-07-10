# day 98 - week 14 wrap-up: matplotlib and pandas combined (applied)
# opt-log | consistency over perfection.

import pandas as pd
import matplotlib.pyplot as plt

data = {"subject": ["math", "english", "korean", "social studies"],
        "mon": [3, 1, 2, 4],
        "tue": [2, 1, 5, 3],
        "wed": [3, 2, 3, 4]}

df = pd.DataFrame(data)
df["total"] = df["mon"] + df["tue"] + df["wed"]

print(df)
print()


print(f"grand total hours: {df['total'].sum()}")

print(f"most studied subject: {df.loc[df['total'].idxmax(), 'subject']}")


fig, axes = plt.subplots(1, 3, figsize=(14, 4))


axes[0].bar(df["subject"], df["total"], color="mediumseagreen")
axes[0].set_title("total hours by subject")


axes[1].plot(["mon", "tue", "wed"], [df["mon"].sum(), df["tue"].sum(), df["wed"].sum()],
             marker="o", color="tomato")

axes[1].set_title("Daily Total Trend")
axes[1].grid(True)

axes[2].pie(df["total"], labels=df["subject"], autopct="%1.1f%%")
axes[2].set_title("subject share")

plt.tight_layout()
plt.show()

#week 14 review done
