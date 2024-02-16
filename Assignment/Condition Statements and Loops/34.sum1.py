'''Write a Python program to sum two integers. 
However, if the sum is between 15 and 20 it 
will return 20.'''

x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))
sum=x+y 
if 15<=sum<=20:
    sum=20
    print(sum)
else:
    print(sum)