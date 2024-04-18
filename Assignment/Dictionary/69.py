'''Write a Python program to group the elements of a given list based on the given function.
Sample Output:
Original list & function:
[7, 23, 3.2, 3.3, 8.4] Function name: floor:
Group the elements of the said list based on the given function:
{7: [7], 23: [23], 3: [3.2, 3.3], 8: [8.4]}
Original list & function:
['Red', 'Green', 'Black', 'White', 'Pink'] Function name: len:
Group the elements of the said list based on the given function:
{3: ['Red'], 5: ['Green', 'Black', 'White'], 4: ['Pink']}'''

from itertools import groupby

def group_elements(lst, func):
    return {key: list(group) for key, group in groupby(sorted(lst, key=func), key=func)}

lst1 = [7, 23, 3.2, 3.3, 8.4]
func1 = lambda x: int(x)

grouped_dict1 = group_elements(lst1, func1)
print("Original list & function:")
print(lst1, "Function name: floor:")
print("Group the elements of the said list based on the given function:")
print(grouped_dict1)

lst2 = ['Red', 'Green', 'Black', 'White', 'Pink']
func2 = lambda x: len(x)

grouped_dict2 = group_elements(lst2, func2)
print("\nOriginal list & function:")
print(lst2, "Function name: len:")
print("Group the elements of the said list based on the given function:")
print(grouped_dict2)
