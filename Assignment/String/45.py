'''Write a  Python program to check whether a string contains all letters of the alphabet.'''

def contains_all_letters(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = string.lower()
    for letter in alphabet:
        if letter not in string:
            return False
    return True
input_string = input("Enter a string: ")
if contains_all_letters(input_string):
    print("The string contains all letters of the alphabet.")
else:
    print("The string does not contain all letters of the alphabet.")
