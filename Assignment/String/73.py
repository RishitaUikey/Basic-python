'''Write a  Python program to count Uppercase, Lowercase, special characters and numeric values in a given string.'''

def count_characters(input_string):
    uppercase_count = 0
    lowercase_count = 0
    special_count = 0
    numeric_count = 0

    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            numeric_count += 1
        else:
            special_count += 1
    return uppercase_count, lowercase_count, special_count, numeric_count
input_string = "Hello World! 123"
uppercase, lowercase, special, numeric = count_characters(input_string)
print("Uppercase characters:", uppercase)
print("Lowercase characters:", lowercase)
print("Special characters:", special)
print("Numeric values:", numeric)
