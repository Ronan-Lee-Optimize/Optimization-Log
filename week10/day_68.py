# day 68 - review: modules combined (applied)
# opt-log | consistency over perfection.


import random
import datetime
import math



now = datetime.datetime.now()
csat = datetime.datetime(2026, 11, 19)
dday = csat - now



score = random.randint(60, 100)


print("today is:")
print(f"{now.month}/{now.day}/{now.year}")
print()



print(f"{dday.days} days left til csat")

if dday.days < 180:
    print("im screwed HELP")
    
elif dday.days >= 180:
    print("not much time left but u still got some time")

print()

    
print(f"today's random score: {score}")
