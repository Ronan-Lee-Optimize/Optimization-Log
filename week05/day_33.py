# day 33 - list comprehension
# opt-log | consistency over perfection.

numbers = [1, 2, 3, 4, 5]

# normal way
doubled = []

for n in numbers:
    doubled.append(n * 2)  # add each doubled value



# list comprehension way
doubled2 = [n * 2 for n in numbers]  # same thing, one line

print(doubled)   # [2, 4, 6, 8, 10]

print(doubled2)  # [2, 4, 6, 8, 10]

# can get the same results
