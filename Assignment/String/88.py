
'''Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length.
Sample Output:
Input the string: W3resource
['Valid string.']'''

def check_string(input_str):
    has_upper = any(char.isupper() for char in input_str)
    has_lower = any(char.islower() for char in input_str)
    has_digit = any(char.isdigit() for char in input_str)
    has_min_length = len(input_str) >= 6 

    if has_upper and has_lower and has_digit and has_min_length:
        return ['Valid string.']
    else:
        return ['Invalid string.']

input_str = input("Input the string: ")
print(check_string(input_str))
