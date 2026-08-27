# day 140 - week 20 wrap-up: sorting and full pipeline review (applied)
# opt-log | consistency over perfection.

def add_entry(logs, subject, hours):
    logs.append({"subject": subject, "hours": hours})

    return logs


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


logs = []
logs = add_entry(logs, "math", 2)
logs = add_entry(logs, "english", 1)
logs = add_entry(logs, "korean", 4)
logs = add_entry(logs, "social studies", 5)



# review: bubble sort by hours, lowest to highest
n = len(logs)
for i in range(n):

    for j in range(n - 1 - i):

        if logs[j]["hours"] > logs[j + 1]["hours"]:
            temp = logs[j]
            logs[j] = logs[j + 1]
            logs[j + 1] = temp


print("sorted logs (lowest to highest hours):")
for entry in logs:
    print(entry)


totals = total_by_subject(logs)
print()
print("totals per subject:", totals)
