if __name__ == "__main__":
    s = input("Enter a string: ")
    n = len(s)
    mid = n // 2

    # Check for Symmetrical
    if (n % 2 == 0 and s[:mid] == s[mid:]) or (n % 2 != 0 and s[:mid] == s[mid+1:]):
        print("The string is Symmetrical")
    else:
        print("The string is not Symmetrical")

    # Check for Palindrome
    if s == s[::-1]:
        print("The string is Palindrome")
    else:
        print("The string is not Palindrome")

# Code by Harshit