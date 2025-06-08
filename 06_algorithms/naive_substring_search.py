# 06_algorithms/naive_substring_search.py

def naive_substring_search(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            return i  # Return first occurrence index
    return -1  # Not found

text = "hello world"
pattern = "world"
index = naive_substring_search(text, pattern)
print(index)  # 6

pattern2 = "python"
index2 = naive_substring_search(text, pattern2)
print(index2)  # -1

