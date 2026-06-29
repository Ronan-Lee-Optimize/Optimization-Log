# day 87 - matplotlib: multiple plots
# opt-log | consistency over perfection.

import matplotlib.pyplot as plt


subjects = ["math", "english", "korean"]

hours_this_week = [3, 5, 2]

hours_last_week = [2, 4, 3]



plt.bar(subjects, hours_last_week, label="last week", alpha=0.5)    # transparency for overlap

plt.bar(subjects, hours_this_week, label="this week", alpha=0.5)    # second bar set

plt.title("study hours comparison")

plt.legend()    # show labels

plt.show()
