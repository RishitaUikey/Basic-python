'''Sum a list of numbers. Write a  Python program to sum the first number with the second and divide it by 2, then sum the second with the third and divide by 2, and so on.
Original list:
[1, 2, 3, 4, 5, 6, 7]
Sum the said list of numbers:
[1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
Original list:
[0, 1, -3, 3, 7, -5, 6, 7, 11]
Sum the said list of numbers:
[0.5, -1.0, 0.0, 5.0, 1.0, 0.5, 6.5, 9.0]'''

def sum_and_average_list(nums):
    result = []
    for i in range(len(nums) - 1):
        average = (nums[i] + nums[i + 1]) / 2
        result.append(average)
    return result

original_list1 = [1, 2, 3, 4, 5, 6, 7]
print("Original list:")
print(original_list1)
print("Sum the said list of numbers:")
print(sum_and_average_list(original_list1))

original_list2 = [0, 1, -3, 3, 7, -5, 6, 7, 11]
print("\nOriginal list:")
print(original_list2)
print("Sum the said list of numbers:")
print(sum_and_average_list(original_list2))
