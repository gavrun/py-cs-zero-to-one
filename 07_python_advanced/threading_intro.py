# 07_python_advanced/threading_intro.py

# Threading for I/O-bound tasks and lightweight concurrency

# Due to the Global Interpreter Lock (GIL), threads in Python do not run Python bytecode in parallel.
# However, they can be useful for overlapping I/O (e.g., file, network).

import threading
import time

# Simulate a computation or I/O task
def worker(num):
    print(f"[Thread-{num}] started")
    total = 0
    for i in range(1_000_000):
        total += i
    print(f"[Thread-{num}] finished with total = {total}")

threads = []

# Launch multiple threads
for i in range(3):
    t = threading.Thread(target=worker, args=(i,), name=f"Worker-{i}")
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All threads completed\n")


# Synchronization with Lock

counter = 0
lock = threading.Lock()

def safe_increment():
    global counter
    for _ in range(100_000):
        with lock:  # ensures only one thread modifies at a time
            counter += 1

threads = []
for _ in range(5):
    t = threading.Thread(target=safe_increment)
    threads.append(t)
    t.start()

# Bonus: check thread name and current count
print("Active threads:", threading.active_count())
for t in threading.enumerate():
    print("Running:", t.name)

for t in threads:
    t.join()

print("\nFinal counter (with Lock):", counter)


# Notes
# - All threads share the same memory → protect shared data with Lock
# - GIL means threads don't run Python code truly in parallel
# - Use .start() to launch, .join() to wait

# Useful tools

# threading.current_thread().name  → debug thread identity
# threading.active_count()         → see how many threads are running
# threading.enumerate()            → get all active threads

