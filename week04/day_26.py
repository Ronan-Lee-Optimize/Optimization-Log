# day 26 - review: tuples and sets
# opt-log | consistency over perfection.

# tuple: fixed, cannot be changed
goals = ("uc transfer", "ie major", "python", "gpa 4.0")
numbers = ("first", "second", "third", "fourth")


for i in range(len(goals)):
    print(f"{numbers[i]} goal: {goals[i]}")  # access both tuples by index

print()



# set: no duplicates
subjects = {"math", "english", "korean", "math", "english"}



print(f"unique subjects: {subjects}")  # duplicates removed

print(f"total: {len(subjects)}")
