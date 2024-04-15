# Write a  Python program to remove all duplicates from a given list of strings and return a list of unique strings. Use the Python set data type.

def remove_duplicates(strings):
    unique_strings = list(set(strings))
    return unique_strings

strings = ["apple", "banana", "apple", "orange", "banana", "grape", "orange"]
unique_strings = remove_duplicates(strings)
print("Unique strings after removing duplicates:")
print(unique_strings)
