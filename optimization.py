# ================================
# PRODUCT MIX OPTIMIZATION USING LINEAR PROGRAMMING
# ================================

# 1. Install & Import Libraries
!pip install pulp

import pandas as pd
import matplotlib.pyplot as plt
from pulp import LpMaximize, LpProblem, LpVariable, value

# -------------------------------
# 2. Business Problem Data
# -------------------------------

# Product data
data = {
    "Product": ["A", "B", "C"],
    "Profit_per_unit": [40, 30, 20],
    "Material_required": [2, 1, 1],
    "Labor_required": [3, 2, 1]
}

df = pd.DataFrame(data)

# Resource availability
TOTAL_MATERIAL = 100
TOTAL_LABOR = 120

# -------------------------------
# 3. Define Optimization Model
# -------------------------------

model = LpProblem("Product_Mix_Optimization", LpMaximize)

# Decision variables
units = {
    row.Product: LpVariable(f"Units_{row.Product}", lowBound=0)
    for _, row in df.iterrows()
}

# Objective Function: Maximize Profit
model += sum(
    df.loc[i, "Profit_per_unit"] * units[df.loc[i, "Product"]]
    for i in df.index
)

# Constraints
model += sum(
    df.loc[i, "Material_required"] * units[df.loc[i, "Product"]]
    for i in df.index
) <= TOTAL_MATERIAL

model += sum(
    df.loc[i, "Labor_required"] * units[df.loc[i, "Product"]]
    for i in df.index
) <= TOTAL_LABOR

# -------------------------------
# 4. Solve the Model
# -------------------------------

model.solve()

# -------------------------------
# 5. Results Table
# -------------------------------

results = []

for _, row in df.iterrows():
    product = row.Product
    optimal_units = units[product].value()
    profit = optimal_units * row.Profit_per_unit
    
    results.append({
        "Product": product,
        "Optimal Units Produced": optimal_units,
        "Profit Contribution": profit
    })

results_df = pd.DataFrame(results)

total_profit = value(model.objective)

print("Optimal Production Plan:")
display(results_df)

print(f"Total Maximum Profit: {total_profit}")

# -------------------------------
# 6. Visualization
# -------------------------------

# Bar chart: Optimal units produced
plt.figure()
plt.bar(results_df["Product"], results_df["Optimal Units Produced"])
plt.xlabel("Product")
plt.ylabel("Units Produced")
plt.title("Optimal Production Quantities")
plt.show()

# Bar chart: Profit contribution
plt.figure()
plt.bar(results_df["Product"], results_df["Profit Contribution"])
plt.xlabel("Product")
plt.ylabel("Profit")
plt.title("Profit Contribution by Product")
plt.show()
