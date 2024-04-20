'''Write a  Python program to compute the sum of non-zero groups (separated by zeros) of a given list of numbers.
Original list:
[3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1, 0, 0, 0]
Compute the sum of non-zero groups (separated by zeros) of the said list of numbers: [15, 38, 15, 27]'''

def sum_non_zero_groups(nums):
    sums = []
    current_sum = 0
    in_group = False
    
    for num in nums:
        if num != 0:
            current_sum += num
            in_group = True
        else:
            if in_group:
                sums.append(current_sum)
                current_sum = 0
                in_group = False
    
    if in_group:
        sums.append(current_sum)
    
    return sums

original_list = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1, 0, 0, 0]
print("Original list:")
print(original_list)
print("Compute the sum of non-zero groups (separated by zeros) of the said list of numbers:")
print(sum_non_zero_groups(original_list))
