# day 116 - new: logging today's real input into the csv (applied)
# opt-log | consistency over perfection.
import pandas as pd

subjects = ["math", "english", "korean", "social studies"]
hours = []


# get today's actual hours from input, instead of hardcoded numbers
for subj in subjects:
    hrs = int(input(f"how many hours did you study {subj} today? "))
    hours.append(hrs)


df_new = pd.DataFrame({"subject": subjects, "hours": hours})


# load existing log and append today's row
df_old = pd.read_csv("study_log.csv")
df_combined = pd.concat([df_old, df_new], ignore_index=True)


df_combined.to_csv("study_log.csv", index=False)


print()
print("today's entry added:")
print(df_new)
print()
print(f"log now has {len(df_combined)} total rows")
