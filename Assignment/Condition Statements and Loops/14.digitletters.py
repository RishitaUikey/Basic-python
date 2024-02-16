'''Write a Python program that accepts a string 
and calculates the number of digits and letters.
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2'''

x=str(input("Enter the string: "))
b='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
c=('0','1','2','3','4','5','6','7','8','9')
letters_count=0
digits_count=0
for i in x:
    if i in b:
        letters_count+=1
    if i in c:
        digits_count+=1
print("letters",letters_count)    
print("Digits",digits_count) 
