# 07_python_advanced/coroutines.py

# Simple coroutine example 

# Coroutine via generator function (pre-async syntax)
# Useful for streaming values, incremental updates, etc.

def coroutine_example():
    total = 0
    count = 0
    average = None
    while True:
        x = yield average  # yield current result, wait for input
        if x is None:
            print("Terminating coroutine")
            break
        total += x
        count += 1
        average = total / count
        print(f"Received {x}, current average: {average}")

# Use the coroutine 
coro = coroutine_example()

# Prime the coroutine to first yield-point (start it)
next(coro)

# Send values into it
coro.send(10)     # avg: 10.0
coro.send(20)     # avg: 15.0
coro.send(30)     # avg: 20.0

# Stop coroutine by sending None
coro.send(None)   # triggers termination


