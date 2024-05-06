''' Write a Python program to create an instance of an OrderedDict using a given dictionary. Sort the dictionary during the creation and print the members of the dictionary in reverse order.
Sample Output:
Afghanistan 93
Albania 355
Algeria 213
Andorra 376
Angola 244
In reverse order:
Angola 244
Andorra 376
Algeria 213
Albania 355
Afghanistan 93'''

from collections import OrderedDict

def create_ordered_dict(input_dict):
    ordered_dict = OrderedDict(sorted(input_dict.items()))

    return ordered_dict

input_dict = {
    'Afghanistan': 93,
    'Albania': 355,
    'Algeria': 213,
    'Andorra': 376,
    'Angola': 244
}

ordered_dict = create_ordered_dict(input_dict)

print("In reverse order:")
for key, value in reversed(ordered_dict.items()):
    print(key, value)
