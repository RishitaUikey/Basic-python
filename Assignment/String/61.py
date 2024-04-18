'''Write a Python program to remove duplicate characters from a given string.'''

def remove_duplicates(string):
    seen = set()
    result = ""
    for char in string:
        if char not in seen:
            result += char
            seen.add(char)
    
    return result
input_string = "well come to the world"
result = remove_duplicates(input_string)
print(result)
