'''Write a Python function to convert a given string to all uppercase if it 
contains at least 2 uppercase characters in the first 4 characters.'''


str1 = input("Enter the string: ")

if sum(1 for char in str1[:4] if char.isupper()) >= 2:
    result = str1.upper()
else:
    result = str1

print("Converted String:", result)

