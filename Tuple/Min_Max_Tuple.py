# Python – Maximum and Minimum K elements in Tuple

def max_min_k_elements(tup, k):
    sorted_tup = sorted(tup)
    min_k = sorted_tup[:k]
    max_k = sorted_tup[-k:]
    return min_k, max_k

tup = (5, 20, 3, 7, 6, 8)
k = 2
min_k, max_k = max_min_k_elements(tup, k)
print(f"Minimum {k} elements: {min_k}")
print(f"Maximum {k} elements: {max_k}")

# Code by Harshit