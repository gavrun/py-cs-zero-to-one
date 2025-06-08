# 07_python_advanced/multiprocessing_intro.py

# Multiprocessing is true parallelism using multiple CPU cores

# Great for CPU-bound tasks like data processing, numerical simulations, ML.
# Unlike threading (which is limited by GIL), each process has its own Python interpreter and memory space.

from multiprocessing import Process, Queue, cpu_count, current_process
import os

# Worker function: compute square of n and return it via Queue
def worker(q, n):
    result = n * n
    print(f"{current_process().name} computed {n}^2 = {result}")
    q.put(result)

if __name__ == '__main__':
    q = Queue()
    processes = []
    num_tasks = 5

    print("CPU count:", cpu_count())

    # Spawn multiple processes
    for i in range(num_tasks):
        p = Process(target=worker, args=(q, i), name=f"Worker-{i}")
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    # Collect results from the queue
    results = []
    while not q.empty():
        results.append(q.get())

    print("Squared numbers:", results)

# Notes 
# - Each Process runs in its own Python interpreter → true parallelism
# - Use Queue to safely share data between processes
# - Use 'if __name__ == "__main__"' to avoid recursive forking on Windows

