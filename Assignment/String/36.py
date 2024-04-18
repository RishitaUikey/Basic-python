'''Write a Python program to format a number with a percentage'''

def format_as_percentage(number):
    formatted_percentage = "{:.2%}".format(number)
    print(formatted_percentage)
number = 0.75
format_as_percentage(number)
