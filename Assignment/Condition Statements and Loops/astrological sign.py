'''Write a Python program to display the astrological sign for a given date of birth.
Expected Output:

Input birthday: 15                                                      
Input month of birth (e.g. march, july etc): may                        
Your Astrological sign is : Taurus '''

month =[January, February, March, April, May, June, July,\
         August, September, October, November, December]
date =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
Astrological_sign=[Aries, Taurus, Gemini, Cancer, Leo, Virgo,\
         Libra, Scorpio, Sagittarius, Capricorn, Aquarius,Pisces]
Aries_month=[March, April, May]
Aries_date=[] 

b=int(input("Input birthday: "))
m=input("Input month of birth (e.g. march, july etc):")
if 