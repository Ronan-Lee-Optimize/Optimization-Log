# day 96 - review: input with pandas and matplotlib (applied)
# opt-log | consistency over perfection.

import pandas as pd
import matplotlib.pyplot as plt


subjects = ["math", "english", "korean", "science"]
hours = []


# get today's study hours from user for each subject
for subj in subjects:
    hrs = int(input(f"how long did you study {subj} today? (hrs): "))
    hours.append(hrs)


data = {"subject": subjects, "hours": hours}
df = pd.DataFrame(data)
print()
print(df)
print()

print(f"total hours today: {df['hours'].sum()}")

print(f"most studied: {df.loc[df['hours'].idxmax(), 'subject']}")



plt.bar(df["subject"], df["hours"], color="skyblue")

plt.title("today's study hours by subject")
plt.xlabel("subject")
plt.ylabel("hours")


plt.grid(axis="y")
plt.show()
