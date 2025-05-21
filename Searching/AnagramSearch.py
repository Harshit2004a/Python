# Program for Anagram Substring Search (Or Search for all permutations)
from collections import Counter

def anagram_search(txt, pat):
    M, N = len(pat), len(txt)
    pat_count = Counter(pat)
    result = []

    for i in range(N - M + 1):
        if Counter(txt[i:i+M]) == pat_count:
            result.append(i)
    return result

if __name__ == "__main__":
    txt = "BACDGABCDA"
    pat = "ABCD"
    indices = anagram_search(txt, pat)
    print(f"Anagram indices: {indices}")
    
# Code by Harshit