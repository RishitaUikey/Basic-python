'''Write a  Python program to add two given lists of different lengths, starting on the right.
Original lists:
[2, 4, 7, 0, 5, 8]
[3, 3, -1, 7]
Add said two lists from left:
[2, 4, 10, 3, 4, 15]
Original lists:
[1, 2, 3, 4, 5, 6]
[2, 4, -3]
Add said two lists from left:
[1, 2, 3, 6, 9, 3]'''

def add_lists_right(list1, list2):
    len_diff = len(list1) - len(list2)
    if len_diff > 0:
        list2 = list2 + [0] * len_diff
    elif len_diff < 0:
        list1 = list1 + [0] * abs(len_diff)
    
    return [x + y for x, y in zip(list1, list2)]

original_list1 = [2, 4, 7, 0, 5, 8]
original_list2 = [3, 3, -1, 7]
print("Add said two lists from right:")
print(add_lists_right(original_list1, original_list2))
original_list3 = [1, 2, 3, 4, 5, 6]
original_list4 = [2, 4, -3]
print("Add said two lists from right:")
print(add_lists_right(original_list3, original_list4))
