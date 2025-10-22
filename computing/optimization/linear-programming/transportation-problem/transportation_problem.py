import pulp
import numpy as np


def transportation_problem(supply, demand, cost_matrix):
    origins = [f"O{i+1}" for i in range(cost_matrix.shape[0])]
    destinations = [f"D{j+1}" for j in range(cost_matrix.shape[1])]
    problem = pulp.LpProblem("Transportation_Problem", pulp.LpMinimize)
    n_origins = len(origins)
    n_destinations = len(destinations)
    variables = np.array([[pulp.LpVariable(f"x_{i}_{j}", lowBound=0, cat=pulp.LpInteger) 
                        for j in range(n_destinations)] 
                        for i in range(n_origins)])
    problem += pulp.lpSum([variables[i][j] * cost_matrix[i][j] 
                        for i in range(n_origins) 
                        for j in range(n_destinations)])
    for i in range(n_origins):
        problem += pulp.lpSum([variables[i][j] for j in range(n_destinations)]) <= supply[i]
    for j in range(n_destinations):
        problem += pulp.lpSum([variables[i][j] for i in range(n_origins)]) >= demand[j]
    problem.solve()
    return problem, origins, destinations, variables


if __name__ == "__main__":
    #costs = np.array([
    #    [17, 20, 13, 12],
    #    [15, 21, 26, 25],
    #    [15, 14, 15, 17]
    #])
    #supply = np.array([70, 90, 115])
    #demand = np.array([50, 60, 70, 95])
    #costs = np.array([
    #    [6, 8, 4],
    #    [4, 5, 8],
    #    [0, 0, 0]
    #])
    #supply = np.array([20, 20, 20])
    #demand = np.array([30, 20, 10])
    costs = np.array([
        [2, 6, 7],
        [4, 7, 5],
        [9, 8, 7]
    ])
    supply = np.array([6, 5, 9])
    demand = np.array([11, 6, 3])

    problem_solved, origins, destinations, variables = \
        transportation_problem(supply, demand, costs)
    n_origins = len(origins)
    n_destinations = len(destinations)

    print(f"Status: {pulp.LpStatus[problem_solved.status]}")
    print(f"Optimal Total Cost = {pulp.value(problem_solved.objective)}")
    print("\nOptimal Allocation:")
    allocation_matrix = np.zeros((n_origins, n_destinations))
    for i in range(n_origins):
        for j in range(n_destinations):
            allocation_matrix[i][j] = variables[i][j].varValue
            if variables[i][j].varValue > 0:
                print(f"  {origins[i]} -> {destinations[j]} = {variables[i][j].varValue}")
    print(f"\nAllocation Matrix:\n{allocation_matrix}")
    print(f"Cost Matrix:\n{costs}")
    print(f"Supply: {supply}")
    print(f"Demand: {demand}")