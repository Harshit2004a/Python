# Find fibonacci series upto n using lambda

n = int(input("Enter the value of n: "))

fib = lambda a, b: a + b

a, b = 0, 1
result = []

while a <= n:
    result.append(a)
    a, b = b, fib(a, b)

print("Fibonacci series up to", n, ":", result)

# Code by Harshit