'''Write a  Python program to count the occurrences of each element in a given list.
Sample Output:
Original List:
['Green', 'Red', 'Blue', 'Red', 'Orange', 'Black', 'Black', 'White', 'Orange']
Count the occurrence of each element of the said list:
Counter({'Red': 2, 'Orange': 2, 'Black': 2, 'Green': 1, 'Blue': 1, 'White': 1})
Original List:
[3, 5, 0, 3, 9, 5, 8, 0, 3, 8, 5, 8, 3, 5, 8, 1, 0, 2]
Count the occurrence of each element of the said list:
Counter({3: 4, 5: 4, 8: 4, 0: 3, 9: 1, 1: 1, 2: 1})'''

from collections import Counter

def count_occurrences(input_list):
    occurrences = Counter(input_list)

    return occurrences

l1 = ['Green', 'Red', 'Blue', 'Red', 'Orange', 'Black', 'Black', 'White', 'Orange']
l2 = [3, 5, 0, 3, 9, 5, 8, 0, 3, 8, 5, 8, 3, 5, 8, 1, 0, 2]


print("Original List:",l1)
print("Count the occurrence of each element of the said list:")
print(count_occurrences(l1))

print("Original List:",l2)
print("Count the occurrence of each element of the said list:")
print(count_occurrences(l2))
