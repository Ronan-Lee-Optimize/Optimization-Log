# day 93 - review: line chart and pie chart (applied)
# opt-log | consistency over perfection.

import matplotlib.pyplot as plt


days = [1, 2, 3, 4, 5, 6, 7]
hours = [2, 3, 1, 4, 5, 3, 4]


# line chart
plt.subplot(1, 2, 1)  # 1 row, 2 columns, position 1

plt.plot(days, hours, marker="o")

plt.title("daily hours")
plt.grid(True)


# pie chart
subjects = ["math", "english", "korean"]
study = [3, 5, 2]


plt.subplot(1, 2, 2)  # position 2

plt.pie(study, labels=subjects, autopct="%1.1f%%")


plt.title("subject split")

plt.show()
