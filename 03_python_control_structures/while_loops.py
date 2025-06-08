# 03_python_control_structures/while_loops.py


# Basic while loop
count = 0
while count < 5:
    print("Count is", count)
    count += 1

# Input loop (runs until correct input is given)
user_input = ""
while user_input != "yes":
    user_input = input("Type 'yes' to continue: ")


# Infinite loop with break
while True:
    num = int(input("Enter a positive number: "))
    if num > 0:
        break
    print("Try again with a number > 0")

# Warning: Always make sure condition will eventually become False
# Otherwise, you'll get a program that runs forever
# while True:
#     pass  # this runs forever unless externally interrupted


# Loop with continue (skips current iteration)
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue  # skip printing 3
    print(x)


# Loop with else (runs if no break)
n = 5
while n > 0:
    print("n =", n)
    n -= 1
else:
    print("Loop completed without break")


# Controlled repetition
# Use while when the number of iterations is unknown ahead of time
password = ""
attempts = 0
while password != "secret" and attempts < 3:
    password = input("Enter password: ")
    attempts += 1

if password == "secret":
    print("Access granted")
else:
    print("Too many failed attempts")


# Countdown with condition
import time

seconds = 3
while seconds > 0:
    print("Countdown:", seconds)
    time.sleep(1)
    seconds -= 1
print("Go!")

