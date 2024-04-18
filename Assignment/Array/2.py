'''Write a Python program to append a new item to the end of the array.
Sample Output:
Original array: array('i', [1, 3, 5, 7, 9])
Append 11 at the end of the array:
New array: array('i', [1, 3, 5, 7, 9, 11])'''

from array import array

arr = array('i', [1, 3, 5, 7, 9])
arr.append(11)

print("Append 11 at the end of the array:")
print("New array:", arr)
