# day 66 - review: datetime module (Applied)
# opt-log | consistency over perfection.

import datetime


now = datetime.datetime.now()
csat = datetime.datetime(2026, 11, 19) # CSAT DAY



dday = csat - now
print(f"today: {now.year}-{now.month}-{now.day}")
print(f"days until CSAT: {dday.days}")
