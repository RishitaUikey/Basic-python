''' Write a  Python program to find the indices of elements in a given list that are greater than a specified value.
Original list:
[1234, 1522, 1984, 19372, 1000, 2342, 7626]
Indices of elements of the said list, greater than 3000
[3, 6]
Original list:
[1234, 1522, 1984, 19372, 1000, 2342, 7626]
Indices of elements of the said list, greater than 20000
[]'''

def find_indices_greater_than(lst, value):
    indices = []
    for i in range(len(lst)):
        if lst[i] > value:
            indices.append(i)
    return indices

original_list1 = [1234, 1522, 1984, 19372, 1000, 2342, 7626]
value1 = 3000
print("Original list:")
print(original_list1)
print("Indices of elements of the given list, greater than", value1)
print(find_indices_greater_than(original_list1, value1))

original_list2 = [1234, 1522, 1984, 19372, 1000, 2342, 7626]
value2 = 20000
print("\nOriginal list:")
print(original_list2)
print("Indices of elements of the given list, greater than", value2)
print(find_indices_greater_than(original_list2, value2))
