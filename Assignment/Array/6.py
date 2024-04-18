'''Write a  Python program to get the number of occurrences of a specified element in an array.
Sample Output:
Original array: array('i', [1, 3, 5, 3, 7, 9, 3])
Number of occurrences of the number 3 in the said array: 3'''

from array import array

arr = array('i', [1, 3, 5, 3, 7, 9, 3])

print("Original array:", arr)
element = 3
occurrences = arr.count(element)
print("Number of occurrences of the number", element, "in the said array:", occurrences)
