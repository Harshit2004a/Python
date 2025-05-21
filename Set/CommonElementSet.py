# Check if two sets have atleast one element common

def have_common_element(set1, set2):
    return not set1.isdisjoint(set2)

a = {1, 2, 3}
b = {3, 4, 5}
print(have_common_element(a, b))  
# Output: True

# Code by Harshit