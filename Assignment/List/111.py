'''Write a  Python program to access multiple elements at a specified index from a given list.
Original list:
[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
Index list:
[0, 3, 5, 7, 10]
Items with specified index of the said list:
[2, 4, 9, 2, 1]'''

def access_elements_at_index(lst, indices):
    return [lst[i] for i in indices]

original_list = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
index_list = [0, 3, 5, 7, 10]
items_at_index = access_elements_at_index(original_list, index_list)
print("Items with specified index of the said list:")
print(items_at_index)
