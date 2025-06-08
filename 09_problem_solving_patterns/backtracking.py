# 09_problem_solving_patterns/backtracking.py

# Backtracking is a general problem-solving technique
# It builds a solution step by step, and "backtracks" when it hits a dead end

def backtrack(path, options):
    """
    path    = current partial solution (a list)
    options = choices you can still make at this step
    """
    
    # Base case: if the path is a complete solution
    if is_solution(path):
        print("Found solution:", path)
        return

    # Try each available option
    for i, option in enumerate(options):
        # Choose the option
        path.append(option)

        # Explore further with this choice
        remaining_options = options[:i] + options[i+1:]  # avoid repeating the same element
        backtrack(path, remaining_options)

        # Undo the choice (this is the backtrack step)
        path.pop()

def is_solution(path):
    """
    Defines when a path is a valid complete solution.
    For teaching purposes, let's say a solution is a path of length 2.
    """
    return len(path) == 2  # toy condition — change as needed

# Available choices — just numbers to make it concrete
choices = [1, 2, 3]

# Start the backtracking process with an empty path
print("Starting backtracking...\n")
backtrack([], choices)

# Output:
# Found solution: [1, 2]
# Found solution: [1, 3]
# Found solution: [2, 1]
# Found solution: [2, 3]
# Found solution: [3, 1]
# Found solution: [3, 2]

# This shows all possible 2-element sequences (without repetition) from [1, 2, 3]

