# 03_python_control_structures/break_continue_pass.py

# break: exit the loop
for i in range(10):
    if i == 5:
        break
    print(i)  # prints 0 to 4

# continue: skip current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # skips 2

# pass: do nothing (placeholder)
for i in range(3):
    pass  # used when code is required syntactically but nothing should happen

# Example: placeholder for future function
def todo():
    pass

