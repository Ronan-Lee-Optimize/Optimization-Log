# day 141 - new project: EOQ core calculation logic
# opt-log | consistency over perfection.
import math


def calculate_eoq(demand, order_cost, holding_cost):

    # EOQ formula: sqrt( (2 * demand * order_cost) / holding_cost )
    eoq = math.sqrt((2 * demand * order_cost) / holding_cost)

    return eoq


def calculate_total_cost(order_qty, demand, order_cost, holding_cost):

    # ordering cost: how many times you order per year * cost per order
    ordering_cost = (demand / order_qty) * order_cost

    # holding cost: average inventory level * cost to hold one unit
    holding_cost_total = (order_qty / 2) * holding_cost

    return ordering_cost + holding_cost_total


# example scenario: a small shop selling one product
annual_demand = 1200      # units needed per year
cost_per_order = 50       # cost to place one order
holding_cost_per_unit = 2 # cost to hold one unit for a year


eoq = calculate_eoq(annual_demand, cost_per_order, holding_cost_per_unit)
min_cost = calculate_total_cost(eoq, annual_demand, cost_per_order, holding_cost_per_unit)


print(f"optimal order quantity (EOQ): {eoq:.1f} units")
print(f"total cost at EOQ: ${min_cost:.2f}")
