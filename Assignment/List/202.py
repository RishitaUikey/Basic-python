'''Write a  Python program to find the indexes of all None items in a given list.
Original list:
[1, None, 5, 4, None, 0, None, None]
Indexes of all None items of the list:
[1, 4, 6, 7]'''

def find_none_indexes(lst):
    none_indexes = []
    for i in range(len(lst)):
        if lst[i] is None:
            none_indexes.append(i)
    return none_indexes

original_list = [1, None, 5, 4, None, 0, None, None]
print("Original list:")
print(original_list)
print("Indexes of all None items of the list:")
print(find_none_indexes(original_list))
