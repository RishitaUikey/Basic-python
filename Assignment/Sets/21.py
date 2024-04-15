# Write a  Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use  Python set data type.

def count_word_frequency(strings):
    word_frequency = {}
    
    for string in strings:
        words = string.split()
        for word in words:
            word_frequency[word] = word_frequency.get(word, 0) + 1
    
    return word_frequency

list_of_strings = [
    "Hello Everyone",
    "Welcome to the world of programming",
    "programming is fun",
    "hello python"
]

word_frequency = count_word_frequency(list_of_strings)

print("Unique words and their frequencies:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")
