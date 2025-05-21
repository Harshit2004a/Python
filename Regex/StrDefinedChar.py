# Check if String Contain Only Defined Characters using Regex

import re

def contains_only_defined_chars(s, allowed_chars):
    pattern = f'^[{re.escape(allowed_chars)}]+$'
    return bool(re.match(pattern, s))

string = "abcabc"
allowed = "abc"
if contains_only_defined_chars(string, allowed):
    print("String contains only defined characters.")
else:
    print("String contains other characters.")
    
# Code by Harshit