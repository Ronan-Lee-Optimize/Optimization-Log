# day 78 - review: pandas DataFrame basics (applied)
# opt-log | consistency over perfection.

import pandas as pd

data = {"subject": ["math", "english", "korean", "social studies"],
        "hrs": [1, 2, 3, 5]}

df = pd.DataFrame(data)

print("<dataframe>")
print()
print(df)
for i in range(2):
    print()
print("summary")
print()
print(f"total hrs: {df['hrs'].sum()}")
print(f"avg hrs: {df['hrs'].mean()}")

# TADC EP9 FINALLY CAME OUTTTTT
