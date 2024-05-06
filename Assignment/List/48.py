# Write a Python program to print nested lists (each list on a new line) using the print() function.

animals = [['lion'], ['tiger'], ['Monkey'],['elephant'],['zebra']]
print('\n'.join([str(lst) for lst in animals])) 