'''Write a Python program to convert a month name to a number of days.
Expected Output:

List of months: January, February, March, April, May, June, July, August
, September, October, November, December                                
Input the name of Month: February                                       
No. of days: 28/29 days '''

m=['January','February','March','April','May','June','July',\
         'August','September','October','November','December']
m=input("Input the name of Month:")
if m=='January':
    print("No. of days in January: 31 days ")
elif m=='February':
    print("No. of days in February: 28/29 days ")
elif m=='March':
    print("No. of days in March: 31 days ")
elif m=='April':
    print("No. of days in April: 30 days ")
elif m=='May':
    print("No. of days in May: 31 days ")
elif m=='June':
    print("No. of days in June: 30 days ")
elif m=='July':
    print("No. of days in July: 31 days ")
elif m=='August':
    print("No. of days in August: 31 days ")
elif m=='September':
    print("No. of days in September: 30 days ")
elif m=='October':
    print("No. of days in October: 31 days ")
elif m=='November':
    print("No. of days in November: 30 days ")
elif m=='December':
    print("No. of days in December: 31 days ")
else:
    print("Invalid input")
