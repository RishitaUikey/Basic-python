'''Write a  Python program to count the most common words in a dictionary.
Sample Output:
[('pink', 6), ('black', 5), ('white', 5), ('red', 4)]'''

from collections import Counter

def count_most_common_words(dictionary):
    words = [word for sublist in dictionary.values() for word in sublist]
    word_counts = Counter(words)
    most_common_words = word_counts.most_common()

    return most_common_words

dictionary = {
    'colors': ['red', 'blue', 'green'],
    'animals': ['black', 'white', 'pink', 'black', 'white', 'pink', 'black', 'white', 'pink']
}

most_common_words = count_most_common_words(dictionary)
print("Most common words in the dictionary:")
print(most_common_words)
