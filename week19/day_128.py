# day 128 - bridge week: reimplementing pandas groupby in pure python (applied)
# opt-log | Consistency over perfection.

logs = [
    {"subject": "math", "hours": 4},
    {"subject": "english", "hours": 2},
    {"subject": "math", "hours": 3},
    {"subject": "korean", "hours": 3},
    {"subject": "english", "hours": 1},
    {"subject": "math", "hours": 2},
]


# pandas equivalent: df.groupby("subject")["hours"].sum()
# doing it by hand with a dict as the "bucket" for each subject
totals = {}


for entry in logs:
    subj = entry["subject"]
    hrs = entry["hours"]

    if subj in totals:
        totals[subj] = totals[subj] + hrs
    else:
        totals[subj] = hrs


print("total hours per subject:")
print()
for subj, total in totals.items():
    print(f"{subj}: {total}")
