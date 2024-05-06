'''Write a Python program to convert a given string into a list of words.
Sample Output:
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']'''

def string_to_word_list(string):
    word_list = string.split()
    return word_list

string = 'The quick brown fox jumps over the lazy dog.'
word_list = string_to_word_list(string)
print(word_list)
