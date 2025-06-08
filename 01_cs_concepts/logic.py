# 01_cs_concepts/logic.py

# Basic propositional logic using Python booleans

# Logical operators
a = True
b = False

print("AND:", a and b)  # False
print("OR:", a or b)    # True
print("NOT a:", not a)  # False
print("XOR:", a != b)   # True (exclusive or)

# Logical equivalences example: De Morgan's Laws
# not (A and B) == (not A) or (not B)
A = True
B = False

print(not (A and B) == (not A or not B))  # True

# Truth tables can be generated

def truth_table():
    print("A\tB\tA and B\tA or B\tnot A")
    for A in [True, False]:
        for B in [True, False]:
            print(f"{A}\t{B}\t{A and B}\t{A or B}\t{not A}")

truth_table()
