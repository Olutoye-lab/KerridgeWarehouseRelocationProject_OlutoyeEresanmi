import pulp

# n - number of items

def boxSolver( n , case_weights, case_volumes, W_max, V_max):
    # Create the Linear Program (LP) problem
    prob = pulp.LpProblem("Minimize Boxes", pulp.LpMinimize)

    # Decision Variables
    # x_ij = 1 if item i is placed in box j, 0 otherwise
    x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

    # y_j = 1 if box j is used, 0 otherwise
    y = pulp.LpVariable.dicts("y", range(n), cat='Binary')

    # Objective: Minimize the number of boxes used
    prob += pulp.lpSum(y[j] for j in range(n)), "Minimize Number of Boxes"

    # Constraints

    # Each item must be placed in exactly one box
    for i in range(n):
        prob += pulp.lpSum(x[i, j] for j in range(n)) == 1, f"Item_{i}_Assigned"

    # The total weight in each box must not exceed the weight limit
    for j in range(n):
        prob += pulp.lpSum(case_weights[i] * x[i, j] for i in range(n)) <= W_max * y[j], f"Box_{j}_Weight_Limit"

    # The total volume in each box must not exceed the volume limit
    for j in range(n):
        prob += pulp.lpSum(case_volumes[i] * x[i, j] for i in range(n)) <= V_max * y[j], f"Box_{j}_Volume_Limit"

    # If a box is used, at least one item must be placed in it
    for j in range(n):
        prob += pulp.lpSum(x[i, j] for i in range(n)) >= y[j], f"Box_{j}_Used_If_Item_Assigned"

    # Solve the problem
    return x, y, prob
