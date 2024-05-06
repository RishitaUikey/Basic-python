'''Write a  Python program to count the number of groups of non-zero numbers separated by zeros in a given list of numbers.
Original list:
[3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]
Number of groups of non-zero numbers separated by zeros of the said list: 4'''

def count_non_zero_groups(nums):
    count = 0
    in_group = False
    
    for num in nums:
        if num != 0:
            if not in_group:
                in_group = True 
        else:
            if in_group:
                count += 1 
                in_group = False 
                
    if in_group:
        count += 1
    
    return count

original_list = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]
print("Original list:")
print(original_list)
print("Number of groups of non-zero numbers separated by zeros of the said list:")
print(count_non_zero_groups(original_list))
