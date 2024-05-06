'''Write a  Python program to get items from a given list with specific conditions.
Original list:
[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
Number of Items of the said list which are even and greater than 45
5'''

def filter_condition(lst):
    return len([num for num in lst if num % 2 == 0 and num > 45])
original_list = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
result = filter_condition(original_list)
print("Number of Items of the said list which are even and greater than 45:")
print(result)
