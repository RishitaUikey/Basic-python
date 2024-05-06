# Write a Python program to iterate over two lists simultaneously.

a = [1,2,3,4,5,6]
b = ['a','b','c','d']

for a,b in zip(a,b):
    print(a,b)