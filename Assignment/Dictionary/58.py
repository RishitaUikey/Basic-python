'''Write a  Python program to get all combinations of key-value pairs in a given dictionary.
Original Dictionary:
{'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
Combinations of key-value pairs of the said dictionary:
[{'V': [1, 4, 6, 10], 'VI': [1, 4, 12]}, {'V': [1, 4, 6, 10], 'VII': [1, 3, 8]}, {'VI': [1, 4, 12], 'VII': [1, 3, 8]}]
Original Dictionary:
{'V': [1, 3, 5], 'VI': [1, 5]}
Combinations of key-value pairs of the said dictionary:
[{'V': [1, 3, 5], 'VI': [1, 5]}]'''

from itertools import combinations

def get_combinations(dictionary):
    keys = list(dictionary.keys())
    result = []
    for r in range(1, len(keys) + 1):
        key_combinations = combinations(keys, r)
        for combo in key_combinations:
            new_dict = {key: dictionary[key] for key in combo}
            result.append(new_dict)
    return result

original_dict1 = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
original_dict2 = {'V': [1, 3, 5], 'VI': [1, 5]}

combinations1 = get_combinations(original_dict1)
combinations2 = get_combinations(original_dict2)

print("Original Dictionary:")
print(original_dict1)
print("Combinations of key-value pairs of the said dictionary:")
print(combinations1)

print("\nOriginal Dictionary:")
print(original_dict2)
print("Combinations of key-value pairs of the said dictionary:")
print(combinations2)
