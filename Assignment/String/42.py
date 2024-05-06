'''Write a Python program to count repeated characters in a string.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2'''

def count_repeated_characters(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_characters = {char: count for char, count in char_count.items() if count > 1}

    return repeated_characters
string = 'thequickbrownfoxjumpsoverthelazydog'
repeated_characters = count_repeated_characters(string)
for char, count in repeated_characters.items():
    print(char, count)
