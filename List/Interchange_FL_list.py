def interchange_elements(lst, idx1, idx2):
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
    return lst

# Example usage:
numbers = [10, 20, 30, 40, 50]
# Swap elements at index 1 and 3
interchanged = interchange_elements(numbers, 1, 3)
print(interchanged)  # Output: [10, 40, 30, 20, 50]

# Code by Harshit