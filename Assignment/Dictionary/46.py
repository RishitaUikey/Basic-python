'''Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
Original list:
[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
Grouping a sequence of key-value pairs into a dictionary of lists:
{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}'''

key_value_pairs = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
grouped_dict = {}
for key, value in key_value_pairs:
    grouped_dict.setdefault(key, []).append(value)
print("Grouping a sequence of key-value pairs into a dictionary of lists:")
print(grouped_dict)
