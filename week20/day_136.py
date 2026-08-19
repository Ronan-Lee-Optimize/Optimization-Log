# day 136 - review: pure python groupby logic (applied)
# opt-log | consistency over perfection.

logs = [
    {"subject": "math", "hours": 1},
    {"subject": "korean", "hours": 3},
    {"subject": "math", "hours": 4},
    {"subject": "english", "hours": 1},
    {"subject": "korean", "hours": 4},
]


totals = {}
for entry in logs:
    subj = entry["subject"]
    hrs = entry["hours"]

    if subj in totals:
        totals[subj] = totals[subj] + hrs

    else:
        totals[subj] = hrs


print("total hours per subject:")
for subj, total in totals.items():
    print(f"{subj}: {total}")


# review: find the max by hand
top_subject = None
highest = 0
for subj, total in totals.items():
    if total > highest:
        highest = total
        top_subject = subj


print()
print(f"most studied: {top_subject} ({highest} hours)")
