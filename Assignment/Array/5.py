'''Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array's contents. Also, find the size of the memory buffer in bytes.
Sample Output:
Original array: array('i', [1, 3, 5, 7, 9])
Current memory address and the length in elements of the buffer: (139741883429512, 5)
The size of the memory buffer in bytes: 20'''

from array import array

arr = array('i', [1, 3, 5, 7, 9])
print("Original array:", arr)
memory_address, length = arr.buffer_info()
print("Current memory address and the length in elements of the buffer:", (memory_address, length))
buffer_size_bytes = length * arr.itemsize
print("The size of the memory buffer in bytes:", buffer_size_bytes)
