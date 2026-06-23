# day 81 - review: pandas groupby (applied)
# opt-log | consistency over perfection.


import pandas as pd


data = {"subject": ["math", "math", "english", "english", "korean"],
        "hours": [2, 3, 1, 2, 4]}


df = pd.DataFrame(data)


total_hours = df.groupby("subject")["hours"].sum()  # total per subject

print(total_hours)
