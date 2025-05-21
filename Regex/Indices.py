# Find Indices of Overlapping Substrings
def find_overlapping_indices(s, sub):
    indices = []
    start = 0
    while True:
        idx = s.find(sub, start)
        if idx == -1:
            break
        indices.append(idx)
        start = idx + 1  
        # Move only one character forward for overlapping
    return indices

if __name__ == "__main__":
    s = "ABABA"
    sub = "ABA"
    print(find_overlapping_indices(s, sub))
    
# Code by Harshit