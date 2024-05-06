'''Write a Python class that has two methods: 
get_String and print_String , get_String accept 
a string from the user and print_String prints
the string in upper case.'''

class StringReverser:
    def __init__(self):
        pass

    def reverse_words(self, s):
        words = s.split()
        return ' '.join(reversed(words))

reverser = StringReverser()
input_string = 'hello . py'
print("Input string:", input_string)
print("Output:", reverser.reverse_words(input_string))
