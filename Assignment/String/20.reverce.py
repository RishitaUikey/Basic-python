'''Write a Python function to reverse a string if its length is a multiple of 4.'''

str1 = input("Enter the string: ")
if len(str1) % 4 == 0:
    print(str1[::-1])