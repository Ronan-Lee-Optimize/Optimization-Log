# day 144 - New project: EOQ scenarios saved to csv
# opt-log | consistency over perfection.
import math
import pandas as pd
from datetime import date


def calculate_eoq(demand, order_cost, holding_cost):
    return math.sqrt((2 * demand * order_cost) / holding_cost)


def calculate_total_cost(order_qty, demand, order_cost, holding_cost):
    ordering_cost = (demand / order_qty) * order_cost
    holding_cost_total = (order_qty / 2) * holding_cost

    return ordering_cost + holding_cost_total


print("let's calculate and save an EOQ scenario:")

scenario_name = input("scenario name (e.g. 'shop A'): ")
annual_demand = int(input("annual demand (units): "))
cost_per_order = float(input("cost per order ($): "))
holding_cost_per_unit = float(input("holding cost per unit per year ($): "))


eoq = calculate_eoq(annual_demand, cost_per_order, holding_cost_per_unit)
eoq_cost = calculate_total_cost(eoq, annual_demand, cost_per_order, holding_cost_per_unit)


print()
print(f"optimal order quantity: {eoq:.1f} units")
print(f"minimum total cost: ${eoq_cost:.2f}")


# build a new row for this scenario
new_row = pd.DataFrame({
    "date": [date.today()],
    "scenario": [scenario_name],
    "demand": [annual_demand],
    "order_cost": [cost_per_order],
    "holding_cost": [holding_cost_per_unit],
    "eoq": [round(eoq, 1)],
    "min_cost": [round(eoq_cost, 2)]
})


# try to load existing scenarios, or start fresh if the file doesn't exist yet
try:
    df_old = pd.read_csv("eoq_scenarios.csv")
    df_all = pd.concat([df_old, new_row], ignore_index=True)

except FileNotFoundError:
    df_all = new_row

df_all.to_csv("eoq_scenarios.csv", index=False)


print()
print("all saved scenarios so far:")
print(df_all)
