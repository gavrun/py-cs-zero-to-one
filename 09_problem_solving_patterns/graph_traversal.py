# 09_problem_solving_patterns/graph_traversal.py

# Different graph traversal strategies overview

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Depth-First Search (DFS) iterative implementation
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            # Add neighbors to stack
            stack.extend(reversed(graph[vertex]))  # reverse for consistent order

# Breadth-First Search (BFS) iterative implementation
from collections import deque

def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            queue.extend(graph[vertex])

print("DFS iterative from A:")
dfs_iterative(graph, 'A')

print("\nBFS iterative from A:")
bfs_iterative(graph, 'A')


