'''Write a Python program to generate two strings from a given string. For the first string, 
use the characters that occur only once, and for the second, 
use the characters that occur multiple times in the said string.'''

def generate_strings(input_string):
    once_chars = ""
    multiple_chars = ""
    char_count = {char: input_string.count(char) for char in input_string}
    for char in input_string:
        if char_count[char] == 1:
            once_chars += char
        elif char_count[char] > 1 and char not in multiple_chars:
            multiple_chars += char
    return once_chars, multiple_chars
input_string = "hellopythonprogramming"
once_chars, multiple_chars = generate_strings(input_string)
print("Characters occurring only once:", once_chars)
print("Characters occurring multiple times:", multiple_chars)
