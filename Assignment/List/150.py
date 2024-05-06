'''Write a  Python program to reverse a given list of lists.
Original list:
[['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]
Reverse said list of lists:
[['white', 'black', 'pink'], ['green', 'blue'], ['orange', 'red']]
Original list:
[[1, 2, 3, 4], [0, 2, 4, 5], [2, 3, 4, 2, 4]]
Reverse said list of lists:
[[2, 3, 4, 2, 4], [0, 2, 4, 5], [1, 2, 3, 4]]'''

def reverse_list_of_lists(input_list):
    input_list.reverse()
    for sublist in input_list:
        sublist.reverse()
    return input_list

original_list1 = [['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]
original_list2 = [[1, 2, 3, 4], [0, 2, 4, 5], [2, 3, 4, 2, 4]]
print("Original list 1:")
print(original_list1)
print("Reverse said list of lists:")
print(reverse_list_of_lists(original_list1))
print("\nOriginal list 2:")
print(original_list2)
print("Reverse said list of lists:")
print(reverse_list_of_lists(original_list2))
