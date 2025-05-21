s = input("Enter a string: ")
# Method 1: Using len() function
print("Length using len():", len(s))

# Method 2: Using a for loop
length2 = 0
for char in s:
    length2 += 1
print("Length using for loop:", length2)

# Method 3: Using while loop and indexing
length3 = 0
while True:
    try:
        s[length3]
        length3 += 1
    except IndexError:
        break
print("Length using while loop:", length3)

# Method 4: Using sum and generator expression
length4 = sum(1 for _ in s)
print("Length using sum and generator:", length4)

# Code by Harshit