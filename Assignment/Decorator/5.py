'''Write a Python program that implements a decorator to validate function arguments based on a given condition.'''

def validate_args(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                raise ValueError("Invalid arguments")
        return wrapper
    return decorator

@validate_args(lambda x, y: x > 0 and y > 0)
def divide(x, y):
    return x / y

try:
    result = divide(10, 0)
    print("Result:", result)
except ValueError as e:
    print("Error:", e)

try:
    result = divide(-10, 5)
    print("Result:", result)
except ValueError as e:
    print("Error:", e)

try:
    result = divide(10, 5)
    print("Result:", result)
except ValueError as e:
    print("Error:", e)
