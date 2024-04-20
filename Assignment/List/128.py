''' Write a  Python program to calculate the sum of the numbers in a list between the indices of a specified range.
Original list:
[2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
Range: 8 , 10
Sum of the specified range:
29'''

def sum_in_range(nums, start, end):
    return sum(nums[start:end+1])

original_list = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
start_index = 8
end_index = 10

sum_of_range = sum_in_range(original_list, start_index, end_index)

print("Original list:")
print(original_list)
print("Range:", start_index, ",", end_index)
print("Sum of the specified range:")
print(sum_of_range)
