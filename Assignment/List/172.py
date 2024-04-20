'''Write a  Python program to remove the last N number of elements from a given list.
Original lists:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
Remove the last 3 elements from the said list:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]
Remove the last 5 elements from the said list:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34]
Remove the last 1 element from the said list:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3]'''

def remove_last_elements(lst, n):
    return lst[:-n]
original_list = [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
result1 = remove_last_elements(original_list, 3)
print("Remove the last 3 elements from the said list:")
print(result1)
result2 = remove_last_elements(original_list, 5)
print("Remove the last 5 elements from the said list:")
print(result2)
result3 = remove_last_elements(original_list, 1)
print("Remove the last 1 element from the said list:")
print(result3)
