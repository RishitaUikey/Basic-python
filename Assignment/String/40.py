'''Write a Python program to reverse words in a string
'''

def reverse_words(string):
    words = string.split()
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words)

    return reversed_string
string = "hello world"
reversed_string = reverse_words(string)
print("Original string:", string)
print("String with reversed words:", reversed_string)
