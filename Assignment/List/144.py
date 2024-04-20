''' Write a  Python program to extract every first or specified element from a given two-dimensional list.
Original list of lists:
[[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
Extract every first element from the said given two dimensional list:
[1, 4, 7]
Extract every third element from the said given two dimensional list:
[3, 6, 9]'''

def extract_elements(list_of_lists, index):
    extracted_elements = [sublist[index] for sublist in list_of_lists]
    return extracted_elements

list_of_lists = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
first_elements = extract_elements(list_of_lists, 0)
print("Extract every first element from the said given two-dimensional list:")
print(first_elements)
third_elements = extract_elements(list_of_lists, 2)
print("Extract every third element from the said given two-dimensional list:")
print(third_elements)
