# day 123 - week 18 wrap-up: full csv logging pipeline review (applied)
# opt-log | consistency over perfection.
import pandas as pd
from datetime import date

subjects = ["math", "english"]
hours = []


print(f"logging practice entry for: {date.today()}")
for subj in subjects:
    hrs = int(input(f"how many hours did you study {subj} today? "))
    hours.append(hrs)


df_new = pd.DataFrame({"date": [date.today()] * len(subjects),
                        "subject": subjects,
                        "hours": hours})


df_old = pd.read_csv("practice_log.csv")
df_all = pd.concat([df_old, df_new], ignore_index=True)
df_all.to_csv("practice_log.csv", index=False)


totals = df_all.groupby("subject")["hours"].sum()
print()
print("all-time totals:")
print(totals)
print(f"top subject: {totals.idxmax()}")
