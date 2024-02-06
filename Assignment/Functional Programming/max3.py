# Write a Python function to find the maximum of three numbers.

def maximum(a,b,c):
 
    if a>=b and a>=c:
        max_one=a
    elif b>=a and b>=c:
        max_one=b
    else:
        max_one=a
    return max_one

a=int(input("Enter a number = "))
b=int(input("Enter a number = "))
c=int(input("Enter a number = "))

max_one=maximum(a,b,c)
print("The maximum value is ",max_one)