# Write a  Python program to import a built-in array module and display the namespace of the said module.

import array

def display_namespace(module):
    for name in dir(module):
        print(name)

print("Namespace of the array module:")
display_namespace(array)
