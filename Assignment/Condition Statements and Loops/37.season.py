'''Write a Python program that reads two integers representing a month and day and prints the season for that month and day.
Expected Output:

Input the month (e.g. January, February etc.): july                     
Input the day: 31                                                       
Season is autumn 
 - Cold Weather Season (Winter) from December to February; 
 - Hot Weather Season (Summer) from March to May; 
 - South-West Monsoom Season (Rainy) from June to September; 
 - Season of Retreating Monsoon (Autumn) from October and November. '''

m = int(input("Enter the month: "))
d = int(input("Enter the date : "))
if(1<=m<=12 and 1<=d<=31):
    if(m==12 or m==1 or m==2):
        print("Winter Season")
    else:
        if(m==3 or m==4 or m==5):
            print("Summer Season")
        else:       
            if(m==6 or m==7 or m==8 or m==9):
                print("Rainy Season")
            else:
                if(m==10 or m==11):
                    print("Autumn Season")

else:
    print("In valid choice")
        