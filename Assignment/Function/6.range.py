#  Write a Python function to check whether a number falls within a given range.

def number_in_range(upper,lower,num):

    return lower <= num <upper
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
num = int(input("Enter the number: "))

if number_in_range(upper,lower,num):
    print("Number falls within a given range.")
else:
    print("Number do not falls within a given range.")

     