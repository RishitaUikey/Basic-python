'''Write a Python program to print the following numbers up to 2 decimal places with a sign.'''

def print_signed_numbers(numbers):
    for number in numbers:
        sign = '+' if number >= 0 else '-'
        print(f"{sign}{abs(number):.2f}")

numbers = [3.14159, -2.71828, 1.41421, -0.57721]
print_signed_numbers(numbers)
