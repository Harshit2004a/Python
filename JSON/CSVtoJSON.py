# Convert CSV to JSON using Python
import csv
import json

with open('input.csv', encoding='utf-8') as csvfile:
    data = list(csv.DictReader(csvfile))

with open('output.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=4)
    
# Code by Harshit