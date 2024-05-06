'''Write a  Python program to pair consecutive elements of a given list.
Original lists:
[1, 2, 3, 4, 5, 6]
Pair up the consecutive elements of the said list:
[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
Original lists:
[1, 2, 3, 4, 5]
Pair up the consecutive elements of the said list:
[[1, 2], [2, 3], [3, 4], [4, 5]]'''

def pair_consecutive_elements(lst):
    pairs = []
    for i in range(len(lst) - 1):
        pairs.append([lst[i], lst[i + 1]])
    return pairs

original_lists = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5]
]

for original_list in original_lists:
    print("Original list:")
    print(original_list)
    print("Pair up the consecutive elements of the said list:")
    print(pair_consecutive_elements(original_list))
    print()
