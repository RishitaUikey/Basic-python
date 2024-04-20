'''Write a  Python program to get the most frequent element in a given list of numbers.
Sample Output:
2
Original list:
[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
Item with maximum frequency of the said list:
2
Original list:
[1, 2, 3, 1, 2, 3, 2, 1, 4, 3, 3]
Item with maximum frequency of the said list:
3
'''

from collections import Counter

def most_frequent_element(lst):
    count = Counter(lst)
    most_common = count.most_common(1)
    return most_common[0][0]

sample_lists = [
    [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2],
    [1, 2, 3, 1, 2, 3, 2, 1, 4, 3, 3]
]
for lst in sample_lists:
    print("Original list:")
    print(lst)
    print("Item with maximum frequency of the said list:")
    print(most_frequent_element(lst))
