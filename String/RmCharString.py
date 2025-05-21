def remove_ith_char(s, i):
    if i < 0 or i >= len(s):
        raise ValueError("Index out of range")
    return s[:i] + s[i+1:]

# Take input from user
string = input("Enter the string: ")
index = int(input("Enter the index of the character to remove: "))

try:
    print("Result:", string[:index] + string[index+1:])
except Exception:
    print("Error: Invalid index")

# Code by Harshit