'''Write a  Python program to combine two lists into another list randomly.
Original lists:
[1, 2, 7, 8, 3, 7]
[4, 3, 8, 9, 4, 3, 8, 9]
Interleave two given list into another list randomly:
[4, 1, 2, 3, 8, 9, 4, 3, 7, 8, 9, 8, 3, 7]'''

import random

def combine_lists_randomly(list1, list2):
    combined_list = list1 + list2
    random.shuffle(combined_list)
    return combined_list

list1 = [1, 2, 7, 8, 3, 7]
list2 = [4, 3, 8, 9, 4, 3, 8, 9]
print("Original lists:")
print(list1)
print(list2)
print("Interleave two given lists into another list randomly:")
print(combine_lists_randomly(list1, list2))
