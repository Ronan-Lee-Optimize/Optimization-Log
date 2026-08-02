# day 121 - review: input logging with date (applied)
# opt-log | consistency over perfection.
import pandas as pd
from datetime import date


subjects = ["math", "english"]
hours = []


print("welcome to ur study logger")
print(f"logging practice entry for: {date.today()}")
for subj in subjects:
    hrs = int(input(f"how many hours did you study {subj} today? "))
    hours.append(hrs)


df_new = pd.DataFrame({"date": [date.today()] * len(subjects),
                        "subject": subjects,
                        "hours": hours})


df_old = pd.read_csv("practice_log.csv")
df_combined = pd.concat([df_old, df_new], ignore_index=True)
df_combined.to_csv("practice_log.csv", index=False)


print()
print("entry added:")
print(df_new)
