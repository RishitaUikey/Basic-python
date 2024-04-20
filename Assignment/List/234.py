'''Write a Python program to convert a given number (integer) to a list of digits.
Sample Output:
[1, 2, 3]
[1, 3, 4, 7, 8, 2, 3]'''

def number_to_digits(number):
    return [int(digit) for digit in str(number)]
number1 = 123
number2 = 1347823
digits1 = number_to_digits(number1)
digits2 = number_to_digits(number2)
print(digits1)
print(digits2)
