# 01_cs_concepts/memory_ram.py

# Memory Model


# Memory is a finite, addressable space used to store data and instructions
# Think of it as a long array of bytes, each with a numeric address

# Example (conceptual, not a code):

# Address    | Value
# -----------|-------
# 0x1000     | 0x1A
# 0x1001     | 0xFF
# 0x1002     | 0x00
# ...

# Values are stored in binary and interpreted based on type and context


# There are different *regions* in memory layout:

# 1. Code/Text segment – stores program instructions
# 2. Stack – for function calls and local variables (LIFO)
# 3. Heap – for dynamic memory (objects, lists, etc.)
# 4. Static/Global – fixed-size data known at compile time


# Example stack vs heap (abstract illustration):

# Stack:
#   [func_b frame]
#   [func_a frame]
#   [main frame]

# Heap:
#   object_1 @ 0x4000
#   object_2 @ 0x4010


# References (or Pointers) store memory addresses, not data itself
# Dereferencing a pointer gives access to the value at that address.
# Example: 
# x = ref(0x4000) means "x refers to value at address 0x4000"


# Mutable vs Immutable:
# - Mutable: object in memory can be modified (e.g., array)
# - Immutable: changing value creates new allocation (e.g., integers, strings)


# Virtual memory: OS gives each process its own address space


# Memory management strategies:
# - Manual allocation (e.g., malloc/free in C)
# - Automatic garbage collection (e.g., in Python, Java)
# - Reference counting (track how many references exist to an object)
# - Tracing GC (find unreachable objects in memory graph)


# CPU accesses memory using Memory Address Register (MAR) and
# Memory Data Register (MDR) in the hardware architecture

# Cache: fast memory closer to CPU (L1/L2/L3)

# Paging & segmentation: memory divided into blocks for efficiency

# Alignment: data placed at memory boundaries (e.g., 4-byte aligned)

# Important terms:
# - RAM: volatile memory used during program execution
# - Address space: range of valid addresses a process can use
# - Segmentation fault: invalid memory access (e.g., accessing NULL)
# - Memory leak: memory allocated but never freed


# Memory is central to performance, correctness, and safety in software.
# Understanding memory model is essential for debugging,
# optimization, and writing performant programs


