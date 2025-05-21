# Program for Binary Search (Recursive and Iterative)
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    return binary_search_recursive(arr, target, left, mid - 1)

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

print("Iterative:", binary_search_iterative(arr, target))
print("Recursive:", binary_search_recursive(arr, target, 0, len(arr) - 1))

# Code by Harshit