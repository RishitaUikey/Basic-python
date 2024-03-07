'''Write a Python function to calculate the factorial of a number (a non-negative integer). 
The function accepts the number as an argument.'''

import math

def factorial_number(num):

    return math.factorial(num)
num = int(input("Enter the non negative integer: "))
output = factorial_number(num)
print("the factorial of a number (a non-negative integer) is ",output)
