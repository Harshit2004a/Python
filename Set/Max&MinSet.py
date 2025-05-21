# Maximum and Minimum in a Set

def max_min_in_set(s):
    if not s:
        raise ValueError("Set is empty")
    return max(s), min(s)

if __name__ == "__main__":
    s = {5, 2, 9, 1, 7}
    maximum, minimum = max_min_in_set(s)
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
    
# Code by Harshit