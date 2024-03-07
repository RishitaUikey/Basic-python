# Write a Python program to create a chain of function decorators (bold, italic, underline etc.).

def bold_decorator(func):
    def wrapper(*args, **kwargs):
        print("<b>", end="")
        func(*args, **kwargs)
        print("</b>", end="")
    return wrapper

def italic_decorator(func):
    def wrapper(*args, **kwargs):
        print("<i>", end="")
        func(*args, **kwargs)
        print("</i>", end="")
    return wrapper

def underline_decorator(func):
    def wrapper(*args, **kwargs):
        print("<u>", end="")
        func(*args, **kwargs)
        print("</u>", end="")
    return wrapper

@bold_decorator
@italic_decorator
@underline_decorator
def greet(name):
    print("Hello, " + name + "!")

greet("John")
