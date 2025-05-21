# Python Script to change name of a file to its timestamp

import os
import datetime

def rename_to_timestamp(file_path):
    if not os.path.isfile(file_path):
        print("File does not exist.")
        return

    mod_time = os.path.getmtime(file_path)
    timestamp = datetime.datetime.fromtimestamp(mod_time).strftime('%Y%m%d_%H%M%S')

    dir_name = os.path.dirname(file_path)
    file_ext = os.path.splitext(file_path)[1]

    # New file name
    new_name = os.path.join(dir_name, f"{timestamp}{file_ext}")

    # Rename the file
    os.rename(file_path, new_name)
    print(f"Renamed to: {new_name}")


file_path = "example.txt" 
rename_to_timestamp(file_path)

# Code by Harshit