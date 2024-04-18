''' Write a Python program to get array buffer information.
Sample Output:
Array buffer start address in memory and number of elements.
(140023105054240, 2)'''

from array import array

arr = array('i', [10, 20])
buffer_info = arr.buffer_info()
print("Array buffer start address in memory and number of elements:")
print(buffer_info)
