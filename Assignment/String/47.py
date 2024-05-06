'''Write a  Python program to lowercase the first n characters in a string'''

def lowercase_first_n(string, n):
    lowercased_part = string[:n].lower()
    rest_of_string = string[n:]
    result = lowercased_part + rest_of_string
    return result
string = 'Sakshi'
n = 5
result = lowercase_first_n(string, n)
print("Original string:", string)
print("String with first", n, "characters lowercased:", result)
