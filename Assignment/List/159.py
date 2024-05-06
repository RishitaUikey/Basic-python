'''Write a Python program to append the same value/a list multiple times to a list/list-of-lists.
Add a value(7), 5 times, to a list:
['7', '7', '7', '7', '7']
Add 5, 6 times, to a list:
[1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
Add a list, 4 times, to a list of lists:
[[1, 2, 5], [1, 2, 5], [1, 2, 5], [1, 2, 5]]
Add a list, 3 times, to a list of lists:
[[5, 6, 7], [1, 2, 5], [1, 2, 5], [1, 2, 5], [1, 2, 5]]'''

def append_same_value(value, times, to_list):
    for _ in range(times):
        to_list.append(value)
    return to_list

def append_list_multiple_times(sub_list, times, to_list_of_lists):
    for _ in range(times):
        to_list_of_lists.append(sub_list.copy())
    return to_list_of_lists

list1 = append_same_value(7, 5, [])
print("Add a value(7), 5 times, to a list:")
print(list1)
list2 = append_same_value(5, 6, [1, 2, 3, 4])
print("\nAdd 5, 6 times, to a list:")
print(list2)
list_of_lists1 = append_list_multiple_times([1, 2, 5], 4, [])
print("\nAdd a list, 4 times, to a list of lists:")
print(list_of_lists1)
list_of_lists2 = append_list_multiple_times([5, 6, 7], 3, [[1, 2, 5]])
print("\nAdd a list, 3 times, to a list of lists:")
print(list_of_lists2)
