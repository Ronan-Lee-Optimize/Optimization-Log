# day 85 - matplotlib: introduction
# opt-log | consistency over perfection.

import matplotlib.pyplot as plt


subjects = ["math", "english", "korean"]

hours = [3, 5, 2]


plt.bar(subjects, hours)

plt.title("study hours")

plt.show()
