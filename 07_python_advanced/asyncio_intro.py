# 07_python_advanced/asyncio_intro.py

import asyncio

# Basics

# Coroutines are defined with 'async def'
# Use 'await' to pause and let other tasks run

async def say_after(delay, message):
    await asyncio.sleep(delay)
    print(message)

# Main async entry point
async def main():
    print("Start")

    # Schedule two coroutines concurrently
    task1 = asyncio.create_task(say_after(1, "Hello"))
    task2 = asyncio.create_task(say_after(2, "World"))

    # Wait for both tasks to complete
    await task1
    await task2

    print("Done")

# Run the async program 
asyncio.run(main()) 

# asyncio.run(...) starts the event loop and runs until complete
# create_task(...) schedules coroutine in the background
# await suspends execution until the task finishes


# Run multiple coroutines in parallel

async def fetch(n):
    await asyncio.sleep(n)
    print(f"Fetched in {n}s")
    return n

async def parallel_tasks():
    results = await asyncio.gather(
        fetch(1),
        fetch(2),
        fetch(3)
    )
    print("All done:", results)

# asyncio.run(parallel_tasks()) # ERR, cannot be called more than once at a time in REPL or scripts


# Sequential vs Parallel

async def sequential():
    await say_after(1, "First")
    await say_after(2, "Second")

async def parallel():
    task1 = asyncio.create_task(say_after(1, "First"))
    task2 = asyncio.create_task(say_after(2, "Second"))
    await task1
    await task2

# asyncio.run(sequential())  # This takes ~3 seconds
# asyncio.run(parallel())    # This takes ~2 seconds


# Don't forget to await coroutines!

async def run_oops():
    coro = say_after(1, "Oops")  # nothing happens until awaited
    await coro  # now it runs

# asyncio.run(run_oops())

# Don't block with time.sleep() — it freezes the loop!

