'''Write a  Python program to group a sequence of key-value pairs into a dictionary of lists.
Sample Output:
[('v', [1, 3]), ('vi', [2, 4]), ('vii', [1])]'''

from collections import defaultdict

def group_to_dict(key_value_pairs):
    grouped_dict = defaultdict(list)

    for key, value in key_value_pairs:
        grouped_dict[key].append(value)

    return grouped_dict

sequence = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]
result = group_to_dict(sequence)
print(list(result.items()))
