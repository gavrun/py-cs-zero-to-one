# 05_data_structures/queues_and_deques.py

from collections import deque

# Queue using deque (FIFO)

queue = deque()

# Enqueue elements
queue.append('a')
queue.append('b')
queue.append('c')

print("Queue:", queue)

# Dequeue elements
first = queue.popleft()
print("Dequeued:", first)
print("Queue after dequeue:", queue)

# Deque can be used as queue or stack

# Stack behavior (LIFO)
stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print("Stack:", stack)

top = stack.pop()
print("Popped from stack:", top)
print("Stack after pop:", stack)

# Rotate deque (useful for circular buffers)
d = deque([1, 2, 3, 4, 5])
d.rotate(2)  # rotate right by 2
print("Rotated deque right by 2:", d)

d.rotate(-3)  # rotate left by 3
print("Rotated deque left by 3:", d)

