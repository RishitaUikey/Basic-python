'''Write a Python function to get a string made of the first three characters of a specified 
string. If the length of the string is less than 3, return the original string.
Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt'''

str1 = input("Enter the string: ")
if 3 >= len(str1):
    print("First_three :",str1)
elif len(str1) > 3:
    print("First_three : ",str1[:3])