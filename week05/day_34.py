# day 34 - lambda functions
# opt-log | consistency over perfection.

# normal function
def add(a, b):
    return a + b


# lambda way
add2 = lambda a, b: a + b  # same thing, one line


# results
print(add(3, 5))   # 8

print(add2(3, 5))  # 8



numbers = [3, 1, 4, 1, 5, 9, 2, 6]

numbers.sort(key=lambda x: x)  # sort using lambda
print(numbers)


numbers.sort(key=lambda x: x, reverse=True) # reverse sort using lambda
print(numbers)

# friday is comingggg
