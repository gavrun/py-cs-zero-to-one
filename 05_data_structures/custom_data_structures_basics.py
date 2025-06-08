# 05_data_structures/custom_data_structures_basics.py

# Basic implementation of custom data structures

# Singly linked list node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Singly linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def to_list(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values

# Usage

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
print("LinkedList contents:", ll.to_list())

# Basic binary tree node
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Simple insertion (binary search tree property not enforced here)
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

print("Root:", root.value)
print("Left child:", root.left.value)
print("Right child:", root.right.value)

