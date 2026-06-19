# day 77 - pandas: sandwich ingredients
# opt-log | consistency over perfection.

import pandas as pd

data = {"things to buy": ["tomato", "bread", "cheese", "salami","milk","lettuce","ranch dressing"],
        "pack(piece)": [1, 2, 4, 3, 2, 1, 2]}


df = pd.DataFrame(data)


sorted_df = df.sort_values("pack(piece)", ascending=False)  # sort by score, high to low

print(sorted_df)
