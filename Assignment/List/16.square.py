'''Write a Python program to generate and print a list 
of the first and last 5 elements where the values 
are square numbers between 1 and 30 (both included).'''

l=[]
for i in range(1,31):
    square=i**2
    if i<31:
        l.append(square)

print("list of the first 5 elements=",l[:6])
print("list of the last 5 elements=",l[-5:])


