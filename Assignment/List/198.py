'''Write a  Python program to compare two given lists and find the indices of the values present in both lists.
Original lists:
[1, 2, 3, 4, 5, 6]
[7, 8, 5, 2, 10, 12]
Compare said two lists and get the indices of the values present in both lists:
[1, 4]
Original lists:
[1, 2, 3, 4, 5, 6]
[7, 8, 5, 7, 10, 12]
Compare said two lists and get the indices of the values present in both lists:
[4]
Original lists:
[1, 2, 3, 4, 15, 6]
[7, 8, 5, 7, 10, 12]
Compare said two lists and get the indices of the values present in both lists:
[]
'''

def find_matching_indices(list1, list2):
    matching_indices = []
    for i, num1 in enumerate(list1):
        if num1 in list2:
            matching_indices.append(i)
    return matching_indices

lists = [
    ([1, 2, 3, 4, 5, 6], [7, 8, 5, 2, 10, 12]),
    ([1, 2, 3, 4, 5, 6], [7, 8, 5, 7, 10, 12]),
    ([1, 2, 3, 4, 15, 6], [7, 8, 5, 7, 10, 12])
]

for list1, list2 in lists:
    matching_indices = find_matching_indices(list1, list2)
    print("Original lists:")
    print(list1)
    print(list2)
    print("Compare said two lists and get the indices of the values present in both lists:")
    print(matching_indices)
