'''Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing', add 'ly' instead. If the string length of the given 
string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly' '''

x = input("Enter the String : ")
if x[-3:]=='ing' :
    result = x + 'ly'
else: 
    result = x + 'ing'
print("Expected Result : ",result)