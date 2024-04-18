'''Write a  Python program to remove spaces from a given string.
 '''
def remove_spaces(string):
    return string.replace(" ", "")

input_string = input("Enter a string: ")
result = remove_spaces(input_string)
print("String with spaces removed:", result)
