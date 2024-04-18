'''Write a  Python program to check if a nested list is a subset of another nested list.
Original list:
[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
[[1, 3], [13, 15, 17]]
If the one of the said list is a subset of another.:
True
Original list:
[[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
[[[3, 4], [5, 6]]]
If the one of the said list is a subset of another.:
True
Original list:
[[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
[[[3, 4], [5, 6]]]
If the one of the said list is a subset of another.:
False'''

def is_subset(list1, list2):
    return all(sublist in list2 for sublist in list1)

lists1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
lists2 = [[1, 3], [13, 15, 17]]
lists3 = [[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
lists4 = [[[1, 2], [2, 3]], [[3, 4], [5, 7]]]

subset1 = is_subset(lists1, lists2)
subset2 = is_subset(lists3, lists4)

print("Original list:")
print(lists1)
print(lists2)
print("If one of the lists is a subset of another.:")
print(subset1)

print("\nOriginal list:")
print(lists3)
print(lists4)
print("If one of the lists is a subset of another.:")
print(subset2)
