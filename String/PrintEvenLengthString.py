# Python program to print even length words in a string

def print_even_length_words(input_string):
    words = input_string.split()
    for word in words:
        if len(word) % 2 == 0:
            print(word)

# Example usage
if __name__ == "__main__":
    input_str = "This is a sample string with even and odd words"
    print_even_length_words(input_str)
    
# Code by Harshit