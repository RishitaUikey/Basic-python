'''Write a Python program to remove duplicate words from a given string. Use the collections module.
Sample Output:
Original String:
 Python Exercises Practice Solution Exercises
After removing duplicate words from the said string:
Python Exercises Practice Solution'''

def remove_duplicates(string):
    words = string.split()
    unique_words = set(words)
    unique_string = ' '.join(unique_words)

    return unique_string

x = "Python Exercises Practice Solution Exercises"

result_string = remove_duplicates(x)

print("After removing duplicate words from the said string:")
print(result_string)
