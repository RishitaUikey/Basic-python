'''Write a  Python program to find common elements in a nested list.
Original lists:
[[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
Common element(s) in nested lists:
[18, 12]'''

def find_common_elements(nested_list):
    if not nested_list:
        return []

    common_elements = set(nested_list[0])
    for sublist in nested_list[1:]:
        common_elements.intersection_update(sublist)
    return list(common_elements)

nested_list = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]

common_elements = find_common_elements(nested_list)

print("Original lists:")
print(nested_list)
print("Common element(s) in nested lists:")
print(common_elements)
