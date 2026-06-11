# day 69 - review: modules mini project
# opt-log | consistency over perfection.

import random
import math


scores = []


for i in range(5):
    score = random.randint(60, 100)
    scores.append(score)


avg = sum(scores) / len(scores)



print(f"random scores: {scores}")

print(f"avg: {avg:.2f}")

print(f"hi: {max(scores)}")

print(f"lo: {min(scores)}")

print(f"square root of avg: {math.sqrt(avg):.2f}")
