# day 27 - review: while loop applied
# opt-log | consistency over perfection.

total = 0
count = 0

while True:
    score = int(input("enter score (-1 to stop): "))
    
    if score == -1:
        break              # exit the loop
    
    total += score        # add to total
    count += 1            # count entries

print()


print(f"total scores entered: {count}")

print(f"sum: {total}")

print(f"avg: {total / count}")  # calculate average
