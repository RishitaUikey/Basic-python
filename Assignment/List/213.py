'''Write a Python program to calculate the sum of two lowest negative numbers in a given array of integers.
An integer (from the Latin integer meaning "whole") is colloquially defined as a number that can be written without a fractional component. For example, 21, 4, 0, and -2048 are integers.
Original list elements: [-14, 15, -10, -11, -12, -13, 16, 17, 18, 19, 20]
Sum of two lowest negative numbers of the said array of integers: -27
Original list elements: [-4, 5, -2, 0, 3, -1, 4, 9]
Sum of two lowest negative numbers of the said array of integers: -6'''

def sum_of_two_lowest_negatives(numbers):
    negative_numbers = [num for num in numbers if num < 0]
    negative_numbers.sort()
    if len(negative_numbers) >= 2:
        return negative_numbers[0] + negative_numbers[1]
    else:
        return "Not enough negative numbers"

original_list1 = [-14, 15, -10, -11, -12, -13, 16, 17, 18, 19, 20]
original_list2 = [-4, 5, -2, 0, 3, -1, 4, 9]

print("Original list elements:", original_list1)
print("Sum of two lowest negative numbers of the said array of integers:", sum_of_two_lowest_negatives(original_list1))

print("Original list elements:", original_list2)
print("Sum of two lowest negative numbers of the said array of integers:", sum_of_two_lowest_negatives(original_list2))
