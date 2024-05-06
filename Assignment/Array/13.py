'''Write a  Python program to convert an array to an ordinary list with the same items.
Original array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])
Convert the said array to an ordinary list with the same items:
[1, 3, 5, 3, 7, 1, 9, 3]'''

from array import array

arr = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array:", arr)
ordinary_list = arr.tolist()
print("Convert the said array to an ordinary list with the same items:")
print(ordinary_list)
