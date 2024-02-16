'''Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. 
The program will print the numbers that are divisible by 5 in a comma separated sequence.
Sample Data : 0100,0011,1010,1001,1100,1001
Expected Output : 1010'''

data = "0100,0011,1010,1001,1100,1001"
binary_nos= data.split(',')
divisible = []
for i in binary_nos:
    decimal_no = int(i,2)
    if decimal_no % 5 == 0:
      divisible .append(i)

print(','.join(divisible))
   

