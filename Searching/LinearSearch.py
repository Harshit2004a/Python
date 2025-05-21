# Program for Linear Search

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [5, 3, 8, 4, 2]
target = 4
result = linear_search(arr, target)
print(result)

# Code by Harshit