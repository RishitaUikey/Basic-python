# Write a Python program to count the number of items in a dictionary value that is a list.

my_dict = {'a': [1, 2, 3], 'b': 'hello', 'c': [4, 5], 'd': {'x': 1, 'y': 2}, 'e': [6, 7, 8]}
list_count = sum(isinstance(value, list) for value in my_dict.values())
print("Number of items in dictionary values that are lists:", list_count)

