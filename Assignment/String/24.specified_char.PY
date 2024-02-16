# Write a Python program to check whether a string starts with specified characters.

special_char = input("Enter the special characters: ")
str1 = input("Enter the string: ")
if str1.startswith(special_char):
    print("We found it a string starts with specified characters")
else:
    print("No tring starts with specified characters")

