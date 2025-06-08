# 09_problem_solving_patterns/greedy_algorithm.py

# Greedy: make the best choice at each step

# Example: coin change (smallest number of coins)
def min_coins(amount, coins):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count if amount == 0 else -1

# Example usage
coins = [1, 5, 10, 25]
print(min_coins(37, coins))  # 4 (25 + 10 + 1 + 1)

# Greedy may not give optimal solution for all problems
# Works well when local optimum leads to global optimum

