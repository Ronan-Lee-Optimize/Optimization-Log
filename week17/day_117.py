# day 117 - new: adding a date column to each log entry (applied)
# opt-log | consistency over perfection.
import pandas as pd
from datetime import date

subjects = ["math", "english", "korean", "social studies", "history"]
hours = []


for subj in subjects:
    hrs = int(input(f"how many hours did you study {subj} today? "))
    hours.append(hrs)


# get today's date automatically
today = date.today()
print()
print(f"logging entry for: {today}")


df_new = pd.DataFrame({"date": [today] * len(subjects),
                        "subject": subjects,
                        "hours": hours})


df_old = pd.read_csv("study_log.csv")
df_combined = pd.concat([df_old, df_new], ignore_index=True)
df_combined.to_csv("study_log.csv", index=False)



print()
print("daily summary logged:")
print(df_new)
