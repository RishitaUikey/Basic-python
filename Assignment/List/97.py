'''Write a  Python program to remove sublists from a given list of lists that contain an element outside a given range.
Original list:
[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
After removing sublists from a given list of lists, which contains an element outside the given range:
[[13, 14, 15, 17]]'''

def remove_sublists_outside_range(lst, min_val, max_val):
    filtered_lst = [sublist for sublist in lst if all(min_val <= element <= max_val for element in sublist)]
    return filtered_lst

original_list = [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
min_val = 13
max_val = 17

filtered_list = remove_sublists_outside_range(original_list, min_val, max_val)

print("Original list:")
print(original_list)
print("After removing sublists from a given list of lists, which contain an element outside the given range:")
print(filtered_list)
