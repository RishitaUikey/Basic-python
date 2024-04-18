'''Write a  Python program to append items to a specified list.
Sample Output:
Items in the list: [1, 2, 6, -8]
Append items from the list:
Items in the array: array('i', [1, 2, 6, -8])'''

from array import array

l = [1, 2, 6, -8]
arr = array('i', l)
print("Items in the list:", l)
for item in l:
    arr.append(item)
print("Append items from the list:")
print("Items in the array:", arr)
