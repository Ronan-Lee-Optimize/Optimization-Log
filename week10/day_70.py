# day 70 - week 10 wrap-up: CSAT dashboard
# opt-log | consistency over perfection.

import random
import datetime
import math
import os



now = datetime.datetime.now()

csat = datetime.datetime(2026, 11, 19)

dday = csat - now


subjects = ["math", "english", "korean", "science", "history"]
pick = random.choice(subjects)



files = os.listdir()
py_files = [f for f in files if f.endswith(".py")]



print("=== 수능 Dashboard ===")
print()
print("today is:")
print(f"{now.month}/{now.day}/{now.year}")
print()
print(f"-> {dday.days} days left til 수능")
print()
print()
print(f"today's subject: {pick}")
print(f"total study files: {len(py_files)}")
print(f"avg days left per file: {math.floor(dday.days / len(py_files))}")
print()
print("keep grinding buddy 👍")
