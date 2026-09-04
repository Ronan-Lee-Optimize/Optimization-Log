# day 142 - new project: EOQ visualization with matplotlib
# opt-log | consistency over perfection.
import math
import matplotlib.pyplot as plt


def calculate_eoq(demand, order_cost, holding_cost):
    return math.sqrt((2 * demand * order_cost) / holding_cost)


def calculate_total_cost(order_qty, demand, order_cost, holding_cost):
    ordering_cost = (demand / order_qty) * order_cost
    holding_cost_total = (order_qty / 2) * holding_cost
    return ordering_cost + holding_cost_total


annual_demand = 1200
cost_per_order = 50
holding_cost_per_unit = 2


eoq = calculate_eoq(annual_demand, cost_per_order, holding_cost_per_unit)


# try a range of order quantities and calculate total cost for each
quantities = range(10, 300, 5)
costs = []

for qty in quantities:
    cost = calculate_total_cost(qty, annual_demand, cost_per_order, holding_cost_per_unit)
    costs.append(cost)


plt.plot(quantities, costs, label="total cost")


# mark the EOQ point on the curve
eoq_cost = calculate_total_cost(eoq, annual_demand, cost_per_order, holding_cost_per_unit)
plt.scatter([eoq], [eoq_cost], color="red", zorder=5, label=f"EOQ = {eoq:.0f}")


plt.title("total cost vs order quantity")
plt.xlabel("order quantity")
plt.ylabel("total cost ($)")
plt.legend()
plt.grid(True)
plt.show()

print(f"EOQ: {eoq:.1f} units, minimum cost: ${eoq_cost:.2f}")
