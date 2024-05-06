'''Write a Python program to remove a specified item using the index of an array.
Sample Output:
Original array: array('i', [1, 3, 5, 7, 9])
Remove the third item form the array:
New array: array('i', [1, 3, 7, 9])'''

from array import array

arr = array('i', [1, 3, 5, 7, 9])
print("Original array:", arr)
index_to_remove = 2 
removed_item = arr.pop(index_to_remove)
print("Remove the third item from the array:")
print("New array:", arr)
