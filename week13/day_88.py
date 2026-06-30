# day 88 - matplotlib: line chart applied
# opt-log | consistency over perfection.

import matplotlib.pyplot as plt


days = [1, 2, 3, 4, 5, 6, 7]
hours = [2, 3, 1, 4, 5, 3, 4]


plt.plot(days, hours, marker="o")  # add dots at each point

plt.title("week 13 study hours")
plt.xlabel("day")
plt.ylabel("hours")

plt.grid(True)  # add grid lines

plt.show()
