# Find the power of a number using recursion

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
def power(base, exponent):
    return 1 if exponent == 0 else base * power(base, exponent - 1)

if __name__ == "__main__":
    print(power(base, exponent))

# Code by Harshit