'''Write a Python program to remove a specified column from a given nested list.
Original Nested list:
[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
After removing 1st column:
[[2, 3], [4, 5], [1, 1]]
Original Nested list:
[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
After removing 3rd column:
[[1, 2], [-2, 4], [1, -1]]'''

def remove_column(nested_list, column_index):
    for sublist in nested_list:
        if len(sublist) > column_index:
            del sublist[column_index]
    return nested_list

original_nested_list1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
original_nested_list2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
removed_column_list1 = remove_column(original_nested_list1, 0)
print("Original Nested list:")
print(original_nested_list1)
print("After removing 1st column:")
print(removed_column_list1)
removed_column_list2 = remove_column(original_nested_list2, 2)
print("\nOriginal Nested list:")
print(original_nested_list2)
print("After removing 3rd column:")
print(removed_column_list2)
