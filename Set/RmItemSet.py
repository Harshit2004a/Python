# Remove items from a set in Python
my_set = {1, 2, 3, 4, 5}

# using remove(), Error if item not found
my_set.remove(3)  # Removes 3

# using discard(), No error in this case
my_set.discard(10)  # No error, 10 not in set

# using pop()
removed_item = my_set.pop()

# Clear all items
my_set.clear()

print("Set after removals:", my_set)
print("Last popped item:", removed_item)

# Code by Harshit