# day 92 - review: matplotlib basics - chili (applied)
# opt-log | consistency over perfection.

import matplotlib.pyplot as plt


ingredients = ["tomato", "herbs", "meat", "tomato sauce"]
quantity = [3, 2, 4, 5]


plt.bar(ingredients, quantity, color="steelblue")  # add color


plt.title("quantity of ingredients")
plt.xlabel("ingredient")
plt.ylabel("quantity") 


plt.grid(axis="y")  # horizontal grid lines only

plt.show()

# 🌶️
