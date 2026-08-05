# day 124 - review: filtering csv data (applied)
# opt-log | consistency over perfection.
import pandas as pd

df = pd.read_csv("practice_log.csv")
print("--- all logged data ---")
print(df)
print()


# 1. filter by specific subject only (e.g., math)
math_logs = df[df["subject"] == "math"]
print("--- math logs only ---")
print(math_logs)
print()


# 2. Filter study sessions exceeding a specific time (over 2 hours)
hard_work = df[df["hours"] > 2]
print("--- sessions over 2 hours ---")
print(hard_work)
