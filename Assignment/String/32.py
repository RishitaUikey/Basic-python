'''Write a Python program to print the following positive and negative numbers with no decimal places.'''

def print_integer_numbers(numbers):
    for number in numbers:
        print(f"{int(number):.0f}")
numbers = [3.14159, -2.71828, 1.41421, -0.57721]
print_integer_numbers(numbers)
