# Python program to swap two elements in a list

def swap_elements(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst

# Example usage
my_list = [1, 2, 3, 4]
print("Original List:", my_list)
print("Swap list:",(swap_elements(my_list, 1, 3)))  # Output: [1, 4, 3, 2]

# Code by Harshit