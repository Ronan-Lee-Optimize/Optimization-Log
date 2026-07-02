# day 90 - matplotlib: pie chart
# opt-log | consistency over perfection.

import matplotlib.pyplot as plt


subjects = ["math", "english", "korean", "social studies"]
hours = [5, 3, 2, 4]


plt.pie(hours, labels=subjects, autopct="%1.1f%%")  # show percentages

plt.title("study hours distribution")
plt.show()
