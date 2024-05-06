''''builtins' module provides direct access to all 'built-in' identifiers of Python.
Write a Python program that imports the abs() function using the builtins module, 
displays the documentation of the abs() function and finds the absolute value of -155.'''

import builtins

print("Documentation of abs function:")
print(help(builtins.abs))

absolute_value = builtins.abs(-155)
print("Absolute value of -155:", absolute_value)
