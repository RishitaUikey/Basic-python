'''Write a  Python program to find the first non-repeating character in a given string'''

def first_non_repeating_char(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None
input_string = input("Enter a string: ")
result = first_non_repeating_char(input_string)

if result:
    print("The first non-repeating character is:", result)
else:
    print("No non-repeating character found in the string.")
