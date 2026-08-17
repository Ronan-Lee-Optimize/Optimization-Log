# day 134: bridge week bonus: sorting study hours by hand (bubble sort)
# opt-log | Consistency over perfection.

logs = [
    {"subject": "korean", "hours": 3},
    {"subject": "math", "hours": 5},
    {"subject": "science", "hours": 1},
    {"subject": "english", "hours": 4},
]


# python's sorted() would do this in one line: 
# sorted(logs, key=lambda x: x["hours"])
# here it's done by hand with bubble sort


n = len(logs)
for i in range(n):
    for j in range(n - 1 - i):
        if logs[j]["hours"] > logs[j + 1]["hours"]:

            # swap the two entries
            temp = logs[j]
            logs[j] = logs[j + 1]
            logs[j + 1] = temp


print("sorted from lowest to highest hours:")
for entry in logs:
    print(entry)
