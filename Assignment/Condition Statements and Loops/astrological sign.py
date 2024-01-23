'''Write a Python program to display the astrological sign for a given date of birth.
Expected Output:

Input birthday: 15                                                      
Input month of birth (e.g. march, july etc): may                        
Your Astrological sign is : Taurus  '''

m=['January','February','March','April','May','June','July',\
         'August','September','October','November','December']
d =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

d=int(input("Input birthday: "))
m=input("Input month of birth (e.g. march, july etc):")
if(m=='March' and 21<=d<=31) or (m=='April' and 1<=d<=19):
    print("Your Astrological sign is : Aries")
elif(m=='April' and 20<=d<=30) or (m=='May' and 1<=d<=20):
    print("Your Astrological sign is : Taurus")
elif(m=='May' and 21<=d<=31) or (m=='June' and 1<=d<=20):
    print("Your Astrological sign is : Gemini")
elif(m=='June' and 21<=d<=30) or (m=='July' and 1<=d<=22):
    print("Your Astrological sign is : Cancer")
elif(m=='July' and 23<=d<=31) or (m=='August' and 1<=d<=22):
    print("Your Astrological sign is : Leo")
elif(m=='August' and 23<=d<=31) or (m=='September'and 1<=d<=22):
    print("Your Astrological sign is : Virgo")
elif(m=='September' and 23<=d<=30) or (m=='October' and 1<=d<=22):
    print("Your Astrological sign is : Libra")
elif(m=='October'and 23<=d<=31) or (m=='November' and 1<=d<=21):
    print("Your Astrological sign is : Scorpio")  
elif(m=='November'and 22<=d<=30) or (m=='December' and 1<=d<=21):
    print("Your Astrological sign is : Sagittarius")
elif(m=='December'and 22<=d<=31) or (m=='January' and 1<=d<=19):
    print("Your Astrological sign is : Capricorn")
elif(m=='January' and 20<=d<=31) or (m=='February' and 1<=d<=18):
    print("Your Astrological sign is : Aquarius")
elif(m=='February'and 19<=d<=29) or (m=='March' and 1<=d<=20):
    print("Your Astrological sign is : Pisces")  
else:
    print("Invalid Input")    
   



