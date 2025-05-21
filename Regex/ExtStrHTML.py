# Extract Strings between HTML Tags

import re

def extract_strings_between_tags(html):
    return re.findall(r'>([^<]+)<', html)

# Example usage
html = "<div>Hello <b>World</b>!</div>"
strings = extract_strings_between_tags(html)
print(strings)

# Code by Harshit