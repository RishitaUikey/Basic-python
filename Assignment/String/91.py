'''Write a Python program to convert a given heterogeneous list of scalars into a string.
Sample Output:
Original list:
['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
Convert the heterogeneous list of scalars into a string:
Red,100,-50,green,w,3,r,12.12,False'''

def convert_to_string(input_list):
    result = ','.join(str(item) for item in input_list)
    return result
original_list = ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
print("Original list:")
print(original_list)
print("Convert the heterogeneous list of scalars into a string:")
print(convert_to_string(original_list))
