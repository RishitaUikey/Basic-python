# Write a Python program to convert a tuple to a string.

x = (1,2,3,4,5)
x_string = ''.join(str(i) for i in x)
print("Tuple as a string:",x_string)