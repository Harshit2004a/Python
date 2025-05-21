# 1- Using dict.get() method
my_dict = {'a': 1, 'b': 2}
value = my_dict.get('c', 'default_value')  # Returns default_value if c is missing
print(value)

# 2- Using collections.defaultdict
from collections import defaultdict
default_dict = defaultdict(int)  # Default value is 0 for missing keys
default_dict['x'] += 1  # No KeyError x is set to 1
print(default_dict)

# Code by Harshit