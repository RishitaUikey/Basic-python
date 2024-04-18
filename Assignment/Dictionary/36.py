'''Write a Python program to create a dictionary from two lists without losing duplicate values.
Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
Expected Output: defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})'''

from collections import defaultdict

keys = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
values = [1, 2, 2, 3]
result_dict = defaultdict(set)
for key, value in zip(keys, values):
    result_dict[key].add(value)
print(result_dict)
