# 01_cs_concepts/complexity_classes.py

# Complexity classes

# P (Polynomial time)
# Problems solvable in polynomial time by deterministic algorithms
# Example: sorting (O(n log n)), searching (O(n)), etc.

# NP (Nondeterministic Polynomial time)
# Problems verifiable in polynomial time
# Includes problems like the Boolean satisfiability problem (SAT)

# NP-Complete
# Hardest problems in NP
# If any NP-Complete problem is in P, then P = NP (open problem)

# NP-Hard
# At least as hard as NP-Complete; not necessarily in NP


# Example functions illustrating polynomial vs exponential growth:

def polynomial_time(n):
    # O(n^3)
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                count += 1
    return count

def exponential_time(n):
    # O(2^n)
    if n == 0:
        return 1
    else:
        return exponential_time(n-1) + exponential_time(n-1)

print("Polynomial time with n=10:", polynomial_time(10))

# Warning: exponential_time(10) grows very fast; avoid large n

# Uncomment to test, but it may take long
# print("Exponential time with n=5:", exponential_time(5))
# print("Exponential time with n=10:", exponential_time(10))

