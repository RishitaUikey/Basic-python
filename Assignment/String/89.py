'''Write a  Python program to remove unwanted characters from a given string.
Sample Output:
Original String : Pyth*^on Exercis^es
After removing unwanted characters:
Python Exercises
Original String : A%^!B#*CD
After removing unwanted characters:
ABCD'''


import re

def remove_unwanted_characters(input_string):

    pattern = r'[^a-zA-Z0-9\s]' 
    cleaned_string = re.sub(pattern, '', input_string)

    return cleaned_string

original_string1 = "Pyth*^on Exercis^es"
original_string2 = "A%^!B#*CD"

print("Original String 1:", original_string1)
print("After removing unwanted characters:")
print(remove_unwanted_characters(original_string1))

print("\nOriginal String 2:", original_string2)
print("After removing unwanted characters:")
print(remove_unwanted_characters(original_string2))


