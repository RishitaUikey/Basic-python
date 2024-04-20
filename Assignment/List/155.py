'''Write a  Python program to add two given lists of different lengths, starting on the left.
Original lists:
[2, 4, 7, 0, 5, 8]
[3, 3, -1, 7]
Add said two lists from left:
[5, 7, 6, 7, 5, 8]
Original lists:
[1, 2, 3, 4, 5, 6]
[2, 4, -3]
Add said two lists from left:
[3, 6, 0, 4, 5, 6]'''

def add_lists_left(list1, list2):
    len_diff = len(list1) - len(list2)
    if len_diff > 0:
        list2 = [0] * len_diff + list2
    elif len_diff < 0:
        list1 = [0] * abs(len_diff) + list1
    return [x + y for x, y in zip(list1, list2)]

original_list1 = [2, 4, 7, 0, 5, 8]
original_list2 = [3, 3, -1, 7]
print("Add said two lists from left:")
print(add_lists_left(original_list1, original_list2))
original_list3 = [1, 2, 3, 4, 5, 6]
original_list4 = [2, 4, -3]
print("Add said two lists from left:")
print(add_lists_left(original_list3, original_list4))
