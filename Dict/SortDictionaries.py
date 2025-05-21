def sort_dict_by_key(d, reverse=False):
    return dict(sorted(d.items(), key=lambda item: item[0], reverse=reverse))

def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))

if __name__ == "__main__":
    sample_dict = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

    print("Original dictionary:")
    print(sample_dict)

    print("\nSorted by key:")
    print(sort_dict_by_key(sample_dict))

    print("\nSorted by value:")
    print(sort_dict_by_value(sample_dict))
    
# Code by Harshit