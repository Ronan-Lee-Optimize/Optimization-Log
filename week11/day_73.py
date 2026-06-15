# day 73 - pandas: filtering
# opt-log | consistency over perfection.

import pandas as pd

data = {"subject": ["Math", "English", "Korean", "Science"],
        "score": [85, 92, 78, 95]}

df = pd.DataFrame(data)


passed = df[df["score"] >= 90]  # filter rows where score >= 90
print(passed)

# 157 days left 🫩
