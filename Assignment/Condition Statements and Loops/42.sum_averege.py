'''Write a Python program to calculate the sum and average of
n integer numbers (input from the user). Input 0 to finish.'''

sum=0
count=0

while True:
    try:
        num=int(input("Enter the integer (Input 0 to finish): "))
    except ValueError:
        print("Invalid input")
        continue
    if num==0:
        break
    else:
        sum+=num
        count+=1

if count==0:
    avarage=0
else:
    average=sum/count

print("The sum of interger is ",sum)
print("The average of integer is ",average) 
    
