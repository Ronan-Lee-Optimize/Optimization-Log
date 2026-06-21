# day 79 - review: pandas filtering (applied)
# opt-log | consistency over perfection.

import pandas as pd

data = {"subject": ["math", "english", "korean", "social studies"],
        "hours": [0.5, 1, 2, 4]}


df = pd.DataFrame(data)


studied_alot = df[df["hours"] >= 3]
studied_less = df[df["hours"] < 3]



print("studied a lot:")
print(studied_alot)
print()

print("more time needed:")
print(studied_less)
