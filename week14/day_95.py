# day 95 - review: line chart with markers and grid (applied)
# opt-log | consistency over perfection.
import pandas as pd
import matplotlib.pyplot as plt


data = {"day": ["mon", "tue", "wed", "thu", "fri"],
        "study_hours": [7, 5, 8, 3, 9]}


df = pd.DataFrame(data)
print(df)
print()

print(f"average hours this week: {df['study_hours'].mean():.1f}")


plt.plot(df["day"], df["study_hours"], marker="o", linestyle="-", color="tomato")
plt.grid(True)

plt.title("study hours this week")
plt.xlabel("day")
plt.ylabel("hours")
plt.show()
