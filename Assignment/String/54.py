'''Write a  Python program to find the first repeated 
character in a given string where the index of the first occurrence is smallest.'''

def first_repeated_char(string):
    seen_chars = set()
    for char in string:
        if char in seen_chars:
            return char
        seen_chars.add(char)
    return None
input_string = input("Enter a string: ")
result = first_repeated_char(input_string)

if result:
    print("The first repeated character with the smallest index of the first occurrence is:", result)
else:
    print("No repeated character found in the string.")
