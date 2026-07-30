# day 118 - new: visualizing real csv log data (applied)
# opt-log | consistency over perfection.
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("study_log.csv")
print(f"total rows logged: {len(df)}")
print()


# group by subject across ALL logged days combined
totals = df.groupby("subject")["hours"].sum()
print(totals)


plt.bar(totals.index, totals.values, color="mediumpurple")
plt.title("total study hours by subject (all logs)")
plt.xlabel("subject")
plt.ylabel("total hours")
plt.grid(axis="y")
plt.show()


print()
print(f"most studied overall: {totals.idxmax()}")
