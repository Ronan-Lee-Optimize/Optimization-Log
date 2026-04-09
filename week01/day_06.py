# day 06 - lists, append, remove and for loop
# opt-log | consistency over perfection

subjects = ["math", "english", "korean", "science"]


print(subjects)         # print the whole list
print(subjects[0])      # first item (index starts at 0)
print(subjects[-1])     # last item



subjects.append("history") # add an item to the and
print(subjects)

subjects.remove("math")    # remove an item
print(subjects)



# application

for subject in subjects:
    print("studying:", subject) # loop through the list


# the week is almost over babeeeee
