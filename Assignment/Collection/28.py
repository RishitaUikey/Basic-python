'''Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists. Use the collections module.
Sample Output:
Original list:
[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
Grouping a sequence of key-value pairs into a dictionary of lists:
defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})'''

from collections import defaultdict

def group_to_dict(key_value_pairs):
    grouped_dict = defaultdict(list)

    for key, value in key_value_pairs:
        grouped_dict[key].append(value)

    return grouped_dict

x = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

grouped_dict = group_to_dict(x)
print("Grouping a sequence of key-value pairs into a dictionary of lists:",grouped_dict)

