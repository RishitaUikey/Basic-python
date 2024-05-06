'''Write a  Python program to find all index positions of the maximum and minimum values in a given list of numbers.
Original list:
[12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
Index positions of the maximum value of the said list:
7
Index positions of the minimum value of the said list:
3, 11'''

def find_max_min_indices(lst):
    max_value = max(lst)
    min_value = min(lst)

    max_indices = [i for i, num in enumerate(lst) if num == max_value]
    min_indices = [i for i, num in enumerate(lst) if num == min_value]

    return max_indices, min_indices

original_list = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
max_indices, min_indices = find_max_min_indices(original_list)

print("Original list:")
print(original_list)
print("Index positions of the maximum value of the said list:")
print(max_indices)
print("Index positions of the minimum value of the said list:")
print(min_indices)
