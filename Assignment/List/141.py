''' Write a  Python program to remove empty lists from a given list of lists.
Original list:
[[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
After deleting the empty lists from the said lists of lists
['Red', 'Green', [1, 2], 'Blue']'''

def remove_empty_lists(original_list):
    return [sublist for sublist in original_list if sublist]
original_list = [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
result_list = remove_empty_lists(original_list.copy())
print("After deleting the empty lists from the given list of lists:")
print(result_list)
