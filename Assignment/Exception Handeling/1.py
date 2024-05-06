# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

def divide_numbers(a, b):
    try:
        result = a / b
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Division by zero!")

try:
    divide_numbers(10, 0)
except ZeroDivisionError:
    print("Error occurred while dividing numbers.")
