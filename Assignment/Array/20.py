''' Write a  Python program to get the length of an array.
Sample Output:
Length of the array is:
5'''

from array import array

arr = array('i', [10, 20, 30, 40, 50])
length = len(arr)
print("Length of the array is:")
print(length)
