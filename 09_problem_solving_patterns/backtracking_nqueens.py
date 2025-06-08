# 09_problem_solving_patterns/backtracking_nqueens.py

# N-Queens problem using backtracking
# Goal: Place N queens on an N x N chessboard so that no two queens attack each other

def is_safe(board, row, col):
    """
    Checks if it's safe to place a queen at board[row][col].
    A queen can attack vertically and diagonally.
    """
    # Check vertical (same column)
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal (↖)
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal (↗)
    i, j = row - 1, col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, solutions):
    """
    Tries placing a queen in every column of the current row.
    If it's safe, recursively proceed to the next row.
    If not, backtrack and try the next column.
    """
    if row == len(board):
        # Base case: All queens are placed successfully
        # Store a deep copy of the current board configuration
        solutions.append(["".join(r) for r in board])
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            # Place a queen
            board[row][col] = 'Q'
            # Move on to the next row
            solve_n_queens(board, row + 1, solutions)
            # Remove the queen (backtrack)
            board[row][col] = '.'

def print_solutions(solutions):
    """
    Prints all valid solutions to the N-Queens problem
    """
    for idx, solution in enumerate(solutions, 1):
        print(f"\nSolution {idx}:")
        for row in solution:
            print(row)

# Board size (N x N)
N = 4

# Initialize empty board ('.' means empty cell)
board = [['.' for _ in range(N)] for _ in range(N)]

# List to store all valid solutions
solutions = []

# Start backtracking algorithm from the first row
solve_n_queens(board, 0, solutions)

# Print all the solutions found
print_solutions(solutions)

# Output:
# Solution 1:
# .Q..
# ...Q
# Q...
# ..Q.

# Solution 2:
# ..Q.
# Q...
# ...Q
# .Q..
