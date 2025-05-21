my_list = [1, 2, 3, 4, 5]

# Method 1: len() function
print("Length using len():", len(my_list))

# Method 2: loop
length = 0
for _ in my_list:
    length += 1
print("Length using for loop:", length)

# Method 3: sum()
print("Length using sum():", sum(1 for _ in my_list))

#Code by Harshit