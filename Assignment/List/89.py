'''Write a  Python program to Zip two given lists of lists.
Original lists:
[[1, 3], [5, 7], [9, 11]]
[[2, 4], [6, 8], [10, 12, 14]]
Zipped list:
[[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]'''

list1 = [[1, 3], [5, 7], [9, 11]]
list2 = [[2, 4], [6, 8], [10, 12, 14]]

zipped_list = [x + y for x, y in zip(list1, list2)]

print("Zipped list:")
print(zipped_list)
