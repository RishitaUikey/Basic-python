'''Write a Python program to calculate a dog's age in dog years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
Expected Output:

Input a dog's age in human years: 15                                    
The dog's age in dog's years is 73'''

dh=0
d=0
dh=int(input("Input a dog's age in human years:"))
if dh<=2:
    d=10.5*dh
    print("The dog's age in dog's years is",d)
elif dh>2:
    d= 2 * 10.5 + (dh - 2) * 4
    print("The dog's age in dog's years is",d)
else:
    print("Invalid Input")
    