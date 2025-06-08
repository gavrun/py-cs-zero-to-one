# 06_algorithms/depth_first_search.py

# Depth-First Search (DFS) using adjacency list (recursive)

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

def dfs(node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)

# Example usage
dfs("A")  # A B D E F C (order may vary depending on recursion stack)
