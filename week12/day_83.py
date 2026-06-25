# day 83 - week 12 wrap up: pandas with input
# opt-log | consistency over perfection.

import pandas as pd

subjects = []
hours_list = []


for i in range(3):
    subj = input("enter subject: ")

    hrs = int(input("enter hours studied: "))

    subjects.append(subj)

    hours_list.append(hrs)

    print()


data = {"subject": subjects, "hours": hours_list}

df = pd.DataFrame(data)

print()
print(df)
print()

print(f"total hours: {df['hours'].sum()}")

print(f"average: {df['hours'].mean():.2f}")
