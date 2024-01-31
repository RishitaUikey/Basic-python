'''Write a Python program to change the position 
of every n-th value to the (n+1)th in a list.
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]'''

l=[0,1,2,3,4,5]
for i in range(0, len(l) - 1 ,2):
    l[i], l[i+1] = l[i+1], l[i]
print(l)


