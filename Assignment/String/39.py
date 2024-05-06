'''Write a  Python program to reverse a string.'''

def reverse_string(string):
    reversed_string = string[::-1]
    return reversed_string

string = "hello world"
reversed_string = reverse_string(string)
print("Original string:", string)
print("Reversed string:", reversed_string)
