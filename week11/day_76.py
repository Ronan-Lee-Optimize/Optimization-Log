# day 76 - pandas: groupby
# opt-log | consistency over perfection.

import pandas as pd

data = {"subject": ["math", "math", "english", "english"],
        "score": [85, 90, 78, 88]}


df = pd.DataFrame(data)



grouped = df.groupby("subject")["score"].mean()  # average score per subject
print(grouped)
