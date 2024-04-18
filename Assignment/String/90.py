'''Write a Python program to remove duplicate words from a given string.
Sample Output:
Original String:
 Python Exercises Practice Solution Exercises
After removing duplicate words from the said string:
Python Exercises Practice Solution'''

def remove_duplicate_words(input_str):
    words = input_str.split()
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    result = ' '.join(unique_words)
    return result
input_str = "Python Exercises Practice Solution Exercises"
print("Original String:")
print(input_str)
print("After removing duplicate words from the said string:")
print(remove_duplicate_words(input_str))
