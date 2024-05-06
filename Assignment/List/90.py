'''Write a  Python program to count the number of lists in a given list of lists.
Original list:
[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
Number of lists in said list of lists:
4
Original list:
[[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
Number of lists in said list of lists:
3'''

def count_lists(list_of_lists):
    count = 0
    for sublist in list_of_lists:
        if isinstance(sublist, list):
            count += 1
    return count

list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]

num_lists = count_lists(list1)

print("Original list:")
print(list1)
print("Number of lists in said list of lists:")
print(num_lists)

list2 = [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
num_lists = count_lists(list2)

print("\nOriginal list:")
print(list2)
print("Number of lists in said list of lists:")
print(num_lists)
