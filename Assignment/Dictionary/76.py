'''Write a  Python program to combine two lists into a dictionary. The elements of the first one serve as keys and the elements of the second one serve as values. Each item in the first list must be unique and hashable.
Sample Output:
Original lists:
['a', 'b', 'c', 'd', 'e', 'f']
[1, 2, 3, 4, 5]
Combine the values of the said two lists into a dictionary:
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}'''

def combine_lists_to_dict(keys, values):
    return dict(zip(keys, values))

keys_list = ['a', 'b', 'c', 'd', 'e', 'f']
values_list = [1, 2, 3, 4, 5]
result_dict = combine_lists_to_dict(keys_list, values_list)

print("Original lists:")
print(keys_list)
print(values_list)
print("Combine the values of the said two lists into a dictionary:")
print(result_dict)
