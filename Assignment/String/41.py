'''Write a  Python program to strip a set of characters from a string.'''

def strip_characters(string, characters):
    stripped_string = string
    for char in characters:
        stripped_string = stripped_string.replace(char, '')
    return stripped_string
string = "hello world"
characters_to_strip = "aeiou"
stripped_string = strip_characters(string, characters_to_strip)
print("Original string:", string)
print("String with specified characters stripped:", stripped_string)
