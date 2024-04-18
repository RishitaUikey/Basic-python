'''Write a Python program to insert an element at the beginning of a given Ordered Dictionary.
Sample Output:
Original OrderedDict:
OrderedDict([('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')])
Insert an element at the beginning of the said OrderedDict:
Updated OrderedDict:
OrderedDict([('color4', 'Orange'), ('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')])'''

from collections import OrderedDict

dict = OrderedDict([('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')])
dict.update({'color4': 'Orange'}, top=True)
print("Updated OrderedDict:")
print(dict)
