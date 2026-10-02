# day 146 - new project: input validation and error handling
# opt-log | consistency over perfection.
import math
import matplotlib.pyplot as plt


def calculate_eoq(demand, order_cost, holding_cost):
    return math.sqrt((2 * demand * order_cost) / holding_cost)


def calculate_total_cost(order_qty, demand, order_cost, holding_cost):
    ordering_cost = (demand / order_qty) * order_cost
    holding_cost_total = (order_qty / 2) * holding_cost
    return ordering_cost + holding_cost_total


def get_positive_int(message):
    # keep asking until the user gives a valid positive whole number
  
    while True:
        try:
            value = int(input(message))
            if value <= 0:
                print("please enter a number greater than 0")
                continue
            return value
        except ValueError:
            print("that's not a valid number, try again")


def get_positive_float(message):
    # keep asking until the user gives a valid positive number
    while True:
        try:
            value = float(input(message))
            if value <= 0:
                print("please enter a number greater than 0")
                continue
            return value
        except ValueError:
            print("that's not a valid number, try again")


print("let's calculate your own EOQ scenario:")


annual_demand = get_positive_int("annual demand (units): ")
cost_per_order = get_positive_float("cost per order ($): ")
holding_cost_per_unit = get_positive_float("holding cost per unit per year ($): ")


eoq = calculate_eoq(annual_demand, cost_per_order, holding_cost_per_unit)
eoq_cost = calculate_total_cost(eoq, annual_demand, cost_per_order, holding_cost_per_unit)

print()
print(f"optimal order quantity: {eoq:.1f} units")
print(f"minimum total cost: ${eoq_cost:.2f}")


max_range = int(eoq * 3)
quantities = range(10, max(max_range, 60), 5)
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
