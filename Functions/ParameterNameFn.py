# Get list of parameters name from a function in Python
def get_param_names(func):
    return func.__code__.co_varnames[:func.__code__.co_argcount]

def example_function(a, b, c=3, *args, **kwargs):
    pass

print(get_param_names(example_function))

# Code by Harshit