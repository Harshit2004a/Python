# Python program to find the size of a Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 1st Method- using len fn
print(f"Size of the dictionary: {len(my_dict)}")

# 2nd Method- By counting keys manually
count = 0
for key in my_dict:
    count += 1
print(f"Size of the dictionary (manual count): {count}")

# Code by Harshit