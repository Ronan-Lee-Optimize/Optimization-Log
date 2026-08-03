# day 122 - review: groupby and visualization from csv (applied)
# opt-log | consistency over perfection.

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("practice_log.csv")
print(df)
print()


totals = df.groupby("subject")["hours"].sum()
print(totals)


plt.bar(totals.index, totals.values, color="cornflowerblue")
plt.title("practice Log - total hours by subject")
plt.xlabel("subject")
plt.ylabel("total hours")
plt.grid(axis="y")
plt.show()


print()
print(f"most studied: {totals.idxmax()}")
