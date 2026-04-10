# Day 07 - dictionaries: accessing keys, updating values, and looping
# opt-log | Consistency over perfection.

student = {"name": "ronan", "goal": "uc transfer", "days studied": 7}

print(student["name"])         # access by key
print(student["goal"])         # access by key
print(student["days studied"]) # access by key



student["days studied"] = 8    # update a value
student["language"] = "Python" # add a new key

print(student)  # print the whole dictionary



for key, value in student.items():
    print(key, ":", value)  # loop through dictionary


# we finished our first week YAYNESS
# start application and review next week

