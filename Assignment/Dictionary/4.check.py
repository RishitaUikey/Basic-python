'''Write a Python script to check whether a 
given key already exists in a dictionary.'''

dict={'name':'Rishita','college':'YCCE','age':21,'DOB':28_10_2002,'branch':'CSE','roll_no':115}
user=input("Enter the user_key: ")  

if user in dict:
    print(f"{user} already exists in a dict")
else:
    print(f"{user} do not exists in a dict")