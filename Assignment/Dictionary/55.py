'''Write a  Python program to access dictionary key's element by index.
Expected Output:
physics
math
chemistry'''

from collections import OrderedDict

my_dict = OrderedDict([('physics', 90), ('math', 95), ('chemistry', 85)])
keys = list(my_dict.keys())
for i in range(len(keys)):
    print(keys[i])
