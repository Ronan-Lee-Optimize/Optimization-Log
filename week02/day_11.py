# day 11 - review day 04: while loop (applied)
# opt-log | consistency over perfection.

total = 0
day = 1

print("input time u studied this week(every single day)")



while day <= 7:

    hours = int(input("how many hrs did you study?"))


    total += hours  # add to total
    day += 1        # move to next day


print()
print("total amount this week:", total)
print("daily avg:", total / 7, "hrs")  # calculate average
