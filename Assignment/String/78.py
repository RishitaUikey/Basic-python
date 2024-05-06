'''Write a  Python program to count characters at the same position in a 
given string (lower and uppercase characters) as in the English alphabet.'''

def count_same_position_characters(input_string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for i, char in enumerate(input_string):
        if char.lower() in alphabet and char.lower() == alphabet[i % 26]:
            count += 1
    return count
input_string = "AbCdeFghiJklmNopqrStUvwXYZ"
result = count_same_position_characters(input_string)
print("Number of characters at the same position in the English alphabet:", result)
