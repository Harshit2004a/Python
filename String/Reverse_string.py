if __name__ == "__main__":
    input_str = input("Enter a string: ")
    # Split the string into words, reverse the list, and join back to a string
    print("Reversed words:", ' '.join(input_str.split()[::-1]))

# Code by Harshit