'''Write a Python program to get a list, sorted in increasing order by the 
last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]'''
'''from operator import intergetter
l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_l=sorted(l,key=intergetter(-1))
print(sorted_l())

# Get user input for a list of numbers
numbers = int(input("Enter a list of numbers separated by spaces: "))

# Convert the input string to a list of integers
numbers_list = [int(x) for x in numbers.split()]

# Sort the list in ascending order
sorted_numbers = sorted(numbers_list)

# Print the sorted list
print("Numbers in ascending order:", sorted_numbers)
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


