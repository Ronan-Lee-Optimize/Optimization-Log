# day 87.1 - matplotlib: multiple plots
# opt-log | consistency over perfection.

import matplotlib.pyplot as plt


subjects = ["math", "english", "korean"]

hours_this_week = [3, 5, 2]

hours_last_week = [2, 4, 3]



x = range(len(subjects))


plt.bar([i - 0.2 for i in x], hours_last_week, width=0.4, label="last week")  # shift left

plt.bar([i + 0.2 for i in x], hours_this_week, width=0.4, label="this week")  # shift right

plt.xticks(x, subjects)  # use subject names as labels

plt.title("study hours comparison")

plt.legend()

plt.show()
