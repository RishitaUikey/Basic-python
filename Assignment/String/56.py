'''Write a Python program to find the second most repeated word in a given string.'''

def second_most_repeated_word(string):
    word_freq = {}
    words = string.split()
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    max_freq = max(word_freq.values())
    second_max_freq = 0
    second_most_repeated_word = None

    for word, freq in word_freq.items():
        if freq < max_freq and freq > second_max_freq:
            second_max_freq = freq
            second_most_repeated_word = word

    return second_most_repeated_word
input_string = input("Enter a string: ")
result = second_most_repeated_word(input_string)

if result:
    print("The second most repeated word is:", result)
else:
    print("No second most repeated word found in the string.")
