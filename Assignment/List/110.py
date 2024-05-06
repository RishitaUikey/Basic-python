'''Write a  Python program to find the item with the most occurrences in a given list.
Original list:
[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
Item with maximum occurrences of the said list:
2'''

from collections import Counter

def most_common_item(lst):
    counts = Counter(lst)
    most_common = counts.most_common(1)
    return most_common[0][0] if most_common else None

original_list = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
most_common = most_common_item(original_list)
print("Item with maximum occurrences of the said list:")
print(most_common)
