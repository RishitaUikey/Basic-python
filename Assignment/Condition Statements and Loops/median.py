''' Write a Python program to find the median of three values.
Expected Output:

Input first number: 15                                                  
Input second number: 26                                                 
Input third number: 29                                                  
The median is 26.0   '''
'''

'''

x=int(input("Input first number:"))
y=int(input("Input second number:"))
z=int(input("Input third number:"))

if x<y<z or x>y>z:
    print("The median is ",y)
elif x>z>y or x<z<y:
    print("The median is ",z)
else:
    print("The median is ",x)

