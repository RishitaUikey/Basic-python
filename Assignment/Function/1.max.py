# Write a Python function to find the maximum of three numbers.

def find_max(a,b,c):
    
    return max(a,b,c)
numbers = (input("Enter the numbers : "))
num1,num2,num3 = map(int,numbers.split())
maximum = find_max(num1,num2,num3)
print("the maximum of three numbers: ",maximum)