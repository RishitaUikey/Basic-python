'''Write a Python program to multiply all the items in a dictionary.'''
mul=1
x={'a':37,'b':92,'c':56,'d':89}
for value in x.values():
    mul*= value
print(mul)