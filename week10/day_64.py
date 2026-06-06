# day 64 - review: math module (Applied)
# opt-log | consistency over perfection.

import math

scores = [85, 92, 78, 96, 88]

total = sum(scores)
avg = total / len(scores)



print(f"total: {total}")
print(f"average: {avg:.2f}")
print(f"rounded down: {math.floor(avg)}")
print(f"rounded up: {math.ceil(avg)}")
print(f"square root of avg: {math.sqrt(avg):.2f}")
