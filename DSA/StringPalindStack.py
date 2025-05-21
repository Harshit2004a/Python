# Check whether the given string is Palindrome using Stack

def is_palindrome(s):
    stack = list(s)
    for char in s:
        if char != stack.pop():
            return False
    return True

if __name__ == "__main__":
    s = input("Enter a string: ")
    print("Palindrome" if is_palindrome(s) else "Not a palindrome")
    
# Code by Harshit