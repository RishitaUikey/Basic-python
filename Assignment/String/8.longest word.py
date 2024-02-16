'''Write a Python function that takes a list of words and return the longest word and the length of the longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9 '''

def list_of_words(words):
    longest_word = ''
    length_of_word = 0

    for i in words:
        if len(i) > length_of_word:
            longest_word = i
            length_of_word = len(i)
    return longest_word,length_of_word

sample_words = ['Python', 'program', 'is', 'fun', 'Exercises']
longest_word,length_of_word = list_of_words(sample_words)
print("Longest word: ",longest_word )
print("Length of the longest word: ",length_of_word )