'''Write a Python program to move spaces to the front of a given string.'''

def move_spaces_to_front(string):
    spaces = ""
    non_spaces = ""
    for char in string:
        if char == " ":
            spaces += char
        else:
            non_spaces += char
    return spaces + non_spaces

input_string = input("Enter a string: ")
result = move_spaces_to_front(input_string)
print("String with spaces moved to the front:", result)
