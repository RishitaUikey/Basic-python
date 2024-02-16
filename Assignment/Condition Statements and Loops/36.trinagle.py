'''Write a Python program to check if a triangle is equilateral, isosceles or scalene.
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.
Expected Output:

Input lengths of the triangle sides:                                    
x: 6                                                                    
y: 8                                                                    
z: 12                                                                   
Scalene triangle  

x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)'''

x, y, z = (input("Enter the value of a,b &c = ")).split()
if(x==y==z):
    print("Its an equilateral triangle")
elif(x==y!=z):
    print("Its an isoscales triangle ")
else:
    print("Its an scalene triangle ")


