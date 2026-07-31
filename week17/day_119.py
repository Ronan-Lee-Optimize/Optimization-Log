# day 119 - new: SLA (study log assistant) (mini project, wraps up week 17)
# opt-log | Consistency over perfection.
import pandas as pd
from datetime import date

subjects = ["math", "english", "korean", "social studies"]
hours = []

print(f"logging entry for: {date.today()}")
for subj in subjects:
    hrs = int(input(f"how many hours did you study {subj} today? "))
    hours.append(hrs)


# build today's entry with a date column
df_new = pd.DataFrame({"date": [date.today()] * len(subjects),
                        "subject": subjects,
                        "hours": hours})


# append to the existing log
df_old = pd.read_csv("study_log.csv")
df_all = pd.concat([df_old, df_new], ignore_index=True)
df_all.to_csv("study_log.csv", index=False)


print()
print(f"today's total: {df_new['hours'].sum()} hours")


# show all-time totals per subject
totals = df_all.groupby("subject")["hours"].sum()
print()
print("all-time totals:")
print(totals)
print(f"strongest subject overall: {totals.idxmax()}")
