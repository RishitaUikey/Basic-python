'''Write a Python program to insert a given string at the beginning of all items in a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']'''

a = [1, 2, 3, 4]
b = "emp"
new = [b+str(i) for i in a]
print(new)