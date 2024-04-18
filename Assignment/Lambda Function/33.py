'''Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda.
Input the string: W3resource
['Valid string.']'''

input_string = "W3resource"

check_conditions = lambda s: any(char.isupper() for char in s) \
                            and any(char.islower() for char in s) \
                            and any(char.isdigit() for char in s) \
                            and len(s) >= 8

result = 'Valid string.' if check_conditions(input_string) else 'Invalid string.'

print(result)
