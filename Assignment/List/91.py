'''Write a  Python program to find a list with maximum and minimum lengths.
Original list:
[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])
Original list:
[[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
List with maximum length of lists:
(3, [3, 5, 7])
List with minimum length of lists:
(1, [0])
Original list:
[[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
List with maximum length of lists:
(4, [1, 34, 5, 7])
List with minimum length of lists:
(1, [12])'''

def max_min_list_lengths(list_of_lists):
    max_len_list = max(list_of_lists, key=len)
    min_len_list = min(list_of_lists, key=len)
    return (len(max_len_list), max_len_list), (len(min_len_list), min_len_list)

lists1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
lists2 = [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
lists3 = [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]

max_min_lengths1 = max_min_list_lengths(lists1)
max_min_lengths2 = max_min_list_lengths(lists2)
max_min_lengths3 = max_min_list_lengths(lists3)

print("Original list:")
print(lists1)
print("List with maximum length of lists:")
print(max_min_lengths1[0])
print("List with minimum length of lists:")
print(max_min_lengths1[1])

print("\nOriginal list:")
print(lists2)
print("List with maximum length of lists:")
print(max_min_lengths2[0])
print("List with minimum length of lists:")
print(max_min_lengths2[1])

print("\nOriginal list:")
print(lists3)
print("List with maximum length of lists:")
print(max_min_lengths3[0])
print("List with minimum length of lists:")
print(max_min_lengths3[1])
