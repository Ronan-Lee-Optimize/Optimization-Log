# day 133 - week 19 wrap-up: full logging pipeline in pure python (applied)
# opt-log | consistency over perfection.

def add_entry(logs, subject, hours):
    # same job as pd.concat - just append to a list
    logs.append({"subject": subject, "hours": hours})
    return logs


def filter_by_subject(logs, subject):
    result = []

    for entry in logs:
        if entry["subject"] == subject:
            result.append(entry)

    return result


def total_by_subject(logs):
    totals = {}

    for entry in logs:
        subj = entry["subject"]
        hrs = entry["hours"]

        if subj in totals:
            totals[subj] = totals[subj] + hrs

        else:
            totals[subj] = hrs

    return totals


def most_studied(totals):
    top_subject = None
    highest = 0

    for subj, total in totals.items():
        if total > highest:
            highest = total
            top_subject = subj

    return top_subject


logs = []
logs = add_entry(logs, "math", 4)
logs = add_entry(logs, "english", 2)
logs = add_entry(logs, "math", 3)
logs = add_entry(logs, "korean", 5)


print("all logs:")
for entry in logs:
    print(entry)


print()
print("math sessions:", filter_by_subject(logs, "math"))


totals = total_by_subject(logs)
print()
print("totals per subject:", totals)
print("most studied:", most_studied(totals))
