'''Write a Python program to find the first repeated character in a given string'''

def first_repeated_char(string):
    char_set = set()
    
    for char in string:
        if char in char_set:
            return char
        else:
            char_set.add(char)
    
    return None
input_string = input("Enter a string: ")
result = first_repeated_char(input_string)

if result:
    print("The first repeated character is:", result)
else:
    print("No repeated character found in the string.")
