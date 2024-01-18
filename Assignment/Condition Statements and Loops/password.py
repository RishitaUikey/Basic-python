'''Write a Python program to check the validity 
of passwords input by users.
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.'''

a=str(input("Enter the password: "))
x='abcdefghijklmnopqrstuvwxyz'
y='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
z=('1','2','3','4','5','6','7','8','9')
b=('@','#','$','%','^','&','*','+','-','~','!','?','|','/',',','.')
x_count=0
y_count=0
z_count=0
b_count=0
if (6<=len(a)<=16):
    if x in a:
        x_count+=1
    if y in a: 
        y_count+=1   
    if y in a: 
        z_count+=1 
    if b in a: 
        b_count+=1

    if x in a and y in a and y in a and b in a:
        print("STRONG PASSWORD")
    else:
        print("WEAK PASSWORD")

   
       
   
        
    
        