# Pyramid Patterns in Python

def pyramid(rows):
    for i in range(rows):
        print(' ' * (rows - i - 1) + '* ' * (i + 1))

def inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        print(' ' * (rows - i) + '* ' * i)

def number_pyramid(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + ' '.join(str(j) for j in range(1, i + 1)))

if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    print("\nStar Pyramid:")
    pyramid(n)
    print("\nInverted Star Pyramid:")
    inverted_pyramid(n)
    print("\nNumber Pyramid:")
    number_pyramid(n)
    
# Code by Harshit