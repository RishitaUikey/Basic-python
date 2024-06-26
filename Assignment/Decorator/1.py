# Write a  Python program to create a decorator that logs the arguments and return value of a function.

def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments:")
        print("Arguments:", args)
        print("Keyword arguments:", kwargs)
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned:", result)
        return result
    return wrapper


@log_function
def add(a, b):
    return a + b

result = add(3, 5)
