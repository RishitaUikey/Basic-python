'''Write a  Python program to round the numbers in a given list, print the minimum and maximum numbers and multiply the numbers by 5. Print the unique numbers in ascending order separated by space.
Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
Minimum value: 4
Maximum value: 22
Result:
20 25 45 55 60 70 80 90 110'''

def process_numbers(numbers):
    rounded_numbers = [round(num) for num in numbers]
    
    min_value = min(rounded_numbers)
    max_value = max(rounded_numbers)
    multiplied_numbers = [num * 5 for num in rounded_numbers]
    
    print("Minimum value:", min_value)
    print("Maximum value:", max_value)
    
    unique_numbers = sorted(set(multiplied_numbers))
    print("Result:")
    print(" ".join(map(str, unique_numbers)))

original_list = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
process_numbers(original_list)
