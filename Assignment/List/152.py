'''Write a  Python program to combine two sorted lists using the heapq module.
Original sorted lists:
[1, 3, 5, 7, 9, 11]
[0, 2, 4, 6, 8, 10]
After merging the said two sorted lists:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]'''

import heapq

def merge_sorted_lists(list1, list2):
    return list(heapq.merge(list1, list2))

list1 = [1, 3, 5, 7, 9, 11]
list2 = [0, 2, 4, 6, 8, 10]

print("Original sorted lists:")
print(list1)
print(list2)
merged_list = merge_sorted_lists(list1, list2)
print("After merging the said two sorted lists:")
print(merged_list)
