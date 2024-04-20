'''Write a  Python program to sum two or more lists. The lengths of the lists may be different.
Original list:
[[1, 2, 4], [2, 4, 4], [1, 2]]
Sum said lists with different lengths:
[4, 8, 8]
Original list:
[[1], [2, 4, 4], [1, 2], [4]]
Sum said lists with different lengths:
[8, 6, 4]'''

from itertools import zip_longest

def sum_lists(*lists):
    summed_list = []
    for items in zip_longest(*lists, fillvalue=0):
        summed_list.append(sum(items))
    
    return summed_list
original_lists = [
    [[1, 2, 4], [2, 4, 4], [1, 2]],
    [[1], [2, 4, 4], [1, 2], [4]]
]
for lists in original_lists:
    print("Original list:")
    print(lists)
    print("Sum said lists with different lengths:")
    print(sum_lists(*lists))
    print()
