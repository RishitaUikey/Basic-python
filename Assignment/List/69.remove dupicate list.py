'''Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]'''

l=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
s={tuple(i) for i in l}
new = [list(i) for i in s]
print("new list:",new)