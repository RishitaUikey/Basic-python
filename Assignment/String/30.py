'''Write a Python program to print the following numbers up to 2 decimal places.'''

def print_numbers(numbers):
    for number in numbers:
        print(round(number, 2))
numbers = [3.102453, 5.45797, 8.123456, 6.123456]
print_numbers(numbers)
