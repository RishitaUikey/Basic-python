'''Write a Python program to count the elements in a list until an element is a tuple.'''

x = [1, 2, 3, (4, 5), 6, 7]
count = 0
for i in x:
    if isinstance(i, tuple):
        break 
    count += 1
print("Number of elements before a tuple:", count)
