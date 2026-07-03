# day 91 - matplotlib: full practice
# opt-log | consistency over perfection.

import pandas as pd
import matplotlib.pyplot as plt


subjects = []
hours_list = []


for i in range(4):

    subj = input("enter subject: ")
    hrs = int(input("enter hours: "))

    subjects.append(subj)
    hours_list.append(hrs)



df = pd.DataFrame({"subject": subjects, "hours": hours_list})


plt.bar(df["subject"], df["hours"])

plt.title("my study hours")
plt.xlabel("subject")
plt.ylabel("hours")


print()
print(f"total hours: {sum(hours_list)}")

plt.show()
