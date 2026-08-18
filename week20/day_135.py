# day 135 - review: pure python filtering and lookup (applied)
# opt-log | consistency over perfection.

logs = [
    {"subject": "math", "hours": 3},
    {"subject": "english", "hours": 5},
    {"subject": "korean", "hours": 2},
    {"subject": "s", "hours": 4},
]


# review of day 127: filtering with for + if
long_sessions = []
for entry in logs:
    if entry["hours"] > 3:
        long_sessions.append(entry)


print("sessions over 3 hours:")
for entry in long_sessions:
    print(entry)


# review of day 129: lookup pattern using a dict
scores = {"math": 70, "english": 92, "korean": 69, "social studies": 85}


search = input("\nenter a subject to look up its score: ")
if search in scores:
    print(f"{search}'s score: {scores[search]}")

else:
    print(f"{search} not found")
