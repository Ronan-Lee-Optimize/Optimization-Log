# day 75 - pandas: sorting
# opt-log | consistency over perfection.

import pandas as pd

data = {"subject": ["math", "english", "korean", "science"],
        "score": [85, 92, 78, 95]}


df = pd.DataFrame(data)


sorted_df = df.sort_values("score", ascending=False)  # sort by score, high to low
print(sorted_df)
