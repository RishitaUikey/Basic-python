'''Write a  Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75'''

def multiply_with_unknown(number):
    unknown_number = 5  
    return lambda x: x * unknown_number

double = multiply_with_unknown(2)
triple = multiply_with_unknown(3)
quadruple = multiply_with_unknown(4)
quintuple = multiply_with_unknown(5)

number = 15
print(f"Double the number of {number} = {double(number)}")
print(f"Triple the number of {number} = {triple(number)}")
print(f"Quadruple the number of {number} = {quadruple(number)}")
print(f"Quintuple the number {number} = {quintuple(number)}")
