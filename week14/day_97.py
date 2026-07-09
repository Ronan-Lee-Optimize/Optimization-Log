# day 97 - review: subplot with pandas (applied)
# opt-log | consistency over perfection.

import pandas as pd
import matplotlib.pyplot as plt


data = {"day": ["mon", "tue", "wed", "thu", "fri"],
        
        "study_hours": [7, 5, 8, 3, 9],
        "sleep_hours": [6, 7, 5, 8, 6]}


df = pd.DataFrame(data)
print(df)
print()

print(f"average study hours: {df['study_hours'].mean():.1f}")
print(f"average sleep hours: {df['sleep_hours'].mean():.1f}")


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))


ax1.plot(df["day"], df["study_hours"], marker="o", color="tomato")


ax1.set_title("study hours")
ax1.grid(True)

ax2.bar(df["day"], df["sleep_hours"], color="skyblue")
ax2.set_title("sleep hours")

plt.tight_layout()
plt.show()
