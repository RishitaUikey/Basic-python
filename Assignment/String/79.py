'''Write a Python program to find the smallest and largest words in a given string.'''

def find_smallest_largest_words(input_string):
    words = input_string.split()
    smallest_word = None
    largest_word = None
    for word in words:
        if smallest_word is None or len(word) < len(smallest_word):
            smallest_word = word
        if largest_word is None or len(word) > len(largest_word):
            largest_word = word
    return smallest_word, largest_word
input_string = "Python is an amazing programming language"
smallest, largest = find_smallest_largest_words(input_string)
print("Smallest word:", smallest)
print("Largest word:", largest)
