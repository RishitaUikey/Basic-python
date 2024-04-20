'''Write a  Python program to generate a number in a specified range except for some specific numbers.
Generate a number in a specified range (1, 10) except [2, 9, 10]
7
Generate a number in a specified range (-5, 5) except [-5,0,4,3,2]
-4'''

import random

def generate_number(start, end, exclude):
    numbers = [num for num in range(start, end + 1) if num not in exclude]
    return random.choice(numbers)
number1 = generate_number(1, 10, [2, 9, 10])
print("Generate a number in a specified range (1, 10) except [2, 9, 10]")
print(number1)
number2 = generate_number(-5, 5, [-5, 0, 4, 3, 2])
print("Generate a number in a specified range (-5, 5) except [-5, 0, 4, 3, 2]")
print(number2)
