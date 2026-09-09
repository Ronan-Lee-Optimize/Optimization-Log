# day 143 - new project: EOQ with user input
# opt-log | consistency over perfection.
import math
import matplotlib.pyplot as plt


def calculate_eoq(demand, order_cost, holding_cost):
    return math.sqrt((2 * demand * order_cost) / holding_cost)


def calculate_total_cost(order_qty, demand, order_cost, holding_cost):
    ordering_cost = (demand / order_qty) * order_cost
    holding_cost_total = (order_qty / 2) * holding_cost
    return ordering_cost + holding_cost_total


# get the scenario from the user instead of hardcoding it
print("let's calculate your own EOQ scenario:")
annual_demand = int(input("annual demand (units): "))
cost_per_order = float(input("cost per order ($): "))
holding_cost_per_unit = float(input("holding cost per unit per year ($): "))


eoq = calculate_eoq(annual_demand, cost_per_order, holding_cost_per_unit)
eoq_cost = calculate_total_cost(eoq, annual_demand, cost_per_order, holding_cost_per_unit)


print()
print(f"optimal order quantity: {eoq:.1f} units")
print(f"minimum total cost: ${eoq_cost:.2f}")


# build the curve around whatever the user entered
max_range = int(eoq * 3)
quantities = range(10, max_range, 5)
costs = []

for qty in quantities:
    cost = calculate_total_cost(qty, annual_demand, cost_per_order, holding_cost_per_unit)
    costs.append(cost)


plt.plot(quantities, costs, label="total cost")
plt.scatter([eoq], [eoq_cost], color="red", zorder=5, label=f"EOQ = {eoq:.0f}")

plt.title("Total Cost vs Order Quantity (your scenario)")
plt.xlabel("order quantity")
plt.ylabel("total cost ($)")
plt.legend()

plt.grid(True)
plt.show()
