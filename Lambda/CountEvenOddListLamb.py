# Count Even and Odd numbers in a List using lambda

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count_even = len(list(filter(lambda x: x % 2 == 0, numbers)))
count_odd = len(list(filter(lambda x: x % 2 != 0, numbers)))

print("Even numbers count:", count_even)
print("Odd numbers count:", count_odd)

# Code by Harshit