# Find the most repeated word in a text file
from collections import Counter
import re

def most_repeated_word(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        words = re.findall(r'\w+', f.read().lower())
    if not words:
        return None, 0
    word, count = Counter(words).most_common(1)[0]
    return word, count

if __name__ == "__main__":
    fname = input("Enter the filename: ")
    word, count = most_repeated_word(fname)
    if word:
        print(f"Most repeated word: '{word}' ({count} times)")
    else:
        print("No words found.")

# Code by Harshit