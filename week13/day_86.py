# day 86 - matplotlib: line chart
# opt-log | consistency over perfection.

import matplotlib.pyplot as plt


days = [1, 2, 3, 4, 5]

hours = [2, 3, 1, 4, 5]



plt.plot(days, hours)  # line chart

plt.title("study hours over days")

plt.xlabel("day")

plt.ylabel("hours")

plt.xticks([1, 2, 3, 4, 5])  # force integer ticks

plt.show()
