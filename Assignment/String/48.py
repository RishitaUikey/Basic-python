'''Write a Python program to swap commas and dots in a string.
Sample string: "32.054,23"
Expected Output: "32,054.23"'''

def swap_commas_and_dots(string):
    swapped_string = ""
    for char in string:
        if char == ',':
            swapped_string += '.'
        elif char == '.':
            swapped_string += ','
        else:
            swapped_string += char

    return swapped_string
string = "32.054,23"
result = swap_commas_and_dots(string)
print("Original string:", string)
print("Swapped string:", result)
