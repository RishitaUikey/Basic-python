'''Write a  Python program to find the item with the highest frequency in a given list.
Sample Output:
Original list:
[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
Item with maximum frequency of the said list:
(2, 5)'''

from collections import Counter

original_list = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
counts = Counter(original_list)
max_item = max(counts, key=counts.get)
max_freq = counts[max_item]

print("Item with maximum frequency of the said list:")
print((max_item, max_freq))
