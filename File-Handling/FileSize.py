# How to check file size in Python?
import os

file_path = '/path/to/your/file.txt'
file_size = os.path.getsize(file_path)
print(f"File size: {file_size} bytes")

# Code by Harshit