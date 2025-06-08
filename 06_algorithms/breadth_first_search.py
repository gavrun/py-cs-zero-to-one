# 06_algorithms/breadth_first_search.py

# Breadth-First Search (BFS) using adjacency list (queue-based)

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

def bfs(start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(graph[node])

# Example usage

bfs("A")  # Starting from node 'A' or B C D E F
