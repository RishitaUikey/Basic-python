# Write a Python program to sum all the items in a list.

x = input("Enter the numbers: ")
numbers = list(map(int, x.split()))
total = 0

for num in numbers:
    total += num
print("The sum of all items is:", total)

