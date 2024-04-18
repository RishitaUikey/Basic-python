'''Write a Python program to display a number with a comma separator.'''

def display_with_comma_separator(number):
    formatted_number = "{:,}".format(number)
    print(formatted_number)
number = 10000000000
display_with_comma_separator(number)
