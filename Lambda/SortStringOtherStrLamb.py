# Sorting string using order defined by another string using lambda
def custom_sort(s, order):
    return ''.join(sorted(s, key=lambda c: order.find(c) if c in order else len(order)))

s = "programming"
order = "gmproain"
print(custom_sort(s, order))  # Output: ggmproainmr

# Code by Harshit