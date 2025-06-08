# 06_algorithms/depth_first_traversal_filetree.py

import os

# Recursive function to print a directory tree

def print_tree(startpath, prefix=""):
    tree_lines = []

    # Sort the list of files and folders to print them in order
    files = sorted(os.listdir(startpath))  # ← this is where sorting happens
    files_count = len(files)

    # Iterate over each item
    for index, name in enumerate(files):
        path = os.path.join(startpath, name)  # Full path to the item
        is_last = index == files_count - 1    # Check if it's the last item in the list

        # Connectors: "├──", "└──", "│", "    ", etc.
        # Choose the appropriate tree branch symbol
        connector = "└── " if is_last else "├── "

        # Print the current item with the prefix
        # print(prefix + connector + name)
        tree_lines.append(prefix + connector + name)

        # Check if the item is a directory (i.e., has children) and recurse into it
        if os.path.isdir(path):
            # Recursive call that performs a depth-first traversal (DFS)
            extension = "    " if is_last else "│   "
            subtree = print_tree(path, prefix + extension)  # ← recursive call
            tree_lines.extend(subtree.splitlines())
    
    return "\n".join(tree_lines)


# if __name__ == "__main__":
#     root = "/path/folder"
#     print(os.path.basename(root) + "/")
#     print(print_tree(root))

print(print_tree('./'))

