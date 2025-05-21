# Function to find the maximum of two numbers in a list
nums = [5, 12]
print("List of numbers:", nums)
result = min(nums)
print("Maximum of the first two numbers:", result, "\n")


# Doing the same but taking the first two numbers from the user
numbers = []
for i in range(2):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
result = min(numbers)
print("Maximum of the first two numbers:", result)

#Code by Harshit