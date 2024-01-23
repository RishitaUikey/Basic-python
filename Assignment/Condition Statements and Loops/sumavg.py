'''Write a Python program to calculate the sum and average of 
n integer numbers (input from the user). Input 0 to finish.

sum=0
count=0
a=int(input("Enter the integers : "))
for i in a:
    if a==0:
        break
    else:
        sum+=sum
        count+=1
        average=sum/count
        print("The sum of integers= ",sum)
        print("The average of integers= ",average)    
'''
sum_numbers = 0
count = 0

while True:
    try:
        number = int(input("Enter an integer (enter 0 to finish): "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue

    if number == 0:
        break
    else:
        sum_numbers += number
        count += 1

# Avoid division by zero
if count == 0:
    average = 0
else:
    average = sum_numbers / count

print("Sum:", sum_numbers)
print("Average:", average)
