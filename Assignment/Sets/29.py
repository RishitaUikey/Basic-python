# Write a  Python program to find the third largest number from a given list of numbers.Use the Python set data type.

def find_third_largest(numbers):
    unique_numbers = set(numbers)  
    sorted_numbers = sorted(unique_numbers, reverse=True)  
    if len(sorted_numbers) < 3:
        return "There are less than three unique numbers in the list."
    else:
        return sorted_numbers[2]  


numbers = [10, 20, 20, 30, 40, 50, 50, 60, 70]

third_largest = find_third_largest(numbers)

print("The third largest number is:", third_largest)
