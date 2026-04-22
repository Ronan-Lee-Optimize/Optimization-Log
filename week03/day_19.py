# day 19 - nested dictionaries
# opt-log | consistency over perfection.

students = {
    "ronan": {
        "goal": "uc transfer",   # nested dict
        "days_studied": 19
    },
    "lexus": {
        "goal": "uc berkley",
        "days_studied": 5
    }
}

print(students["ronan"]["goal"])        # access nested value
print(students["lexus"]["days_studied"]) # access nested value

for name, info in students.items():
    print(name, "-", info["goal"])      # loop through nested dict

