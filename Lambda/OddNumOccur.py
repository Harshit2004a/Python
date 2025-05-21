# The Number Occurring Odd Number of Times

from functools import reduce
arr = [1, 2, 3, 2, 3, 1, 3]

print("Number occurring odd number of times:", reduce(lambda x, y: x ^ y, arr))

# Code by Harshit