''' Write a Python program to count the number of 
even and odd numbers in a series of numbers
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4  '''

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in x:
    if (i%2==0):
        print("Number of even numbers :",i)
    else:
        print("Number of odd numbers :",i)