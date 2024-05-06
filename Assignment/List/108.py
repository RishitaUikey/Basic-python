'''Write a  Python program to extract a specified column from a given nested list.
Original Nested list:
[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
Extract 1st column:
[1, 2, 1]
Original Nested list:
[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
Extract 3rd column:
[3, -5, 1]'''

def extract_column(nested_list, column_index):
    column = []
    for sublist in nested_list:
        if len(sublist) > column_index:
            column.append(sublist[column_index])
    return column

original_nested_list1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
original_nested_list2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
extracted_column_list1 = extract_column(original_nested_list1, 0)
print("Original Nested list:")
print(original_nested_list1)
print("Extract 1st column:")
print(extracted_column_list1)
extracted_column_list2 = extract_column(original_nested_list2, 2)
print("\nOriginal Nested list:")
print(original_nested_list2)
print("Extract 3rd column:")
print(extracted_column_list2)
