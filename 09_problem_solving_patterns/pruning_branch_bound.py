# 09_problem_solving_patterns/pruning_branch_bound.py

# Branch and Bound for the 0/1 Knapsack problem

def knapsack_branch_and_bound(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_solution = None

    # Sort items by value/weight ratio
    items = sorted([(values[i], weights[i], i) for i in range(n)], key=lambda x: x[0]/x[1], reverse=True)

    def bound(i, current_weight, current_value):
        # Upper bound on max value reachable from item i
        if current_weight >= capacity:
            return 0
        total_value = current_value
        total_weight = current_weight
        while i < n and total_weight + items[i][1] <= capacity:
            total_weight += items[i][1]
            total_value += items[i][0]
            i += 1
        # Add fraction of next item if possible
        if i < n:
            total_value += (capacity - total_weight) * (items[i][0] / items[i][1])
        return total_value

    def backtrack(i, current_weight, current_value, taken):
        nonlocal max_value, best_solution
        if current_weight <= capacity and current_value > max_value:
            max_value = current_value
            best_solution = taken[:]
        if i == n or current_weight > capacity:
            return
        # Prune if upper bound less than max_value
        if bound(i, current_weight, current_value) <= max_value:
            return
        # Take item i
        taken.append(items[i][2])
        backtrack(i + 1, current_weight + items[i][1], current_value + items[i][0], taken)
        taken.pop()
        # Don't take item i
        backtrack(i + 1, current_weight, current_value, taken)

    backtrack(0, 0, 0, [])
    return max_value, best_solution

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_val, solution = knapsack_branch_and_bound(weights, values, capacity)
print("Max value:", max_val)
print("Items taken (indices):", solution)

