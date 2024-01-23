'''If a year is evenly divisible by 4, go to step 2. If not, it's not a leap year.
If a year is divisible by 100, go to step 3. If not, it is a leap year.
If a year is divisible by 400, it's a leap year. If not, it's not a leap year.'''

x=int(input("Enter a year: "))
if (x%4==0 and x%100!=0) or (x%400==0):
    print("Its a LEAP YEAR")
else:
    print("Its not a Leap Year ")
    