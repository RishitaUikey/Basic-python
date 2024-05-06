''' Write a  Python program to find the maximum and minimum values in a given list within a specified index range.
Original list:
[4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
Index range:
3 to 8
Maximum and minimum values of the said given list within index range:
(5, 0)'''

def find_max_min_within_range(input_list, start_index, end_index):
    sublist = input_list[start_index:end_index+1]
    max_value = max(sublist)
    min_value = min(sublist)
    return max_value, min_value

original_list = [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
start_index = 3
end_index = 8
print("Original list:")
print(original_list)
print("Index range:", start_index, "to", end_index)
print("Maximum and minimum values of the said given list within index range:")
print(find_max_min_within_range(original_list, start_index, end_index))
