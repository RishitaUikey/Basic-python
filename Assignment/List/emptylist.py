# Write a Python program to check if a list is empty or not.

list=[]
list=input("Enter the list :").split()
list=[int(i) for i in list]

if not list:
    print("List is empty")
else:
    print("List is not empty")