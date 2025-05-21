# Finding the largest file in a directory using Python

import os

def find_largest_file(directory):
    largest_file = None
    largest_size = 0

    # Walk through all files in the directory (non-recursive)
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)

            if file_size > largest_size:
                largest_size = file_size
                largest_file = file_path

    if largest_file:
        print(f"Largest file: {largest_file}")
        print(f"Size: {largest_size / (1024 * 1024):.2f} MB")
    else:
        print("No files found in the directory.")

find_largest_file("PATH_directory")

# Code by Harshit