# day 127 - bridge week: reimplementing pandas filtering in pure python (applied)
# opt-log | Consistency over perfection.

# same shape of data pandas would hold, but as a plain list of dicts
logs = [
    {"subject": "", "hours": 4},
    {"subject": "english", "hours": 2},
    {"subject": "korean", "hours": 3},
]

# pandas equivalent: df[df["hours"] > 2]
# doing it by hand with a for loop and an if check
long_sessions = []
for entry in logs:
    if entry["hours"] > 2:
        long_sessions.append(entry)


print("sessions over 2 hours:")
for entry in long_sessions:
    print(entry)


# pandas equivalent: df[df["subject"] == "math"]
math_only = []
for entry in logs:
    if entry["subject"] == "math":
        math_only.append(entry)


print()
print("math sessions only:")
for entry in math_only:
    print(entry)
