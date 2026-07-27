# day 115 - new: filtering and analyzing loaded csv data (applied)
# opt-log | consistency over perfection.
import pandas as pd

df = pd.read_csv("study_log.csv")
print("all logged data:")
print(df)
print()


# filter: only rows where hours > 3
long_sessions = df[df["hours"] > 3]
print("sessions over 3 hours:")
print(long_sessions)
print()
