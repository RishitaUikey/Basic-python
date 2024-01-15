'''Write a Python program to get the next day of a given date.
Expected Output:

Input a year: 2016                                                      
Input a month [1-12]: 08                                                
Input a day [1-31]: 23                                                  
The next date is [yyyy-mm-dd] 2016-8-24  '''

x=int(input("Enter the year: "))
y=int(input("Enter the month: "))
z=int(input("Enter the day: "))
if(1<=y<=12 and 1<=z<=31):
    if y==12 and z==31:
        x+=1
        y=1
        z=1
    
    else:
        if z==31:
            z=1 
            y+=1
        else:
            z+=1
        
    print("The next date is ",x,"-",y,"-",z)
else:
    print("Invalid input")