# day 126 - week 18 wrap-up: Advanced SLA review (applied)
# opt-log | consistency over perfection.

import pandas as pd
from datetime import date


# 1. receive new data input
subjects = ["math", "english", "science"]
hours =[]


print(f"logging practice entry for: {date.today()}")
for subj in subjects:
    hrs = int(input(f"how many hours did you study {subj} today? "))
    hours.append(hrs)


df_new = pd.DataFrame({"date": [date.today()] * len(subjects),
                       "subject": subjects,
                       "hours": hours})


# 2. load, merge, and save existing data
df_old = pd.read_csv("practice_log.csv")
df_all = pd.concat([df_old, df_new], ignore_index=True)
df_all.to_csv("practice_log.csv", index=False)


print("\n--- updated all-time data ---")
print(df_all)


# 3. analyze data (identify the most vulnerable subject - study sessions of 2 hours or less)
short_sessions = df_all[df_all["hours"] <= 2]
needs_work = short_sessions.groupby("subject")["hours"].count()


print("\n--- subjects that need more focus (sessions with 2 hrs or less) ---")
print(needs_work)
