# Diamond Pattern in python
def print_diamond(n):
    for i in range(2 * n - 1):
        stars = 2 * (n - abs(n - i - 1)) - 1
        spaces = abs(n - i - 1)
        print(' ' * spaces + '*' * stars)

if __name__ == "__main__":
    print_diamond(5)
    
# Code by Harshit