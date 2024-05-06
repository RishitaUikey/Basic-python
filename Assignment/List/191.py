'''Write a  Python program to find the maximum and minimum values of the three given lists.
Original lists:
[2, 3, 5, 8, 7, 2, 3]
[4, 3, 9, 0, 4, 3, 9]
[2, 1, 5, 6, 5, 5, 4]
Maximum value of the said three lists:
9
Minimum value of the said three lists:
0'''

def max_min_values(list1, list2, list3):
    max_value = max(max(list1), max(list2), max(list3))
    min_value = min(min(list1), min(list2), min(list3))
    return max_value, min_value

list1 = [2, 3, 5, 8, 7, 2, 3]
list2 = [4, 3, 9, 0, 4, 3, 9]
list3 = [2, 1, 5, 6, 5, 5, 4]

max_value, min_value = max_min_values(list1, list2, list3)
print("Original lists:")
print(list1)
print(list2)
print(list3)
print("Maximum value of the said three lists:", max_value)
print("Minimum value of the said three lists:", min_value)
