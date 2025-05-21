# Flattening JSON objects in Python
import json

def flatten_json(d, parent_key='', sep='.'):
    flat = {}
    for k, v in d.items():
        key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            flat.update(flatten_json(v, key, sep))
        elif isinstance(v, list):
            for i, item in enumerate(v):
                flat.update(flatten_json({str(i): item}, key, sep))
        else:
            flat[key] = v
    return flat

if __name__ == "__main__":
    data = {
        "a": 1,
        "b": {
            "c": 2,
            "d": {
                "e": 3
            }
        },
        "f": [4, 5, {"g": 6}]
    }
    print(json.dumps(flatten_json(data), indent=2))

# Code by Harshit