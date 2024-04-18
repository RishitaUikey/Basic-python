'''Write a Python program to find the maximum number of characters in a given string.'''

def max_characters(string):
    max_count = 0
    for char in string:
        count = string.count(char)
        if count > max_count:
            max_count = count
    
    return max_count
input_string = input("Enter a string: ")
result = max_characters(input_string)
print("Maximum number of characters:", result)
