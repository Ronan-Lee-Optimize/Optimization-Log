# day 145 - comparing EOQ across multiple products
# opt-give | consistency over perfection.
import math
import matplotlib.pyplot as plt


def calculate_eoq(demand, order_cost, holding_cost):
    return math.sqrt((2 * demand * order_cost) / holding_cost)


def calculate_total_cost(order_qty, demand, order_cost, holding_cost):
    ordering_cost = (demand / order_qty) * order_cost
    holding_cost_total = (order_qty / 2) * holding_cost
    return ordering_cost + holding_cost_total


# multiple products, each with their own demand/cost profile
products = [
    {"name": "product A", "demand": 1200, "order_cost": 50, "holding_cost": 2},
    {"name": "product B", "demand": 800, "order_cost": 30, "holding_cost": 5},
    {"name": "product C", "demand": 3000, "order_cost": 20, "holding_cost": 1},
]


results = []
for p in products:
    eoq = calculate_eoq(p["demand"], p["order_cost"], p["holding_cost"])
    cost = calculate_total_cost(eoq, p["demand"], p["order_cost"], p["holding_cost"])
    results.append({"name": p["name"], "eoq": eoq, "cost": cost})

    print(f"{p['name']}: EOQ = {eoq:.1f} units, min cost = ${cost:.2f}")


# visualize EOQ side by side across products
names = [r["name"] for r in results]
eoqs = [r["eoq"] for r in results]


plt.bar(names, eoqs, color="mediumseagreen")
plt.title("EOQ Comparison Across Products")
plt.xlabel("product")
plt.ylabel("EOQ (units)")
plt.grid(axis="y")


# find which product needs the most frequent reordering (smallest EOQ)
smallest = min(results, key=lambda r: r["eoq"])
print()
print(f"needs most frequent reordering: {smallest['name']} (EOQ = {smallest['eoq']:.1f})")


plt.show()
