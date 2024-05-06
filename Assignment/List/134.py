''' Write a  Python program to find the difference between two lists including duplicate elements.
Original lists:
[1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
[1, 1, 2, 4, 5, 6]
Difference between two said list including duplicate elements):
[3, 3, 4, 7]'''

from collections import Counter

def list_difference(list1, list2):
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    difference = counter1 - counter2
    return list(difference.elements())

list1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
list2 = [1, 1, 2, 4, 5, 6]

print("Difference between two said lists including duplicate elements:")
print(list_difference(list1, list2))
