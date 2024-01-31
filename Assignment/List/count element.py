# Write a Python program to count the number of elements in a list within a specified range.

list=[10,123,15,60,75,90,34,111,123,234,695,432]
count=0
for i in list:
    if 1<=i<=100:
        count+=1
print(count)