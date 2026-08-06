# day 125 - review: filtering and visualization (applied)
# opt-log | consistency over perfection.
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("practice_log.csv")


# filter for 'true focus time' over 2 hours
focused_df = df[df["hours"] > 2]
print("--- focused sessions (over 2 hours) ---")
print(focused_df)
print()


# calculate total focused hours by subject
focused_totals = focused_df.groupby("subject")["hours"].sum()
print("--- focused totals by subject ---")
print(focused_totals)

# visualization
plt.bar(focused_totals.index, focused_totals.values, color="lightcoral")
plt.title("focused study hours (sessions > 2 hours)")
plt.xlabel("subject")
plt.ylabel("hours")
plt.grid(axis="y")
plt.show()
