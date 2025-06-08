# 05_data_structures/heap_priority_queue.py

import heapq

# Heap as a priority queue (min-heap by default)

heap = []

# Push elements with priority
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)

print("Heap elements:", heap)  # [1, 5, 3] internal structure

# Pop smallest element
smallest = heapq.heappop(heap)
print("Smallest element:", smallest)  # 1

print("Heap after pop:", heap)

# Convert list to heap
data = [7, 2, 9, 4]
heapq.heapify(data)
print("Heapified data:", data)

# Pop all elements in sorted order
sorted_data = [heapq.heappop(data) for _ in range(len(data))]
print("Sorted elements:", sorted_data)

# Use heap for priority queue with (priority, item)
pq = []
heapq.heappush(pq, (2, 'task2'))
heapq.heappush(pq, (1, 'task1'))
heapq.heappush(pq, (3, 'task3'))

while pq:
    priority, task = heapq.heappop(pq)
    print(f"Processing {task} with priority {priority}")

