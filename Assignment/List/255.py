'''Write a  Python program to perform a deep flattening of a list.
Sample Output:
Original list elements:
[1, [2], [[3], [4], 5], 6]
Deep flatten the said list:
[1, 2, 3, 4, 5, 6]
Original list elements:
[[[1, 2, 3], [4, 5]], 6]
Deep flatten the said list:
[1, 2, 3, 4, 5, 6]'''

def deep_flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result

sample_lists = [
    [1, [2], [[3], [4], 5], 6],
    [[[1, 2, 3], [4, 5]], 6]
]
for lst in sample_lists:
    print("Original list elements:")
    print(lst)
    print("Deep flatten the said list:")
    print(deep_flatten(lst))
