'''Write a Python program that checks whether 
a string represents an integer or not.
Expected Output:

Input a string: Python                                                  
The string is not an integer. '''

x=input("Enter the string: ")
y='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
z=('0','1','2','3','4','5','6','7','8','9')
alp_count=0
num_count=0
for i in x:
    if i in z:
       num_count+=1
    elif i in y:
        alp_count+=1
    else:
        print("INVALID INPUT")

if alp_count>0 and num_count>0:
    print("The string is an Alpha Numeric")       
elif  alp_count==0 and num_count>0: 
    print("The string is an integer.")
elif alp_count>0 and num_count==0:
    print("The string is not an integer.")

else:
    print("INVALID INPUT")

