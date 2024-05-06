'''Write a Python program to convert a given Bytearray to a Hexadecimal string.
Sample Output:
Original Bytearray :
[111, 12, 45, 67, 109]
Hexadecimal string:
6f0c2d436d'''

import binascii

def bytearray_to_hex(bytearray_input):
    hex_string = binascii.hexlify(bytearray_input).decode()

    return hex_string

bytearray_input = bytearray([111, 12, 45, 67, 109])
print("Original Bytearray:")
print(bytearray_input)
print("Hexadecimal string:")
print(bytearray_to_hex(bytearray_input))
