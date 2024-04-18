'''Write a Python program to find the first repeated word in a given string'''

def first_repeated_word(string):
    word_set = set()
    words = string.split()
    for word in words:
        if word in word_set:
            return word
        word_set.add(word)
    return None
input_string = input("Enter a string: ")
result = first_repeated_word(input_string)

if result:
    print("The first repeated word is:", result)
else:
    print("No repeated word found in the string.")
