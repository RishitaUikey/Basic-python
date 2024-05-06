'''Write a Python program to find the occurrences of the 10 most common words in a given text.
Sample Output:
[(' Python', 6), ('the', 6), ('and', 5), ('We', 2), ('with', 2), ('The', 1), ('Software', 1), ('Foundation', 1), ('PSF', 1), ('is', 1)]'''

def most_common_words(text, n=10):
    words = text.lower().split()
    word_counts = {}
    for word in words:
        word = word.strip('.,!?;:')
        word_counts[word] = word_counts.get(word, 0) + 1
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    most_common_words = sorted_word_counts[:n]
    return most_common_words

text = "We love Python and Python is awesome. Python programming with Python is fun. The Python Software Foundation (PSF) is a non-profit organization devoted to the Python programming language."
most_common_words_result = most_common_words(text)
print(most_common_words_result)
