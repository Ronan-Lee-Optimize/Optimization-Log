# day 89 - matplotlib + pandas combined
# opt-log | consistency over perfection.

import pandas as pd
import matplotlib.pyplot as plt


data = {"subject": ["math", "english", "korean", "social studies"],
        "hours": [2, 1, 4, 5
                  ]}

df = pd.DataFrame(data)


plt.bar(df["subject"], df["hours"])  # use DataFrame columns directly

plt.title("study hours by subject")
plt.xlabel("subject")
plt.ylabel("hours")

plt.show()
