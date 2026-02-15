# OPTIMIZATION_MODEL

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: VITTALA BHAVYA SREE

*INTERN ID*: CTIS4692

*DOMAIN*: DATA SCIENCE

*DURATION*: 8 WEEKS

*MENTOR*: NEELA SANTOSH

*DESCRIPTION*: Optimization is a critical tool in business decision-making, allowing organizations to allocate limited resources efficiently to maximize profits or minimize costs. This project demonstrates how a real-world business problem can be modeled and solved using optimization techniques, specifically Linear Programming (LP), and implemented in Python using the PuLP library. The scenario selected is a product mix optimization problem for a manufacturing company producing multiple products with limited raw materials and labor.

In this business scenario, the company manufactures three products: A, B, and C. Each product requires a different amount of raw material and labor hours, and each has a distinct profit contribution. The company has constraints: a fixed amount of raw materials available per week and a limited number of labor hours that cannot be exceeded. The goal is to determine how many units of each product to produce to maximize the company’s total profit while satisfying these constraints. This type of problem is well-suited for linear programming because both the objective function (profit) and the constraints (resources) are linear functions of the decision variables (product quantities).

The problem setup involves defining decision variables representing the number of units to produce for each product. The objective function is formulated as the total profit, expressed as a linear combination of decision variables multiplied by their respective profit contributions. The constraints include material availability and labor limitations, ensuring that the total resources used by all products do not exceed the available quantities. Additional constraints, such as non-negativity (cannot produce a negative quantity), are included to make the model realistic.

Implementation in Python is straightforward using PuLP. First, we import the library and define the decision variables. Next, the objective function is set up to maximize total profit. Then, constraints are added according to the available resources. The model is solved using PuLP’s default solver, and the optimal production quantities for each product are obtained. The solution also provides insights such as which products contribute most to profit and which constraints are binding, i.e., limiting production.

The insights from the solution are crucial for business strategy. For instance, if the solution shows that one product should not be produced at all, it indicates that it is not cost-effective given the current resource limitations. On the other hand, products with higher profitability per unit of resource may dominate the production schedule. Managers can use these insights to make informed decisions, such as negotiating for additional raw materials or adjusting labor allocation. Sensitivity analysis can further reveal how changes in resource availability or profit margins affect the optimal production plan, helping the company plan for uncertainty and growth.

In conclusion, this project demonstrates the practical application of optimization in business using linear programming. By formulating the problem mathematically and solving it with Python, we can provide actionable insights that directly influence profitability and efficiency. The notebook includes all steps: problem setup, mathematical modeling, Python implementation, solution interpretation, and strategic recommendations, making it a comprehensive guide for decision-making in resource-constrained business environments.

If you want, I can also provide the complete Python notebook code using PuLP for this exact scenario with sample data, all ready to run in one go. It will include the problem setup, solution, and a clear output of optimal production and profits.

# OUTPUT

<img width="903" height="220" alt="Image" src="https://github.com/user-attachments/assets/a4e87bcc-fa22-43e0-b116-aea653760c9d" />

<img width="682" height="545" alt="Image" src="https://github.com/user-attachments/assets/8c57c337-a9ac-4f91-bd72-422b804013b7" />

<img width="701" height="544" alt="Image" src="https://github.com/user-attachments/assets/c3c1e17b-28bf-40f0-aabf-db06f706abc5" />
