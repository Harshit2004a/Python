# Find files having a particular extension using RegEx

import os

def find_files_with_extension(directory, extension):
    ext = f".{extension.lower()}"
    matched_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(ext):
                matched_files.append(os.path.join(root, file))
    return matched_files

if __name__ == "__main__":
    directory = "."
    extension = "py"
    files = find_files_with_extension(directory, extension)
    for f in files:
        print(f)
        
# Code by Harshit