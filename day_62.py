# day 62 - modules: combined
# opt-log | consistency over perfection.

import random
import datetime
import math

now = datetime.datetime.now()
print(f"date: {now.year}-{now.month}-{now.day}")

score = random.randint(70, 100)
print(f"today's random score: {score}")

print(f"square root of score: {math.sqrt(score):.2f}")  # 2 decimal places
