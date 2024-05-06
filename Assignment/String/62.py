'''Write a Python program to compute the sum of the digits in a given string.'''

def sum_of_digits(string):
    total_sum = 0
    for char in string:
        if char.isdigit():
            total_sum += int(char)
    
    return total_sum
input_string = "well come to the world1234567890"
result = sum_of_digits(input_string)
print("Sum of digits in the string:", result)
