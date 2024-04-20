''' Write a  Python program to get the unique values in a given list of lists.
Original list:
[[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
Unique values of the said list of lists:
[0, 1, 2, 3, 4, 5, 7]
Original list:
[['h', 'g', 'l', 'k'], ['a', 'b', 'd', 'e', 'c'], ['j', 'i', 'y'], ['n', 'b', 'v', 'c'], ['x', 'z']]
Unique values of the said list of lists:
['e', 'd', 'c', 'b', 'x', 'k', 'n', 'h', 'g', 'j', 'i', 'a', 'l', 'y', 'v', 'z']'''

def get_unique_values(list_of_lists):
    flattened_list = [item for sublist in list_of_lists for item in sublist]
    return list(set(flattened_list))

original_list1 = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
unique_values1 = get_unique_values(original_list1)

print("Original list:")
for sublist in original_list1:
    print(sublist)
print("Unique values of the said list of lists:")
print(unique_values1)

original_list2 = [['h', 'g', 'l', 'k'], ['a', 'b', 'd', 'e', 'c'], ['j', 'i', 'y'], ['n', 'b', 'v', 'c'], ['x', 'z']]
unique_values2 = get_unique_values(original_list2)

print("\nOriginal list:")
for sublist in original_list2:
    print(sublist)
print("Unique values of the said list of lists:")
print(unique_values2)
