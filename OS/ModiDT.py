# File creation and modification date or time in Python
from pathlib import Path
import datetime

file = Path("your_file.txt")

creation_time = file.stat().st_ctime  # Same platform behavior as getctime()
modification_time = file.stat().st_mtime

print("Created:", datetime.datetime.fromtimestamp(creation_time))
print("Modified:", datetime.datetime.fromtimestamp(modification_time))

# Code by Harshit